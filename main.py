import streamlit as st
from transformers import pipeline

classifier = pipeline("summarization")

st.set_page_config("Text summarizer" , page_icon="https://img.icons8.com/stickers/48/topic.png")

st.title("Text summarizer")

textbox = st.text_input('Enter the text to be summarized', placeholder="text")

if st.button('Summarize'):
    a = classifier(textbox)
    st.write(a)
