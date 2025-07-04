import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA


load_dotenv()


loader = TextLoader("./data/doc.txt")
documents = loader.load()


splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = splitter.split_documents(documents)


embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


vectorstore = FAISS.from_documents(docs, embeddings)


llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2)


qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())


query = "What is LangChain?"
answer = qa.invoke(query)

print("Question:", query)
print("Answer:", answer)
