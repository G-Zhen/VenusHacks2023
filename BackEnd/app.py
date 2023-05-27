#1) install flask: pip install flask
#2) go to app.py in terminal: cd BackEnd
#3) run file: flask run
import requests
from flask import Flask, render_template, request
from json_formatting import Results

app = Flask(__name__)

APIpass = "5456LILYAc2024"
APIkey = "07a51a8ae2df4713b2c2fbe8b9607f50"
API_URL = "https://api.spoonacular.com/food/search"

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/search', methods=['POST'])
# def search():
#     query = request.form['query']  # Get the query from the form
#     params = {
#         "apiKey": APIkey,
#         "query": query,
#         "number": 10
#     }

#     response = requests.get(API_URL, params=params)

#     if response.status_code == 200:
#         results = Results(response)
#         results.parse()
#         recipes = results._recipes
#         return render_template('results.html', recipes=recipes)
#     else:
#         return "Error occurred. Status code: " + str(response.status_code)

# if __name__ == '__main__':
#     app.run(debug=True)
