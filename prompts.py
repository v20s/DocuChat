from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

def get_chain():
    TEMPLATE = (
        "You are an expert in answering question from the given document. "
        "Context:\n{reviews}\n"
        "Question: {question}"
    )
    prompt = ChatPromptTemplate.from_template(TEMPLATE)
    llm = OllamaLLM(model="llama3.2")
    return prompt | llm
