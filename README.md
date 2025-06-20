# RAG QnA App with Streamlit

An interactive Question-Answering web application built with Streamlit that uses Retrieval-Augmented Generation (RAG) to provide accurate answers from PDF documents. Powered by a fine-tuned or custom LLM via Groq and Google Generative AI embeddings.

## Overview

This app allows users to upload a collection of PDF documents, creates vector embeddings from their content, and then answers user queries by retrieving relevant document chunks and generating responses with a large language model (LLM).

## Features

- Loads and processes multiple PDFs from a directory.
- Splits documents into smaller text chunks for better retrieval.
- Uses Google Generative AI embeddings to create semantic vector representations.
- Stores vectors in a FAISS vector store for efficient similarity search.
- Retrieves relevant text chunks based on user queries.
- Uses Groq’s LLM (`allam-2-7b` model) to generate context-aware answers.
- Interactive Streamlit interface for easy user input and response display.

## Installation

### Prerequisites

- Python 3.8+
- Streamlit
- LangChain and related packages
- FAISS
- dotenv for environment variables
- Access to Groq API and Google API keys

### Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/rag-qna-app.git
cd rag-qna-app
pip install -r requirements.txt
