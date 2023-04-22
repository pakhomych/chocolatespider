from scrapy.loader import ItemLoader
from email.policy import default
from itemloaders.processors import MapCompose, TakeFirst

class ChocolateProductLoader(ItemLoader):

    default_output_processor = TakeFirst()
    url_in = MapCompose(lambda x : 'https://hotelchocolat.com' + x)
