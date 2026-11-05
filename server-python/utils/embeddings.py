from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_chroma.vectorstores import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

def create_db():
   docs = load_docs()
   vector_docs(docs)


def load_docs():
   loader = PyPDFDirectoryLoader("data")
   docs = loader.load()

   return docs

def vector_docs(docs):
   db = Chroma.from_documents(docs, HuggingFaceEmbeddings(), persist_directory="database")