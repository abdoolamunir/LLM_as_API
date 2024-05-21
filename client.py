import requests
import streamlit as st

def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/prompt1/invoke",
                             json={'input': {'topic': input_text}})
    return response.json()['output']

def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/prompt2/invoke",
                             json={'input': {'topic': input_text}})
    return response.json()['output']

st.title("LLM as API")
st.write("An example of LLM as API")

input_text = st.text_input('Write a description of:')
input_text1 = st.text_input('Write a haiku of:')
enter = st.button("Enter")
clear = st.button("Clear")

if enter and input_text:
    st.write(get_openai_response(input_text))

if enter and input_text1:
    st.write(get_ollama_response(input_text1))

if clear:
    st.empty()
