# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from webscrapy.items import WebscrapyItem
from webscrapy.redis import redisPool
from webscrapy.settings import INDEX
class WebscrapyPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,WebscrapyItem):
            # print(item)
            redisPool.r.hset(item['title'],item['title'],item)