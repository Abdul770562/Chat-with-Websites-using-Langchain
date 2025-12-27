# Chat with Websites using LangChain

A Python application that lets you **chat with any website** using **LangChain** and LLMs (e.g., OpenAI’s GPT models). This tool extracts and summarizes information from websites in response to your queries — making it easy to interact with live web content using natural language.

Powered by LangChain and Retrieval‑Augmented Generation (RAG) techniques.

---

## 🚀 Features

- 🕸️ Website Interaction — Retrieve and parse content directly from any URL.
- 🧠 LangChain Integration — Use LangChain to build the query pipeline and LLM interface.
- 💬 Conversational Chat — Ask questions about a website and get concise answers.
- 🔑 OpenAI Support — Works with OpenAI models (GPT-3.5, GPT-4, etc.).
- 📜 Simple UI/CLI — Easy local interaction through Python scripts or a basic interface.

---

## 📦 Installation

### 🧰 Prerequisites

- Python 3.8+
- An OpenAI API key

### 🔽 Clone the repo

```bash
git clone https://github.com/Abdul770562/Chat-with-Websites-using-Langchain.git
cd Chat-with-Websites-using-Langchain
```

### 📥 Install dependencies

```bash
pip install -r requirements.txt
```

### 🔧 Setup

Create a `.env` file in the project root (copy from an example file if provided) and add your OpenAI key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Make sure dependencies are installed and the `.env` file is configured.

---

## 🟢 Usage

### 🗨️ Chat from Terminal

Run the main script:

```bash
python src/main.py
```

You will be prompted to enter a website URL and then ask questions about the site:

Example session:

```text
Enter Website URL: https://example.com
Ask your question: What is this site about?
```

The bot will extract and summarize the answer for you.

---

## 🔍 How It Works (RAG)

This application uses a Retrieval‑Augmented Generation pipeline:

1. Fetch website content (HTML/text).
2. Extract and split text into chunks.
3. Use embeddings to index the data.
4. Query the vector store to find relevant information.
5. Use an LLM to generate responses based on the retrieved context.

---

## 🛠️ Customization

- Change LLM models — switch between GPT‑3.5 and GPT‑4 (or other models supported by LangChain).
- Improve parsing — integrate custom HTML extractors or advanced loaders.
- Add vectorstores — use Redis, Chroma, Weaviate, etc., instead of the default.

---

## 🧑‍🤝‍🧑 Contributing

Contributions are welcome! You can:

- Fix bugs
- Improve parsing logic
- Add new features (UI, better loaders)

Please open an issue or submit a pull request.

---

## 📜 License

This project is open source and available under the MIT License.

---

If you find this project helpful, please give it a star! ⭐
