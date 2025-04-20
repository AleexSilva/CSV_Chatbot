import pandas as pd
from decouple import config
import warnings
warnings.filterwarnings('ignore')

#Lnagchain
from langchain import OpenAI
from langchain_experimental.agents import create_csv_agent

df = pd.read_csv('../data/financial_data.csv')
df.head()

openai_api_key = config('OPENAI_API_KEY')

agent = create_csv_agent(
    OpenAI(api_key=openai_api_key), 
    '../data/financial_data.csv', 
    verbose=True,
    allow_dangerous_code = True
)

