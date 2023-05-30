import streamlit as st
from utils import *

st.set_page_config(
    page_title="Known Issues",
    layout='wide'
)
st.markdown('''<img src='data:image/png;base64,{}' width=100% height=140>'''.format(img_to_bytes("assets/consulting_banner.png")), unsafe_allow_html=True)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title("Known bugs and Issues")

st.subheader('Issue:')
st.markdown('''<img src='data:image/png;base64,{}' width=800 height=600>'''.format(img_to_bytes("assets/rate_limit.png")), unsafe_allow_html=True)
st.subheader('Cause:')
st.markdown('**This is due to the OpenAI rate limits for queries - Please retry after a short time**')