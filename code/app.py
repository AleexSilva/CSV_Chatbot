import streamlit as st
import pandas as pd
from decouple import config
import warnings
warnings.filterwarnings('ignore')


#Langchain
from langchain import OpenAI
from langchain_experimental.agents import create_csv_agent

openai_api_key = config('OPENAI_API_KEY')

st.title('CSV Data - RAG Chatbot')

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")


if uploaded_file is not None:
    csv_file_path = uploaded_file.name
    
    with open(csv_file_path, 'wb') as file:
        file.write(uploaded_file.getbuffer())
        
    df = pd.read_csv(csv_file_path)