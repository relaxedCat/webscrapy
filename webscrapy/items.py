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

class XiuxiuCrapyItem(scrapy.Item):
    comment_id = scrapy.Field()
    moive_id = scrapy.Field()
    user_name = scrapy.Field()
    status = scrapy.Field()
    star = scrapy.Field()
    time = scrapy.Field()
    comment = scrapy.Field()
    votes = scrapy.Field()
class Rong360CrapyItem(scrapy.Item):
    card_index = scrapy.Field()
    card_nm = scrapy.Field()
    title = scrapy.Field()
    image_url = scrapy.Field()
    card_level = scrapy.Field()
    card_currency = scrapy.Field()
    cash_out_fee = scrapy.Field()
    annual_fee_policy = scrapy.Field()
    card_detail_url = scrapy.Field()
    base_inf = ''
    privilege = ''
    related_const = ''

class CardDetailInfCrapyItem(scrapy.Item):
    base_inf = scrapy.Field()
    privilege = scrapy.Field()
    related_const = scrapy.Field()