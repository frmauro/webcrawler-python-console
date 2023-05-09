import requests


class CodaService:
     # init method or constructor
    def __init__(self, url, title):
        self.url = url
        self.title = title

    def getColumn(columnName):    
        headers = {'Authorization': 'Bearer 7a208aeb-ea98-414c-8e25-34d988f85892'}
        uri = f'https://coda.io/apis/v1/docs/pOe5ixBASv/tables/grid-wWfa52dKst/rows/'

        params = {
        'query': f'c-ILOZNEGduy:"{columnName}"',
        }

        req = requests.get(uri, headers=headers, params=params)
        res = req.json()
        return res

    def updateTitle(self):
        headers = {'Authorization': 'Bearer 7a208aeb-ea98-414c-8e25-34d988f85892'}
        uri = f'https://coda.io/apis/v1/docs/pOe5ixBASv/tables/grid-wWfa52dKst/rows/i-zUab2yBZcx/'

        payload = {
        'row': {
            'cells': [
            {'column': 'c-swYTqmkWLE', 'value': f'{self.title}'},
            ],
        },
        }

        req = requests.put(uri, headers=headers, json=payload)
        #req.raise_for_status()
        res = req.json()
        return res    