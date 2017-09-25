# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TiebacrawlItem(scrapy.Item):
    #帖子标题
    title = scrapy.Field()
    #帖子的所有回复（包括楼主的）
    reply = scrapy.Field()
    #帖子的链接
    url = scrapy.Field()    
