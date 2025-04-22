import streamlit as st
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

# Langchain
from langchain import OpenAI
from langchain_experimental.agents import create_csv_agent

# Page configuration
st.set_page_config(
    page_title="CSV Data Analysis Bot",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for better spacing and layout
st.markdown("""
    <style>
    .main-container {
        padding: 2rem;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .header-container {
        display: flex;
        align-items: center;
        margin-bottom: 2rem;
    }
    .logo-container {
        margin-right: 20px;
    }
    .title-container {
        flex-grow: 1;
    }
    .data-container {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .query-container {
        background-color: #f0f7ff;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .response-container {
        background-color: #f0fff4;
        padding: 1.5rem;
        border-radius: 10px;
    }
    .footer {
        margin-top: 3rem;
        text-align: center;
        color: #6c757d;
    }
    </style>
""", unsafe_allow_html=True)

# Use secrets for API keys
openai_api_key = st.secrets["api_key"]

# Header with logo and title
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://s3-eu-west-1.amazonaws.com/tpd/logos-domain/6002ab2c312cb900013dfab3/255x0.png", width=100)
with col2:
    st.title('CSV Data Analysis Bot')
    st.subheader('Upload a CSV file and ask questions about your data')

st.markdown("---")

# File upload section
st.markdown("### 📁 Upload Your Dataset")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv", help="Upload your CSV data file here")

if uploaded_file is not None:
    # Create a progress bar for loading
    with st.spinner('Processing your file...'):
        progress_bar = st.progress(0)
        # Save the uploaded file locally
        csv_file_path = os.path.join("temp", uploaded_file.name)
        os.makedirs("temp", exist_ok=True)
        
        with open(csv_file_path, 'wb') as file:
            file.write(uploaded_file.getbuffer())
        
        progress_bar.progress(50)
        
        # Read the CSV file
        df = pd.read_csv(csv_file_path)
        
        progress_bar.progress(100)
    
    # Data preview section
    st.markdown("### 📊 Data Preview")
    with st.container():
        st.markdown('<div class="data-container">', unsafe_allow_html=True)
        
        # Display basic info about the dataset
        col1, col2, col3 = st.columns(3)
        col1.metric("Rows", df.shape[0])
        col2.metric("Columns", df.shape[1])
        col3.metric("File Size", f"{round(os.path.getsize(csv_file_path)/1024/1024, 2)} MB")
        
        # Add tabs for different views of the data
        tab1, tab2, tab3 = st.tabs(["Data Table", "Summary Statistics", "Column Info"])
        
        with tab1:
            st.dataframe(df, height=300)
        
        with tab2:
            st.write(df.describe())
        
        with tab3:
            col_info = pd.DataFrame({
                'Column': df.columns,
                'Type': df.dtypes,
                'Non-Null Count': df.count(),
                'Null Count': df.isnull().sum()
            })
            st.dataframe(col_info)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Create the agent
    with st.spinner('Initializing AI agent...'):
        agent = create_csv_agent(
            OpenAI(api_key=openai_api_key, temperature=0),
            csv_file_path,
            verbose=True,
            allow_dangerous_code=True
        )
    
    # Query section
    st.markdown("### 🤖 Ask Questions About Your Data")
    st.markdown('<div class="query-container">', unsafe_allow_html=True)
    
    query = st.text_input(
        "Enter your question:",
        placeholder="Example: What is the average of column X? or Show me the correlation between X and Y"
    )
    
    # Example questions for guidance
    with st.expander("Example questions you can ask"):
        st.markdown("""
        - What are the column names in this dataset?
        - How many rows have missing values?
        - What is the average value of [column]?
        - What is the correlation between [column1] and [column2]?
        - Can you show me a summary of the data?
        - What is the highest value in [column]?
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Response section
    if query:
        st.markdown("### 📝 Analysis Result")
        st.markdown('<div class="response-container">', unsafe_allow_html=True)
        
        with st.spinner('Analyzing your data...'):
            response = agent.run(query)
        
        st.write(response)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Add a footer
    st.markdown('<div class="footer">© 2025 CSV Data Analysis Bot - Powered by LangChain & OpenAI</div>', unsafe_allow_html=True)
else:
    # Display info when no file is uploaded
    st.info("👆 Please upload a CSV file to get started!")
    
    # Brief instructions
    st.markdown("""
    ### How to use this app:
    
    1. Upload a CSV file using the file uploader above
    2. View your data and statistics automatically
    3. Ask questions about your data in natural language
    4. Get instant analysis and visualizations
    
    This app uses AI to help you analyze and understand your data without writing code!
    """)