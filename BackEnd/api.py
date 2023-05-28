#First go to terminal and install: pip install requests
import requests
import json_formatting
from dotenv import load_dotenv

load_dotenv()
import os

APIpass = os.getenv('APIpass')
APIkey = os.getenv('APIkey')
API_URL = "https://api.spoonacular.com/food/search"
params = {
    "apiKey": APIkey
}

response = requests.get(API_URL, params=params)
print(response) #code 200 = good to go

results = json_formatting.Results(response)
results.parse()
