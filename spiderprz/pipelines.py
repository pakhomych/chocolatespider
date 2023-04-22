# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SpiderprzPipeline:
    def process_item(self, item, spider):
        return item

class PriceToUSDPipline:

    gbpToUsdRate = 1.3

    def process_item(self, item, spider):

        adapter = ItemAdapter(item)
        
        if(adapter.get('price')):

            floatPrice = float(adapter['price'])
            adapter['price'] = floatPrice * self.gbpToUsdRate

            return item

        else:

            raise Dropitem(f"Net ceny dlya tovara {item}")   

class RatingZerosPipline:

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if not adapter.get('rating'):
            adapter['rating'] = 0

            return item
        else:
            return item

class DuplicatePipline:

    def __init__(self):

        self.names_seen = set()

    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        if adapter['name'] in self.names_seen:

            raise DropItem(f"Dublikat nayden: {item!r}")

        else:

            self.names_seen.add(adapter['name'])

            return item
