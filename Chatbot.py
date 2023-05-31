from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)
import streamlit as st
from streamlit_chat import message
from utils import *
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Creating the webpage
st.set_page_config(page_title='Thoughtworks Academies - Finn the Finance Robot!', layout='wide')
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.markdown('''<img src='data:image/png;base64,{}' width=100% height=140>'''.format(img_to_bytes("assets/consulting_banner.png")), unsafe_allow_html=True)
st.title('Welcome to Finn! Your personal Finance Bot!')

st.write('''Hi! I am Finn. I am an AI-powered chatbot.\nI have available to me the Thoughtworks annual reports of the financial years of 2021 and 2022. I speak multiple languages so feel free to ask me questions in your language! 
I'm here as a small-scale experiment for us to try out.\n
Obviously nothing that I say could be taken as financial advice, and like all chatbots, I will generally tell you if I don't have the answer …  but I can sometimes produce information that's just plain wrong. 
\nBut hey, pull up a stool and ask me some questions!\n\n
I know I'm buggy, but I still welcome your feedback. Please mail us @ consulting-academy@thoughtworks.com\n\n
''')
st.divider()

# Setting up the chatbot area
if 'responses' not in st.session_state:
    st.session_state['responses'] = ["How can I assist you?"]

if 'requests' not in st.session_state:
    st.session_state['requests'] = []

llm = ChatOpenAI(model_name='gpt-3.5-turbo', openai_api_key=os.environ.get('OPENAI_API_KEY'))

if 'buffer_memory' not in st.session_state:
    st.session_state.buffer_memory = ConversationBufferWindowMemory(k=3, return_messages=True)

system_msg_template = SystemMessagePromptTemplate.from_template(
    template="""Play the role of a financial advisor and expert accountant. 
    Answer the question as truthfully as possible using the provided context, 
and if the answer is not contained within the context provided, say 'I don't know'.
Always provide the response in markdown text format""")

human_msg_template = HumanMessagePromptTemplate.from_template(template="{input}")

prompt_template = ChatPromptTemplate.from_messages(
    [system_msg_template, MessagesPlaceholder(variable_name="history"), human_msg_template])

conversation = ConversationChain(memory=st.session_state.buffer_memory, prompt=prompt_template, llm=llm, verbose=True)

# container for chat history
response_container = st.container()

# container for text box
text_container = st.container()

with text_container:
    query = st.text_input("Query: ", key="input")
    if query:
        with st.spinner("Querying..."):
            conversation_string = get_conversation_string()
            refined_query = query_refiner(conversation_string, query)
            context = find_match(refined_query)
            response = conversation.predict(input=f"Context:\n {context} \n\n Query:\n{query}")
        st.session_state.requests.append(query)
        st.session_state.responses.append(response)

with response_container:
    if st.session_state['responses']:

        for i in range(len(st.session_state['responses'])):
            message(st.session_state['responses'][i], key=str(i))
            if i < len(st.session_state['requests']):
                message(st.session_state["requests"][i], is_user=True, key=str(i) + '_user')
