class Results:
    def __init__(self, response):
        self._results = response.json()['searchResults']
        self._recipes = {}


    def parse(self):
        recipes = self._results[0]['results']
        for recipe in recipes:
            self._recipes[recipe['name']] = [recipe['image'], recipe['link'], recipe['content']]
