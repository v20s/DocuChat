import tempfile, os
from langchain.document_loaders import CSVLoader, PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import docx

def process_file(uploaded_file):
    """
    1) Save the upload locally
    2) Load & chunk documents
    3) Build Chroma vector store
    4) Return (retriever, chunk_count)
    """
    # save
    path = os.path.join(tempfile.gettempdir(), uploaded_file.name)
    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # load
    ext = os.path.splitext(uploaded_file.name)[1].lower()
    if ext == ".csv":
        docs = CSVLoader(path).load()
    elif ext == ".pdf":
        docs = PyPDFLoader(path).load()
    else:
        word = docx.Document(path)
        paras = [p.text for p in word.paragraphs if p.text.strip()]
        docs = [Document(page_content="\n\n".join(paras), metadata={})]

    # chunk
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    n = len(chunks)

    # build vector store
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")
    db = Chroma(persist_directory=None, embedding_function=embeddings)
    if n > 0:
        db.add_documents(chunks)

    retriever = db.as_retriever(search_kwargs={"k": 5})
    return retriever, n