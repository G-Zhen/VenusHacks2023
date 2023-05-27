#First go to terminal and install: pip install requests
import requests
import json_formatting
# API info
#lchakhoy@uci.edu
#Pass: #5456LILYAc2024
# api key: 07a51a8ae2df4713b2c2fbe8b9607f50

APIpass = "5456LILYAc2024"
APIkey = "07a51a8ae2df4713b2c2fbe8b9607f50"
API_URL = "https://api.spoonacular.com/food/search"
params = {
    "apiKey": APIkey
}

response = requests.get(API_URL, params=params)
print(response) #code 200 = good to go

results = json_formatting.Results(response)
results.parse()
