import requests

headers = {'Authorization': 'Bearer 7a208aeb-ea98-414c-8e25-34d988f85892'}
uri = f'https://coda.io/apis/v1/docs/pOe5ixBASv/tables/grid-wWfa52dKst/columns'
res = requests.get(uri, headers=headers).json()

print(f'This table\'s columns: {", ".join(c["name"] for c in res["items"])}')
print(f'This table\'s columns: {", ".join(c["id"] for c in res["items"])}')
#print(f'This table\'s columns: {", ".join(c["value"] for c in res["items"])}')

# => This table's columns: Task, Duration (hr), Duration (min)
