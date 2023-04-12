from bs4 import BeautifulSoup
import requests
import re

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

# title = soup.title
# print(title)

# print(soup.get_text())


#print(html_document)