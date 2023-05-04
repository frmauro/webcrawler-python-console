import requests

headers = {'Authorization': 'Bearer 7a208aeb-ea98-414c-8e25-34d988f85892'}
uri = f'https://coda.io/apis/v1/docs/pOe5ixBASv/tables/grid-wWfa52dKst/rows/i-zUab2yBZcx/'

payload = {
  'row': {
    'cells': [
      {'column': 'c-ILOZNEGduy', 'value': 'https://www.scrapethissite.com/pages/simple/'},
    ],
  },
}



req = requests.put(uri, headers=headers, json=payload)
req.raise_for_status() # Throw if there was an error.
res = req.json()

print(f'Updated row {res["id"]}')

# => This table's columns: Task, Duration (hr), Duration (min)
