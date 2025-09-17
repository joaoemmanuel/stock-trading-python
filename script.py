import requests
import os
import openai
from dotenv import load_dotenv
load_dotenv()

POLYGON_API_KEY = os.getenv('POLYGON_API_KEY')

LIMIT = 5
url = f'https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={POLYGON_API_KEY}'
response = requests.get(url)
data = response.json()
print(data['results']["ticker"])