__author__ = 'xXl'
from bs4 import BeautifulSoup
from webscrapy.items import XiuxiuCrapyItem
import scrapy
import logging
import time
import random
INDEX= 0
class XiuxiuMoiveSprider(scrapy.Spider):

    name = 'xiuxiuSprider'
    allowed_domains = ['movie.douban.com/']
    start_urls = ['https://movie.douban.com/subject/27038183/comments?status=P']

    def parse(self, response):
        global INDEX
        bs4_html = BeautifulSoup(response.text,'lxml')
        # print(bs4_html)
        for child in bs4_html.find(id='comments').find_all(class_='comment-item'):
            item = XiuxiuCrapyItem()
            INDEX+=1
            print(INDEX)
            print('P')
            print(27038183)
            print(child.find_all('div')[1].find(class_='comment-info').a.string)
            print(child.find_all('div')[1].find(class_='comment-info').find(class_='comment-time ')['title'])
            print(child.find_all('div')[1].find(class_='comment-info').find_all('span')[1]['class'][0][7:])
            print(child.find_all('div')[1].find(class_='comment-vote').span.string)
            print(child.find_all('div')[1].p.string)
            print('=================')

            item['comment_id'] = INDEX
            item['moive_id'] = 27038183
            if child.find_all('div')[1].find(class_='comment-info').a.string:
                item['user_name'] = child.find_all('div')[1].find(class_='comment-info').a.string.strip()
            item['status'] ='P'
            item['star'] = child.find_all('div')[1].find(class_='comment-info').find_all('span')[1]['class'][0][7:]
            item['time'] = child.find_all('div')[1].find(class_='comment-info').find(class_='comment-time ')['title']
            if child.find_all('div')[1].p.string:
                item['comment'] = child.find_all('div')[1].p.string.strip()
            if child.find_all('div')[1].find(class_='comment-vote').span.string:
                item['votes'] = child.find_all('div')[1].find(class_='comment-vote').span.string.strip()

            yield item
        try:
            if bs4_html.find(class_='next')['href']:
                print('https://movie.douban.com/subject/27038183/comments'+bs4_html.find(class_='next')['href'])
                time.sleep(1 + float(random.randint(1, 100)) / 20)
                url = 'https://movie.douban.com/subject/27038183/comments'+bs4_html.find(class_='next')['href']
                yield scrapy.Request(url,callback=self.parse,dont_filter=True)
            else:
                pass
        except Exception as e:
            logging.error(e)

