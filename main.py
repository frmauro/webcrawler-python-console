from beautifulSoupService import SoupService
from codaService import CodaService

# assign URL
url_to_scrape = "https://www.scrapethissite.com/pages/simple/"

soupService = SoupService(url_to_scrape)
soup = SoupService.getSoupDocument(soupService)
# print(soup.title)
# print(soup.get_text())

codaService = CodaService(url_to_scrape, soup.title)
resColumn = CodaService.getColumn(url_to_scrape)
#print(resColumn)
#print(len(resColumn["items"]))

itemsLenght = len(resColumn["items"])

if itemsLenght == 0:
    print("Não foi encontrado nenhuma url com essa valor")

if itemsLenght > 0:
    #res = CodaService.updateTitle(codaService)
    #print(f'Updated row {res["id"]}')
    print("foi encontrado a url com essa valor")



#print(f'Row values are: {", ".join(str(v) for v in resColumn["values"].values())}')
