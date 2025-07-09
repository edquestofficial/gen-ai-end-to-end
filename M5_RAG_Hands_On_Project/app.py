import os, streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
gemini = genai.GenerativeModel("gemini-1.5-flash")

def extract_text_from_pdfs(pdfs):
    return "".join([page.extract_text() for pdf in pdfs for page in PdfReader(pdf).pages])

def chunk_text(text):
    return CharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_text(text)

def create_vectorstore(chunks):
    embedder = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    return FAISS.from_texts(chunks, embedder)

def get_conversational_chain(vstore):
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    return ConversationalRetrievalChain.from_llm(
        ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5),
        retriever=vstore.as_retriever(), memory=memory
    )

def ask_gemini(query, context):
    prompt = f"You are answering questions based on the following context:\n\n{context}\n\nQuestion: {query}"
    return gemini.generate_content(prompt).text

def handle_question(user_question):
    if not st.session_state.vectorstore:
        st.warning("Upload and process PDFs first."); return
    docs = st.session_state.vectorstore.similarity_search(user_question, k=3)
    context = "\n\n".join(doc.page_content for doc in docs)
    answer = ask_gemini(user_question, context)
    
    chat = st.session_state.chat_history
    chat += [{"role": "user", "content": user_question}, {"role": "bot", "content": answer}]
    for msg in chat:
        st.write((user_template if msg["role"] == "user" else bot_template).replace("{{MSG}}", msg["content"]), unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon="📚")
    st.write(css, unsafe_allow_html=True)
    st.header("Chat with multiple PDFs 📚")
    
    for key in ["conversation", "chat_history", "vectorstore"]:
        st.session_state.setdefault(key, [] if "history" in key else None)

    user_q = st.text_input("Ask a question about your documents:")
    if user_q: handle_question(user_q)

    with st.sidebar:
        st.subheader("Your documents")
        pdfs = st.file_uploader("Upload PDFs & click Process", accept_multiple_files=True)
        if st.button("Process") and pdfs:
            with st.spinner("Processing..."):
                text = extract_text_from_pdfs(pdfs)
                chunks = chunk_text(text)
                vs = create_vectorstore(chunks)
                st.session_state.vectorstore = vs
                st.session_state.conversation = get_conversational_chain(vs)
                st.success("PDFs processed! Ask your questions.")

if __name__ == "__main__":
    main()
