import os
from dotenv import load_dotenv
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
import openai

# Load environment variables
load_dotenv()

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


if __name__ == '__main__':
    documents = load_docs(directory)
    print(f"Number of documents ingested: {len(documents)}")
    chunks = split_docs(documents)
    print(f"Number of chunks created: {len(chunks)}")
    print(type(chunks[0]))

    api_key = os.getenv("OPENAI_API_KEY")

    for chunk in chunks:
        chunk = str(chunk)
        prompt = """I want you to play the role of a machine learning expert who can help train open ai models to 
        fine tune search results for a Q & A application on custom data.
        Create a jsonl file for the following data. Make the jsonl file as exhaustive as possible to enable semantic 
        search. The prompt will contain a possible question with as much detail as possible that can be asked on the 
        data provided and completion will contain a high-quality answer for the question with data provided only. 
        Do not create data that does not exist.

        provide the answer in the following jsonl format.
        {"prompt" : " ", "completion" : " "}
        """ + chunk

        response = openai.Completion.create(
          model="gpt-3.5-turbo",
          prompt=prompt,
          temperature=0,
          max_tokens=256,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0,
          stop=["END"]
        )

        print(response)
