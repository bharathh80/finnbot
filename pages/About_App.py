import streamlit as st

st.set_page_config(
    page_title="About this app",
    layout='wide'
)

st.title("About Finnbot")
st.write("""
**Why did you make this chatbot?**\n
The consulting Academy is interested in trying out techniques for stimulating learning and discussion  which might scale well. We have a mission to uplift consulting capability for all Thoughtworkers. Annual reports are by law public data and not commercial-in confidence. so we thought we'd give this a try. It is an experiment we’re trying out just in Europe. We will be asking for feedback from you later on. 

**How reliable are the answers from this chatbot?**\n
The answers from this chatbot cannot be absolutely relied upon. Something few of us put together very quickly because we thought it might be interesting for learners to try out. Typically a chatbot based on an LLM will say “I don't know the answer to that” when it doesn't know the answer to something. But sometimes they do give some odd answers.

**What kind of questions can I ask this chatbot?**\n
You can ask it questions based on anything which is in the annual report, and anything the chatbot like gpt-3 might know about the wider internet. You can try asking it comparison questions, comparing financial results within the thought works financial reporting to the wider market. 


**Example Questions:**
- how did Thoughtworks’ earnings before tax change between 2021 and 2022?\n
- who were the directors in 2022?\n
- what was Thoughtworks’ retained earnings in 2021, and how does this compare to the market?\n

**What will the chatbot definitely not know?**\n
This chatbot will definitely not know anything about anything that happened in the wider world after September 2021, because that is where the date of which was used to train it cuts off. From the point of view of Thoughtworks’  specific  financial data, it has indexed our public financial year 2021 and financial year 2022 annual report data. 

**What documents has the chatbot ingested?**\n
The OpenAI LLM as a whole has been trained on a huge amount of data on the Internet up to September 2021. This chatbot has additionally ingested our to public annual reports for FY 2021 and FY2022,  which you can find [here](https://investors.thoughtworks.com/financial-information/annual-reports)

**How this app works**\n
![image](assets/architecture.png)
""")

