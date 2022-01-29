import streamlit as st
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

st.set_page_config("Text summarizer" , page_icon="https://img.icons8.com/stickers/48/topic.png")

st.title("Text summarizer")

textbox = st.text_input('Enter the text to be summarized', placeholder="text")

if st.button('Summarize'):
    st.write(summarizer(textbox, max_length=130, min_length=30, do_sample=False))
