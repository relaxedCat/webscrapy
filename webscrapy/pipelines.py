# -*- coding: utf-8 -*-

from webscrapy.items import WebscrapyItem
from webscrapy.redis import redisPool
import csv
from requests.exceptions import RequestException
import requests
import os
import webscrapy.cache.cache as gc
from webscrapy.items import XiuxiuCrapyItem
import logging
from webscrapy.spiders.xiuxiu_moive_sprider import XiuxiuMoiveSprider

EXCEL_PATH = './webscrapy/resource/csv/'
FIRST = 1

class RedisPipeline(object):
    def process_item(self,item,spider):
        if isinstance(item,WebscrapyItem):
            redisPool.r.hset(item['title'],item['title'],item)
            print(redisPool.r.hget(item['title'],item['title']))
        return item

class CsvPipeline(object):
    def process_item(self,item,spider):
        if isinstance(item,WebscrapyItem):
            print(os.getcwd())
            try:
                # if FIRST == 1 and os.path.exists(EXCEL_PATH):
                if gc.get_value('INDEX') is None and os.path.exists(EXCEL_PATH + 'moive.csv'):
                    os.remove(EXCEL_PATH + 'moive.csv')
                    gc.set_value('INDEX',1)
                with open(EXCEL_PATH + 'moive.csv','a',newline='',encoding='utf-8') as file:
                    write = csv.writer(file)
                    write.writerow([item['title'],item['actor'],item['image_url'],item['star'],item['critical'],item['quote']])
            except Exception as e:
                print(e)
                print(item)
            self.download_img(**item)
        return item

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


class XiuxiuMoivePipline(object):
    def process_item(self,item,spider):
        if isinstance(spider,XiuxiuMoiveSprider):
            if isinstance(item,XiuxiuCrapyItem):
                global FIRST
                try:
                    if FIRST == 1 and os.path.exists(EXCEL_PATH + 'xiuxiu.csv'):
                        FIRST+=1
                        os.remove(EXCEL_PATH + 'xiuxiu.csv')
                    with open(EXCEL_PATH+'xiuxiu.csv','a',newline='',encoding='utf-8') as file:
                        write = csv.writer(file)
                        write.writerow([item['comment_id'],item['moive_id'],item['user_name'],item['status'],item['star'],item['time'],item['comment'],item['votes']])
                except Exception as e :
                    logging.error(e)
                    pass

