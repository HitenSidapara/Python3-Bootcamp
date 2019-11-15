# in this file we are use the external module scrapy
# http://books.toscrape.com/
# scrapy runspider -o books.csv book_scrapy.py  ==> run the file

import scrapy

class BookSpider(scrapy.Spider):
    name = 'bookspider'
    starts_url = ['http://books.toscrape.com/']

    # Automatically request the url

    def parse(self, response):
        for articles in response.css('article.product_pod'):
            yield {
                'price' : articles.css('.price_color::text').extract_first(),
                "title" : articles.css("h3 > a::arrt(title) ").extract_first()
            }