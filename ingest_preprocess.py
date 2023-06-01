import os
import pinecone
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.schema import Document
from langchain.vectorstores import Pinecone
from dotenv import load_dotenv
from utils import *
import openai

# Load environment variables
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Pick the right embedding model to create the vector data store
embeddings = SentenceTransformerEmbeddings(model_name='all-MiniLM-L12-v2')

# Specify where the documents are located
directory = './docs'


def load_docs(_directory):
    loader = DirectoryLoader(_directory)
    _documents = loader.load()
    return _documents


def split_docs(_documents, chunk_size=1000, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(_documents)
    return docs


documents = load_docs(directory)
print(f"Number of documents ingested: {len(documents)}")
chunks = split_docs(documents)
print(f"Number of chunks: {len(chunks)}")
responses = []

# Take each chunk and pre-process it using openai and then convert it back into a Langchain document for embedding
i = 0
for chunk in chunks:
    content = str(chunk).split('metadata={')[0].strip()
    metadata = str(chunk).split('metadata={')[1].strip()
    print(f"Processing chunk #{i} out of {len(chunks)}")
    response = query_preprocess(content)
    doc = Document(
        page_content=response.strip(),
        metadata={'source': metadata.split(':')[1][:-1]}
    )

    responses.append(doc)
    i += 1

print(len(chunks), len(responses))

pinecone.init(os.getenv('PINECONE_API_KEY'), environment=os.getenv('PINECONE_ENVIRONMENT'))
index_name = os.getenv('PINECONE_INDEX_NAME')

index = Pinecone.from_documents(responses, embeddings, index_name=index_name)
