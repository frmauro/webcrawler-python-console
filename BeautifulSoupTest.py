from bs4 import BeautifulSoup
import requests
import json
import re


class Container:
 
    # init method or constructor
    def __init__(self, url, title):
        self.url = url
        self.title = title

# function to extract html document from given url
def getHTMLdocument(url):
      
    # request for HTML document of given url
    response = requests.get(url)
      
    # response will be provided in JSON format
    return response.text


# assign required credentials
# assign URL
url_to_scrape = "https://www.scrapethissite.com/pages/simple/"

# create document
html_document = getHTMLdocument(url_to_scrape)

# create soap object
soup = BeautifulSoup(html_document, 'html.parser')


# find all the anchor tags with "href" 
# attribute starting with "https://"
# for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
#     # display the actual urls
#     print(link.get('href'))  

# for link in soup.find_all('a'):
#     # display the actual urls
#     print(link)  

title = soup.title
titleText = title.get_text()

containerObj = Container(url_to_scrape, titleText)

#print(containerObj.url)
#print(containerObj.title)


# convert into JSON:
containerJson = json.dumps(containerObj.__dict__)
print(containerJson)

# print(soup.get_text())


#print(html_document)

# import requests

# def handler(pd: "pipedream"):
#   token = f'{pd.inputs["coda"]["$auth"]["api_token"]}'
#   authorization = f'Bearer {token}'
#   headers = {"Authorization": authorization, "Content-Type": 'application/json'}
#   r = requests.get('https://coda.io/apis/v1/whoami', headers=headers)
#   # Export the data 
# for use in future steps
#   return r.json()


# import requests

# headers = {'Authorization': 'Bearer <your API token>'}
# uri = 'https://coda.io/apis/v1/docs'
# params = {
#   'isOwner': True,
#   'query': 'New',
# }
# res = requests.get(uri, headers=headers, params=params).json()

# print(f'First doc is: {res["items"][0]["name"]}')
# # => First doc is: New Document



