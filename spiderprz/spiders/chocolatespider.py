import scrapy
from spiderprz.items import SpiderprzItem
from spiderprz.itemloaders import ChocolateProductLoader


class ChocolatespiderSpider(scrapy.Spider):
    name = "chocolatespider"
    
    def start_requests(self):
        url = 'https://www.hotelchocolat.com/uk/shop/collections/'
        data = {
                "inStockOnly": "true",
                "start": "1",
                "sz": "250",
                "format": "page-element"
                }

        yield scrapy.FormRequest(url, formdata=data, callback=self.parse)

    def parse(self, response):

        products = response.css('div.product-tile')

        for product in products:

            chocolate = ChocolateProductLoader(item = SpiderprzItem(), selector = product)
            chocolate.add_css('name', 'div.product-name a::attr(title)'),
            chocolate.add_css('price', 'span.product-sales-price', re = r'\d+\.\d+'),
            chocolate.add_css('url', 'div.product-name a::attr(href)'),
            chocolate.add_css('rating', 'div.stars-rating-filled ::attr(style)', re = r'\d+')
            yield chocolate.load_item()

        pass
