import os
from PyPDF2 import PdfReader
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

import pickle

from typing import List, Tuple

from nicegui import Client, ui

#Passing secrets
with open('../Secrets/open_ai_api_key.txt', 'r') as file:
    key = file.read().rstrip()

os.environ['OPENAI_API_KEY'] = key

# Loading embeddings
with open("/media/pranshumaan/TOSHIBA EXT/Dev/Project_Finmin/vectorstore.pkl", "rb") as f:
    docsearch = pickle.load(f)

chain = load_qa_chain(OpenAI(), chain_type="stuff")

# UI

messages: List[Tuple[str, str, str]] = []
thinking: bool = False


@ui.refreshable
async def chat_messages() -> None:
    for name, text in messages:
        ui.chat_message(text=text, name=name, sent=name == 'You')
    if thinking:
        ui.spinner(size='3rem').classes('self-center')
    await ui.run_javascript('window.scrollTo(0, document.body.scrollHeight)', respond=False)


@ui.page('/')
async def main(client: Client):
    async def send() -> None:
        global thinking
        message = text.value
        messages.append(('You', text.value))
        docs = docsearch.similarity_search(message)
        thinking = True
        text.value = ''
        chat_messages.refresh()

        response = chain.run(input_documents=docs, question=message)
        messages.append(('FinMin Bot', response))
        thinking = False
        chat_messages.refresh()

    anchor_style = r'a:link, a:visited {color: inherit !important; text-decoration: none; font-weight: 500}'
    ui.add_head_html(f'<style>{anchor_style}</style>')
    await client.connected()

    with ui.column().classes('w-full max-w-2xl mx-auto items-stretch'):
        await chat_messages()

    with ui.footer().classes('bg-white'), ui.column().classes('w-full max-w-3xl mx-auto my-6'):
        with ui.row().classes('w-full no-wrap items-center'):
            placeholder = 'message'
            text = ui.input(placeholder=placeholder).props('rounded outlined input-class=mx-3') \
                .classes('w-full self-center').on('keydown.enter', send)
        
ui.run(title='Chat with FinMin')