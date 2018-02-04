import scrapy
import random
import logging
import time
from bs4 import BeautifulSoup
from webscrapy.items import Rong360CrapyItem
from webscrapy.items import CardDetailInfCrapyItem
INDEX= 0
CURRENT_PAGE = 1
class Rong_360_Sprider(scrapy.Spider):
    name = 'rong_360_sprider'
    allowed_domains = ['https://www.rong360.com']
    start_urls = ['https://www.rong360.com/credit/f-card-p1']


    def parse(self, response):
        global INDEX
        global CURRENT_PAGE
        print('=======================当前页：'+str(CURRENT_PAGE)+'===============')
        bs4_html = BeautifulSoup(response.text,'lxml')
        for child in bs4_html.find_all(class_='card-lists wrap-base'):
            item = Rong360CrapyItem()
            INDEX+=1
            print('==============第'+str(INDEX)+'张卡信息如下：=========')
            # print(child)
            # print('============详情如下：====================')
            print(INDEX)
            print('name:'+ child.find_all('p')[0].string)
            print('title:'+ child.find_all('p')[1].string)
            print('image_url:'+ child.find(class_='img')['src'])
            print('level:'+ child.find_all(class_='s1')[0].string + str(child.find(class_='txt2').find_all('li')[0].contents[1]))
            print('currency:'+ child.find_all(class_='s1')[1].string + str(child.find(class_='txt2').find_all('li')[1].contents[1]))
            if(len(child.find(class_='txt2').find_all('li')[2].contents) > 1):
                print('cash_fee:'+ child.find_all(class_='s1')[2].string + str(child.find(class_='txt2').find_all('li')[2].contents[1]))
            else:
                print('cash_fee:'+ child.find_all(class_='s1')[2].string)
            print('policy:'+ child.find_all(class_='s1')[3].string + child.find(class_='s3')['title'])
            print('detail_url:' + child.find(attrs={'click-class':'click'})['href'])

            item['card_index'] = INDEX
            item['card_nm'] = child.find_all('p')[0].string
            item['title'] = child.find_all('p')[1].string
            item['image_url'] = child.find(class_='img')['src']
            item['card_level'] = child.find_all(class_='s1')[0].string + str(child.find(class_='txt2').find_all('li')[0].contents[1])
            item['card_currency'] = child.find_all(class_='s1')[1].string + str(child.find(class_='txt2').find_all('li')[1].contents[1])
            if(len(child.find(class_='txt2').find_all('li')[2].contents) > 1):
                item['cash_out_fee'] = child.find_all(class_='s1')[2].string + str(child.find(class_='txt2').find_all('li')[2].contents[1])
            else:
                item['cash_out_fee'] = child.find_all(class_='s1')[2].string
            item['annual_fee_policy'] = child.find_all(class_='s1')[3].string + child.find(class_='s3')['title']
            item['card_detail_url'] = child.find(attrs={'click-class':'click'})['href']
            yield item
        try:
            if CURRENT_PAGE == 1 :
                url = 'https://www.rong360.com'+bs4_html.find(class_='next-page')['href']
                print('https://www.rong360.com'+bs4_html.find(class_='next-page')['href'])
                CURRENT_PAGE += 1
                yield scrapy.Request(url,callback=self.parse,dont_filter=True)
            if CURRENT_PAGE > 1 and bs4_html.find_all(class_='next-page')[1]['href']:
                print('https://www.rong360.com'+bs4_html.find_all(class_='next-page')[1]['href'])
                # time.sleep(1 + float(random.randint(1, 100)) / 20)
                url = 'https://www.rong360.com'+bs4_html.find_all(class_='next-page')[1]['href']
                CURRENT_PAGE += 1
                yield scrapy.Request(url,callback=self.parse,dont_filter=True)
            else:
                pass
        except Exception as e:
            logging.error(e.__traceback__)