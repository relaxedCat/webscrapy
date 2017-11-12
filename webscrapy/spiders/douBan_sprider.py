import re
import scrapy
from bs4 import BeautifulSoup
from webscrapy.items import WebscrapyItem

INDEX=0
class DouBanSprider(scrapy.Spider):
    name = 'douBanSprider'
    allowed_domains = ['movie.douban.com/']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self,response):
        bs4_html = BeautifulSoup(response.text,'lxml')
        global INDEX
        for child in bs4_html.find(class_='grid_view').find_all('li'):
            item = WebscrapyItem()
            INDEX+=1
            print(INDEX)
            print(child.div.find_all('div')[1].div.a.span.string)
            print(child.div.find_all('div')[1].find_all('div')[1].p.contents[0].strip())
            print(child.div.find_all('div')[0].a.img['src'])
            print(child.find(class_='star').find_all('span')[3].string)
            print(child.find(class_='rating_num').string)

            # title
            item['title'] = child.div.find_all('div')[1].div.a.span.string
            # actor
            item['actor'] = child.div.find_all('div')[1].find_all('div')[1].p.contents[0].strip()
            # # imag_url
            item['image_url'] = child.div.find_all('div')[0].a.img['src']
            # critical
            item['critical'] = child.find(class_='star').find_all('span')[3].string
            # star
            item['star'] = child.find(class_='rating_num').string
            # quote
            if child.find(class_='inq') is not None:
                print(child.find(class_='inq').string)
                item['quote'] = child.find(class_='inq').string
            else:
                item['quote'] = ''
            print("===================")
            yield item
        if bs4_html.find(class_='next').link is not None:
            next_page = self.start_urls[0]+ bs4_html.find(class_='next').contents[1]['href']
            print(next_page)
            yield scrapy.Request(next_page,callback=self.parse,dont_filter=True)
        else:
            print('over')
