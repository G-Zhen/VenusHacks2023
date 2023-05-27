import requests
import json 


class Results:
    def __init__(self, response):
        self._results = response.json()['searchResults']



    def parse(self):
        recipes = self._results[0]['results']
        print(recipes)
