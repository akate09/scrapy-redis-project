# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tiebacrawl.items import TiebacrawlItem
from scrapy_redis.spiders import RedisCrawlSpider

#继承的父类是Rediscrawlspider
class TiebaSpider(RedisCrawlSpider):
    name = 'tieba'
    #必须加入redis_key，在服务器主机的客户端发送lpush命令驱动程序
    redis_key = 'tiebaspider:start_urls'
    

    #匹配页面链接并持续跟进
    page_urls = LinkExtractor(allow = r'tieba.baidu.com.*?ie=utf-8&pn=\d+')
    #匹配页面中帖子的链接，不用跟进
    link_urls = LinkExtractor(allow = r'/p/\d+')

    rules = (
        Rule(page_urls,follow = True),
        Rule(link_urls, callback='parse_item', follow=True)
    )


    def parse_item(self, response):
        item = TiebacrawlItem()
        try:
            item['title'] = response.xpath('//h3/text()').extract()[0]
        except Exception :
            item['title'] = ''
        reply_list = []
        for node in response.xpath('//div[@class="d_post_content j_d_post_content "]'):
            #将每条评论中的文字提取出来，因为可能还有<a>标签，故采用如下方法
            reply =''.join(node.xpath('.//text()').extract()).strip()
            reply_list.append(reply)
        item['reply'] = reply_list
        item['url'] = response.url      
        yield item
