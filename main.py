import streamlit as st
from summarizer import Summarizer

st.set_page_config("Text summarizer" , page_icon="https://img.icons8.com/stickers/48/topic.png")

st.title("Text summarizer")

textbox = st.text_input('Enter the text to be summarized', placeholder="text")

model = Summarizer()

if st.button('Summarize'):
    result = model(textbox, num_sentences=5, min_length=60)
    full = ''.join(result)
    st.write(full)
