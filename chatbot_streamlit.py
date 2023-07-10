import os
from PyPDF2 import PdfReader
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

import pickle

import streamlit as st

#Passing secrets
with open('../Secrets/open_ai_api_key.txt', 'r') as file:
    key = file.read().rstrip()

os.environ['OPENAI_API_KEY'] = key

# Loading embeddings
with open("/media/pranshumaan/TOSHIBA EXT/Dev/Project_Finmin/vectorstore.pkl", "rb") as f:
    docsearch = pickle.load(f)

chain = load_qa_chain(OpenAI(), chain_type="stuff")

# UI
messages = []

st.title('Chat with FinMin')

message = st.text_input('Enter your message', key='input_message')

if message:
    messages.append(('You', message))
    docs = docsearch.similarity_search(message)

    for name, text in messages:
        st.write(f'{name}: {text}')
        
    with st.spinner(text='Thinking...'):
        response = chain.run(input_documents=docs, question=message)
        messages.append(('FinMin Bot', response))

    st.write(f'FinMin Bot: {response}')
