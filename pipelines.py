# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

#在item通过管道文件的时候先保存到本地json文件，再将数据传输给redis库
class TiebaPipeline(object):
    def __init__(self):
        self.writer = open('tiezi.json','w')

    def process_item(self, item, spider):
        text = json.dumps(dict(item),ensure_ascii=False) + '\n'
        self.writer.write(text.encode('utf-8'))
        return item

    def close_spider(self,spider):
        self.writer.close()
