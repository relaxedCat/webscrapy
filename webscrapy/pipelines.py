# -*- coding: utf-8 -*-

from webscrapy.items import WebscrapyItem
from webscrapy.redis import redisPool
import csv
from requests.exceptions import RequestException
import requests
import os
import webscrapy.cache.cache as gc
EXCEL_PATH = './webscrapy/resource/csv/moive.csv'
FIRST = 1

class RedisPipeline(object):
    def process_item(self,item,spider):
        if isinstance(item,WebscrapyItem):
            redisPool.r.hset(item['title'],item['title'],item)
            print(redisPool.r.hget(item['title'],item['title']))
        else:
            print('no...')

class CsvPipeline(object):
    def process_item(self,item,spider):
        if isinstance(item,WebscrapyItem):
            print(os.getcwd())
            # global FIRST
            try:
                # if FIRST == 1 and os.path.exists(EXCEL_PATH):
                if gc.get_value('INDEX') is None and os.path.exists(EXCEL_PATH):
                    os.remove(EXCEL_PATH)
                    gc.set_value('INDEX',1)
                with open(EXCEL_PATH,'a',newline='',encoding='utf-8') as file:
                    write = csv.writer(file)
                    write.writerow([item['title'],item['actor'],item['image_url'],item['star'],item['critical'],item['quote']])
            except Exception as e:
                print(e)
                print(item)
            self.download_img(**item)


    def download_img(self,**kw):
        img_url = kw['image_url']
        try:
            response = requests.get(img_url)
            with open('./webscrapy/resource/img/'+kw['title']+'.jpg','wb') as f:
                f.write(response.content)
                f.close()
        except RequestException as e:
            print(e)
            pass


