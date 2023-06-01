import streamlit as st
from utils import *

st.set_page_config(
    page_title="About this app",
    layout='wide'
)
st.markdown('''<img src='data:image/png;base64,{}' width=100% height=140>'''.format(img_to_bytes("assets/consulting_banner.png")), unsafe_allow_html=True)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title("About Finnbot")
st.write("""
**Why did you make this chatbot?**\n
The consulting Academy is interested in trying out techniques for stimulating learning and discussion  which might scale well. We have a mission to uplift consulting capability for all Thoughtworkers. Annual reports are by law public data and not commercial-in confidence. so we thought we'd give this a try. It is an experiment we’re trying out just in Europe. We will be asking for feedback from you later on. 

**How reliable are the answers from this chatbot?**\n
The answers from this chatbot cannot be absolutely relied upon. Something few of us put together very quickly because we thought it might be interesting for learners to try out. Typically a chatbot based on an LLM will say “I don't know the answer to that” when it doesn't know the answer to something. But sometimes they do give some odd answers.

**What kind of questions can I ask this chatbot?**\n
You can ask it questions based on anything which is in the annual report, and anything the chatbot like gpt-3 might know about the wider internet. You can try asking it comparison questions, comparing financial results within the thought works financial reporting to the wider market. 


**Example Questions:**\n\n
***About the company and its finances***\n
- Compare and contrast the results of Thoughtworks in 2020 and 2021
- How did Thoughtworks perform during Covid
- What are some key highlights of the annual reports?
- How does the revenue of Thoughtworks compare to a typical IT services company
- What are the services offered by Thoughtworks

***About Finance and Strategy***\n
- Apply the Porters 5 forces model on Thoughtworks business model
- Tell me about EBITDA and how it helps indicate financial health of a company
- What financial indicators would indicate leakages in financial conditions for the company?
\n\n
Try asking it to “...explain as if I was a 10 year old”

**What will the chatbot definitely not know?**\n
This chatbot will definitely not know anything about anything that happened in the wider world after September 2021, because that is where the date of which was used to train it cuts off. From the point of view of Thoughtworks’  specific  financial data, it has indexed our public financial year 2021 and financial year 2022 annual report data. 

**What documents has the chatbot ingested?**\n
The OpenAI LLM as a whole has been trained on a huge amount of data on the Internet up to September 2021. This chatbot has additionally ingested our to public annual reports for FY 2021 and FY2022,  which you can find [here](https://investors.thoughtworks.com/financial-information/annual-reports)

**How this app works**\n""")
st.markdown('''<img src='data:image/png;base64,{}' width=700 height=400>'''.format(img_to_bytes("assets/architecture.png")), unsafe_allow_html=True)