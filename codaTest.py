import requests

headers = {'Authorization': 'Bearer <your API token>'}
uri = 'https://coda.io/apis/v1/docs'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers, params=params).json()

print(f'First doc is: {res["items"][0]["name"]}')
# => First doc is: New Document
