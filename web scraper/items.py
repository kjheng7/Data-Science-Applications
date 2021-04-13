# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazontestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name = scrapy.Field()
    product_author = scrapy.Field()
    product_price_whole = scrapy.Field()
    product_price_fraction = scrapy.Field()
    product_imagelink = scrapy.Field()

