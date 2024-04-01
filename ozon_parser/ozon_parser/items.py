from scrapy.item import Item, Field


class DataItem(Item):
    os = Field()
    version = Field()
