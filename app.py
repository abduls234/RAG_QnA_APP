import os
import streamlit as st
from langchain.chains.retrieval import create_retrieval_chain
from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
os.environ["Google_API_KEY"] = os.getenv("GOOGLE_API_KEY")

st.title("RAG QnA APP with GEMMA Model")
llm = ChatGroq(groq_api_key=groq_api_key, model = "allam-2-7b")

prompt = ChatPromptTemplate.from_template(
    """
    Answer the Questions based on the provided context only.
    Please provide the most accurate response based on the questions.
    <context>
    {context}
    <context>
    Questions:{input}

    """
)
def vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
        st.session_state.loader = PyPDFDirectoryLoader("PDF")
        st.session_state.docs=st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=10)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:20])  # splitting
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)



prompt1 =  st.text_input("Enter Your Question: ")
if st.button("Creating Vectors"):
    vector_embedding()
    st.write("Vectors created")

import time

if prompt1:
    documents_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, documents_chain)

    start = time.process_time()
    response = retrieval_chain.invoke({'input': prompt1})
    st.write(response['answer'])


