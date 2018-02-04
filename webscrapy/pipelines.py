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
from  webscrapy.spiders.rong360_sprider import Rong_360_Sprider
from webscrapy.common import common
from webscrapy.items import Rong360CrapyItem
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
            with open('./webscrapy/resource/img/'+str(kw['card_index'])+'_'+kw['card_nm']+'.jpg','wb') as f:
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
        return item
class Rong360Pipline(object):
    def process_item(self,item,spider):
        if isinstance(spider,Rong_360_Sprider):
            if isinstance(item,Rong360CrapyItem):
                detail_dic = self.do_page_by_url(**item)
                if 'privilege' not in detail_dic:
                    detail_dic['privilege'] = ''
                global FIRST
                try:
                    if FIRST == 1 and os.path.exists(EXCEL_PATH + 'credit_card.csv'):
                        FIRST+=1
                        os.remove(EXCEL_PATH + 'credit_card.csv')
                    with open(EXCEL_PATH+'credit_card.csv','a',newline='',encoding='utf-8') as file:
                        write = csv.writer(file)
                        write.writerow([item['card_index'],item['card_nm'],item['title'],item['image_url'],item['card_level'],item['card_currency'],item['cash_out_fee'],item['annual_fee_policy'],item['card_detail_url']
                                        ,detail_dic['base_inf'],detail_dic['privilege'],detail_dic['related_const']])
                except Exception as e :
                    logging.error(e)
                    pass
                cp = CsvPipeline()
                cp.download_img(**item)
    def do_page_by_url(self,**kw):
        url = kw['card_detail_url']
        html = common.get_one_page(url)
        if html != None:
            return common.parse_page(html,**kw)