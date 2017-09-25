# -*- coding: utf-8 -*-

# Scrapy settings for douban250 project

#BOT_NAME = 'douban250'

#SPIDER_MODULES = ['douban250.spiders']
#NEWSPIDER_MODULE = 'douban250.spiders'
BOT_NAME = 'tiebacrawl'
SPIDER_MODULES = ['tiebacrawl.spiders']
NEWSPIDER_MODULE = 'tiebacrawl.spiders'

#启用scrapy_redis的指纹去重系统
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

#启用scrapy_redis调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

#保留上一次爬取的缓存，方便下次从中断点开始下载
SCHEDULER_PERSIST = True

#采用优先队列的方式处理请求
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
DUPEFILTER_DEBUG =True

# 设置下载延迟
DOWNLOAD_DELAY = 0.25

# 禁用COOKIE，防止被检测
COOKIES_ENABLED = False


# 处理请求头，模仿浏览器登陆
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
   'Cache-Control':'max-age=0'
}

#模仿不同浏览器登陆，通过下载中间件随机选取
UserAgents = [
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)',
    'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
    'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13',
    'Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/4.1 Mobile Safari/533.1'   
        ]

#设置下载中间件，用于随机选择请求头
DOWNLOADER_MIDDLEWARES = {
    'tiebacrawl.middlewares.UserAgent': 200
}

#设置管道文件
ITEM_PIPELINES = {
    'tiebacrawl.pipelines.TiebaPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400
}
#设置链接的master端的ip/端口/密码
REDIS_HOST = '192.168.0.103'
REDIS_PORT = 6379
REDIS_PASS = 123456
#服务器端有密码的情况下要采用如下格式：
REDIS_URL = 'redis://root:123456@192.168.0.103:6379'





