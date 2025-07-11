import streamlit as st
from styles import inject_css
from vector import process_file
from prompts import get_chain

# 1) Page setup & CSS
st.set_page_config(page_title="DocuChat", layout="wide")
inject_css()

# 2) Chat history
if "history" not in st.session_state:
    st.session_state.history = []

# 3) Sidebar upload + vectorization
with st.sidebar:
    st.header("📂 Upload a document")
    upload = st.file_uploader(
        "Quick Q&A on your documents.",
        type=["csv","pdf","docx"]
    )

    retriever = None
    if upload:
        retriever, chunk_count = process_file(upload)
        st.success(f"📄 Document split into {chunk_count} chunks.")
        st.success("✅ Vector store initialized. You can now ask questions!")
        st.session_state.retriever = retriever

# 4) Main chat UI
st.title("💬 DocuChat")
chain = get_chain()

if st.session_state.get("retriever"):
    query = st.text_input("", placeholder="Type your question here...")
    if st.button("Send") and query:
        docs = st.session_state.retriever.get_relevant_documents(query)
        context = "\n\n".join(d.page_content for d in docs)
        answer = chain.invoke({"reviews": context, "question": query})
        st.session_state.history.append((query, answer))

    st.markdown("---")
    for q, a in reversed(st.session_state.history):
        st.markdown(
            f"<div class='user-bubble'><strong>You:</strong> {q}</div>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<div class='bot-bubble'><strong>Bot:</strong> {a}</div>",
            unsafe_allow_html=True
        )
else:
    st.info("Upload a document to start.")