#1) install flask: pip install flask
#2) go to app.py in terminal: cd BackEnd
#3) run file: flask run
import requests
from flask import Flask, render_template, request, jsonify, Response
from json_formatting import Results
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

APIpass = "5456LILYAc2024"
APIkey = "07a51a8ae2df4713b2c2fbe8b9607f50"
API_URL = "https://api.spoonacular.com/food/search"

@app.route('/')
def index():
    return jsonify({"name": "meal"}) #arbitrary dictionary for now

@app.route('/search', methods=['GET'])
def search():
    # query = request.form['query']  # Get the query from the form
    args = request.args
    query = args.get("query")
    params = {
        "apiKey": APIkey,
        "query": query,
        "number": 10
    }

    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        results = Results(response)
        results.parse()
        recipes = results._recipes
        return jsonify(recipes)
    else:
        errorResponse = jsonify({"detail": "Error occurred. Status code: " + str(response.status_code)})
        errorResponse.status = response.status_code
        return errorResponse

if __name__ == '__main__':
    app.run(port=8000)
