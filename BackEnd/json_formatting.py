import requests
import json
from collections import namedtuple

Item = namedtuple("Item", ['name' 'image' 'link' 'content'])

class Results:
    def __init__(self, response):
        self._results = response.json()['searchResults']
        self._recipes = []


    def parse(self):
        recipes = self._results[0]['results']
        for recipe in recipes:
            item = Item([recipe['name'], recipe['image'], recipe['link'], recipe['content']])
            self._recipes.append(item)

