# 💬 DocuChat

[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-ff4b4b)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/Powered%20By-Ollama-black)](https://ollama.com)

> **DocuChat** is a lightweight and powerful chatbot that allows you to **ask questions** about your documents using **local LLMs**. Upload a PDF, Word, or CSV file and start chatting with your data — all in your browser.

---
## 📽️ Live Demo

https://github.com/v20s/DocuChat/assets/demo.mov

---

## 🖼️ UI Preview


---

## 🚀 Features

- 📂 Upload **PDF**, **DOCX**, or **CSV** documents  
- 🔎 Split and embed your documents locally with **Chroma + mxbai-embed-large**
- 🤖 Chat with the content using **LLaMA 3.2** from Ollama
- 💬 Clean, minimalistic **chat UI** built with Streamlit
- 🧠 All processing is **local** — **no cloud APIs required**

---

## 📦 Installation

- Python **3.9+**
- [Ollama](https://ollama.com/) installed and running locally  
  (Make sure the following models are pulled and available)
  ```bash
  ollama pull llama3:instruct
  ollama pull mxbai-embed-large
---

## 🔧 Setup

- Clone the repository
git clone https://github.com/yourusername/DocuChat.git
cd DocuChat
- Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
- Install dependencies
pip install -r requirements.txt
- Launch the app
streamlit run main.py

---
