from beautifulSoupService import SoupService
from codaService import CodaService

# assign URL
url_to_scrape = "https://www.scrapethissite.com/pages/simple/"

soupService = SoupService(url_to_scrape)
soup = SoupService.getSoupDocument(soupService)
# print(soup.title)
# print(soup.get_text())

codaService = CodaService(url_to_scrape, soup.title)
res = CodaService.updateTitle(codaService)

print(f'Updated row {res["id"]}')