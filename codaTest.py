# doc: memex
# tabela: sopa
# colunas: URL, title

# a url do doc é: https://coda.io/d/memex_dpOe5ixBASv
import requests

headers = {'Authorization': 'Bearer 7a208aeb-ea98-414c-8e25-34d988f85892'}
uri = 'https://coda.io/apis/v1/docs/pOe5ixBASv/tables/grid-wWfa52dKst'
#uri = f'https://coda.io/apis/v1/docs/pOe5ixBASv/tables/grid-wWfa52dKst/rows'

# params = {
#   'isOwner': True,
#   'query': 'New',
# }

params = {
  'query': '<column ID>:"Work out"',
}

req = requests.get(uri, headers=headers).json()

req.raise_for_status() # Throw if there was an error.
res = req.json()
print(f'Matching rows: {len(res["items"])}')



#print(res);
#print(f'The name of the first table is {res["items"][0]["name"]}')
#print(f'First doc is: {res["items"][0]["name"]}')
#print(f'Table {res["name"]} has {res["rowCount"]} rows')


# from codaio import Coda, Document
# # Initialize by providing a coda object directly
# coda = Coda('7a208aeb-ea98-414c-8e25-34d988f85892', 'https://coda.io/apis/v1/docs/pOe5ixBASv')
# doc = Document('pOe5ixBASv', coda=coda)

#doc.list_tables()