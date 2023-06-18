from langchain.document_loaders import PyPDFLoader
import os
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

with open('../Secrets/open_ai_api_key.txt', 'r') as file:
    key = file.read().rstrip()

os.environ['OPENAI_API_KEY'] = key

file_path = "/media/pranshumaan/TOSHIBA EXT/Dev/Project_Finmin/Budget_Speeches_PDF/bs199192.pdf"

loader = PyPDFLoader(file_path)
pages = loader.load_and_split()

faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings())

docs = faiss_index.similarity_search("How is the balance of payment crisis doing?", k=3)
for doc in docs:
    print(str(doc.metadata["page"]) + ":", doc.page_content[:300])
