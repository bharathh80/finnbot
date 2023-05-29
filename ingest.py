import os

import pinecone
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Pinecone
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Pick the right embedding model to create the vector data store
embeddings = SentenceTransformerEmbeddings(model_name='paraphrase-multilingual-MiniLM-L12-v2')

# Specify where the documents are located
directory = './docs'


def load_docs(_directory):
    loader = DirectoryLoader(_directory)
    _documents = loader.load()
    return _documents


def split_docs(_documents, chunk_size=1000, chunk_overlap=200):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(_documents)
    return docs


documents = load_docs(directory)
print(f"Number of documents ingested: {len(documents)}")
chunks = split_docs(documents)
print(f"Number of chunks created: {len(chunks)}")

pinecone.init(os.getenv('PINECONE_API_KEY'), environment=os.getenv('PINECONE_ENVIRONMENT'))
index_name = os.getenv('PINECONE_INDEX_NAME')

index = Pinecone.from_documents(chunks, embeddings, index_name=index_name)
