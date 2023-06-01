import os

from sentence_transformers import SentenceTransformer
import pinecone
import openai
import streamlit as st
import base64
from pathlib import Path
from dotenv import load_dotenv

# Loading the environment variables
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
model = SentenceTransformer('all-MiniLM-L6-v2')

# Getting the vectors from the Pinecone Index
pinecone.init(api_key=os.getenv('PINECONE_API_KEY'), environment=os.getenv('PINECONE_ENVIRONMENT'))
index = pinecone.Index(os.getenv('PINECONE_INDEX_NAME'))


# Converting an image to bytes for streamlit rendering
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


# Finding the right chunk to match the required query in the index
def find_match(_input):
    try:
        input_em = model.encode(_input).tolist()
        result = index.query(input_em, top_k=2, includeMetadata=True)
        return result['matches'][0]['metadata']['text'] + "\n" + result['matches'][1]['metadata']['text']
    except:
        return "Pinecone index issue found"


# Pre-process data chunks for easier access
def query_preprocess(chunk):
    try:
        response = openai.Completion.create(
            model='text-davinci-003',
            prompt="""I want you to play the role of a ML expert who can create training data for a vector database. 
            Summarize and pre-process the text below that would optimize the data for semantic search when converted into 
            vectors that are stored in a vector database and matches found using the cosine function. 
            Only output the resulting text. Do not provide any other data\n\n""" + chunk,
            temperature=0,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        return response['choices'][0]['text']
    except Exception as e:
        return "OpenAI issue found - probable cause is Pinecone index unavailability or rate limit error. Please retry in a few minutes..."


# Redefining the query asked by the user based on the chat history and question asked
def query_refiner(conversation, query):
    try:
        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=f"Given the following user query and conversation log, formulate a question that would be the most relevant to provide the user with an answer from a knowledge base.\n\nCONVERSATION LOG: \n{conversation}\n\nQuery: {query}\n\n",
            temperature=0,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        return response['choices'][0]['text']
    except:
        return "OpenAI issue found - probable cause is Pinecone index unavailability or rate limit error. Please retry in a few minutes..."


# Constructing the history for the chat
def get_conversation_string():
    conversation_string = ""
    for i in range(len(st.session_state['responses']) - 1):
        conversation_string += "Human: " + st.session_state['requests'][i] + "\n"
        conversation_string += "Bot: " + st.session_state['responses'][i + 1] + "\n"
    return conversation_string
