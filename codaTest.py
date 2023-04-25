import requests

headers = {'Authorization': 'Bearer 7a208aeb-ea98-414c-8e25-34d988f85892'}
uri = 'https://coda.io/apis/v1/docs/pOe5ixBASv/'
params = {
  'isOwner': True,
  'query': 'New',
}
res = requests.get(uri, headers=headers).json()

print(res);
#print(f'First doc is: {res["items"][0]["name"]}')


# from codaio import Coda, Document
# # Initialize by providing a coda object directly
# coda = Coda('7a208aeb-ea98-414c-8e25-34d988f85892', 'https://coda.io/apis/v1/docs/pOe5ixBASv')
# doc = Document('pOe5ixBASv', coda=coda)

#doc.list_tables()