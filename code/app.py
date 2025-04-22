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
    
    st.write("Uploaded CSV file:")
    
    st.dataframe(df)
    
    agent = create_csv_agent(OpenAI(api_key=openai_api_key), csv_file_path, verbose=True, allow_dangerous_code = True)
    
    query = st.text_input("Ask a question about the dataset:")

    if query:
        
        response = agent.run(query)
        
        st.write('Answer:')
        
        st.write(response)