# CSV Data Analysis Bot
A professional Streamlit application that allows users to upload CSV files and interact with them using natural language queries powered by LangChain and OpenAI.
Show Image
Features

## Upload and preview CSV files
View dataset statistics and information
Ask questions about your data in natural language
Get AI-powered analysis and insights
Professional UI with responsive design

## Setup Instructions
### Prerequisites

Python 3.7+
Pip package manager

### Installation

Clone this repository:
git clone https://github.com/yourusername/csv-data-analysis-bot.git
cd csv-data-analysis-bot

Install the required packages:
pip install -r requirements.txt

## Set up your OpenAI API key:


Option 1: Create a .env file in the project root:
OPENAI_API_KEY=your_api_key_here

Option 2: Use Streamlit secrets management as described in the Streamlit documentation



Running the Application
Run the application with the following command:
streamlit run app.py
The application will be available at http://localhost:8501 in your web browser.
Usage

Upload a CSV file using the file uploader
Review the data preview and statistics
Type your question in the text input field
View the AI-generated analysis and results

# Example Questions

What are the column names in this dataset?
How many rows have missing values?
What is the average value of [column]?
What is the correlation between [column1] and [column2]?
Can you show me a summary of the data?
What is the highest value in [column]?
Plot a histogram of [column].

## Project Structure

app.py - Main application file
.streamlit/config.toml - Streamlit configuration and styling
.streamlit/secrets.toml - Secure storage for API keys and sensitive information
requirements.txt - Required Python packages

Dependencies

- streamlit
- pandas
- langchain
- openai
- python-decouple

## License
This project is licensed under the MIT License - see the LICENSE file for details.