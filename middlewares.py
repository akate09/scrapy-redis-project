#coding=utf-8

#从setting文件中导入浏览器列表
from tiebacrawl.settings import UserAgents
import random

class UserAgent(object):
    #porcess_request为必须写的方法，其他可以省略
    def process_request(self,request,spider):
        #随机选择浏览器
        useragent = random.choice(UserAgents)
        #给请求头添加选择的浏览器
        request.headers.setdefault('User-Agent',useragent)

   
