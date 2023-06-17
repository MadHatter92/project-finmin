import os
from PyPDF2 import PdfReader
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

import pickle

#Passing secrets
with open('../Secrets/open_ai_api_key.txt', 'r') as file:
    key = file.read().rstrip()

os.environ['OPENAI_API_KEY'] = key

#Reading in all PDFs
folder_path = "/media/pranshumaan/TOSHIBA EXT/Dev/Project_Finmin/test_folder/"
loader = PyPDFDirectoryLoader(folder_path)
docs = loader.load()

# read data from the file and put them into a variable called raw_text
raw_text = ''
for doc in docs:
    text = doc.page_content
    if text:
        raw_text += text

# Splitting up the text into smaller chunks for indexing
text_splitter = CharacterTextSplitter(        
    separator = "\n",
    chunk_size = 1000,
    chunk_overlap  = 200, #striding over the text
    length_function = len,
)
texts = text_splitter.split_text(raw_text)

#Making the embeddings
embeddings = OpenAIEmbeddings()

docsearch = FAISS.from_texts(texts, embeddings)
# This is the vector store

with open("/media/pranshumaan/TOSHIBA EXT/Dev/Project_Finmin/vectorstore.pkl", "wb") as f:
    pickle.dump(docsearch, f)