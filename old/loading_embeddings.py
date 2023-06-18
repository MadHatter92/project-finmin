import os

from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

import pickle


with open('../Secrets/open_ai_api_key.txt', 'r') as file:
    key = file.read().rstrip()

os.environ['OPENAI_API_KEY'] = key

with open("/media/pranshumaan/TOSHIBA EXT/Dev/Project_Finmin/vectorstore.pkl", "rb") as f:
    docsearch = pickle.load(f)

chain = load_qa_chain(OpenAI(), chain_type="stuff")

message = "What are the names of all the Finance Ministers that have delivered these speeches?"

docs = docsearch.similarity_search(message)
response = chain.run(input_documents=docs, question=message)

print(response)