# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ComponentsItem(scrapy.Item):
    processors = scrapy.Field()
    gpus = scrapy.Field()
    motherboards = scrapy.Field()
    rams = scrapy.Field()
