# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    actor = scrapy.Field()
    image_url = scrapy.Field()
    star = scrapy.Field()
    critical = scrapy.Field()
    quote = scrapy.Field()

