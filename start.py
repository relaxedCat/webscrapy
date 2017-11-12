from scrapy.cmdline import execute
import webscrapy.cache.cache as gc
gc._init()
execute('scrapy crawl douBanSprider'.split())

