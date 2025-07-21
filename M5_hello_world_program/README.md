# 🔍 LangChain QA with Gemini and FAISS

This project demonstrates a simple **Retrieval-Augmented Generation (RAG)** pipeline using:

- [LangChain](https://www.langchain.com/)
- [Google Gemini LLM](https://ai.google.dev/)
- [HuggingFace Embeddings](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- [FAISS](https://github.com/facebookresearch/faiss) for vector storage

It loads a text file, splits it into chunks, creates vector embeddings, stores them in a FAISS index, and uses the Gemini LLM to answer a hardcoded query.

---

## 📁 Project Structure

```plaintext
.
├── data/
│   └── doc.txt           # Source document
├── main.py               # Main script
├── .env                  # API keys (not committed)
├── README.md             # You're here!
└── requirements.txt      # Optional - for pip/uv
```

---

## 🚀 Setup Instructions

This project uses [`uv`](https://github.com/astral-sh/uv), a modern and fast Python package manager.

### 1. Clone the repository

```bash
git clone https://github.com/edquestofficial/gen-ai-end-to-end.git
cd M5_full_scale_rag\hello_world_program
```

### 2. Create a virtual environment

```bash
uv venv
```

### 3. Install dependencies

```bash
uv sync
```

> Make sure you have `uv` installed. You can install it with:
> ```bash
> curl -Ls https://astral.sh/uv/install.sh | sh
> ```

### 4. Configure Environment Variables

Create a `.env` file in the root directory with your API key:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

You must have access to [Google Generative AI](https://ai.google.dev/) to use the Gemini model.

---

## ▶️ How to Run

```bash
python main.py
```

The script will:

- Load `doc.txt`
- Split it into 1000-character chunks
- Generate embeddings using `all-MiniLM-L6-v2`
- Store vectors in a FAISS index
- Use Gemini to answer the query: **"What is LangChain?"**

---

## 💬 Example Output

```
Question: What is LangChain?
Answer: LangChain is a framework for building applications powered by language models. It helps with chaining together components like LLMs, vector stores, and retrievers...
```

---

## 🛠 Tech Stack

- `langchain`
- `langchain-google-genai`
- `langchain-huggingface`
- `langchain-community`
- `faiss-cpu`
- `python-dotenv`
- `uv` (for dependency management)

---

## 📚 References

- [LangChain Docs](https://docs.langchain.com/)
- [HuggingFace Sentence Transformers](https://www.sbert.net/)
- [Google Generative AI](https://ai.google.dev/)
- [FAISS - Facebook AI Similarity Search](https://github.com/facebookresearch/faiss)

---

## ✅ To-Do / Suggestions

- [ ] Accept dynamic user input via CLI or web UI
- [ ] Add support for more file types (PDF, CSV)
- [ ] Handle multiple documents
- [ ] Save/load FAISS index for persistence

