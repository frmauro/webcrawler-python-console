# command to run app: "scrapy runspider myspider.py -O imdb.json"
import scrapy

# class BlogSpider(scrapy.Spider):
#     name = 'blogspider'
#     start_urls = ['https://www.zyte.com/blog/']

#     def parse(self, response):
#         for title in response.css('.oxy-post-title'):
#             yield {'title': title.css('::text').get()}

#         for next_page in response.css('a.next'):
#             yield response.follow(next_page, self.parse)

class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):
        for filmes in response.css('.titleColumn'):
            yield{
                'titulo': filmes.css('.titleColumn a::text').get(),
                'ano': filmes.css('.secondaryInfo ::text').get()[1:-1],
                'nota': response.css('strong::text').get()
            }
