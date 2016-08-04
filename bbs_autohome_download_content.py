#-*- coding=utf-8 -*-
import cookielib
import string
import re
import BaseHTTPServer
import urlparse
import threading
import json
import md5
import datetime
import time
import os
import subprocess
import traceback
import thread
import pymongo
import hashlib
import requests
import urllib
import urllib2
import lxml.etree
import codecs
import math 
import random
from time import sleep, ctime
from pymongo import MongoClient
from scrapy.http import Request, HtmlResponse
from scrapy.selector import HtmlXPathSelector

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

headers = {
  "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
  "Accept-Encoding":"gzip, deflate, sdch",
  "Accept-Language":"zh-CN,zh;q=0.8",
  "Cache-Control":"max-age=0",
  "Connection":"keep-alive",
  "Cookie":'ali_beacon_id=60.166.58.226.1439518952541.043431.3; cna=MrHcDcyVMwICATymOuKgF+Hg; ad_prefer="2015/10/23 16:25:19"; h_keys="%u516c%u53f8#%u62d6%u978b#%u8fde%u8863%u88d9#%u6fee%u9662%u6bdb%u8863#%u53a8%u536b%u6e05%u6d01#%u6c34%u6e29%u8868#%u6539%u6027PP#%u9970%u54c1%u5305%u88c5#%u5316%u5986%u54c1%u5305%u88c5"; ali_ab=60.166.58.226.1443419385082.8; JSESSIONID=8L78OIqv1-KB3V0cqe4U0AuUkUPA-nPuE4bP-Mva4; _csrf_token=1453965463188; _tmp_ck_0="AhAPwLGenDsU2obBvfytDvRiqpy%2BXWtFsW%2BYE6YrWj7%2FLNbrXYNIv9QOYZ1ZEwQbqXy22POB9BOQ%2FhhLcDygQqRZEvxiBUSc7Rpn5VJYsqLXdi%2FtML88giCdejVQSxg7JT%2FrY9z%2F7fjE%2BI3Gx%2BHW7v5lKBobuZNmM0%2BBrjei4cCNapl6KS0GupffhfKI5SxY%2F%2BLjIZg46uY2Ybm33SpV6qlJJpHwm3gpf%2BLxdl0A0bkcIhE2vfJPK2CzoNPqeQNnGAL%2B4FMUABsAH1TzTvi2WNj1bwCHQvdKndmmVR0URvN3pHzUlWBzSlZ%2BrkzQPBKz5mGMrbAqBiw5ckgRmUu9aw%3D%3D"; alicnweb=touch_tb_at%3D1453965493517; _ITBU_IS_FIRST_VISITED_=n; l=AoCAfkiuGy0CK72IiKcqIhqc0ARSCWTT; isg=1E3BFCA0DD17E68312F81EED656890FE',
  "Host":"s.1688.com",
  "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safar"
}

if __name__ == "__main__": 
  
  print 'start'
  fsr=open("bbs_autohome_list.txt","r")
  fsw=open("bbs_autohome_content.txt","a+")
  lines=fsr.readlines() 
  print len(lines)

  for line in lines:
    url = line.strip()
    #url = "http://blog.jrj.com.cn/6787875014,7994755a.html"
    print url+"\n"
    body=requests.get(url,timeout=15).text
    doc=lxml.etree.HTML(body)
    # scrapy shell 'http://club.autohome.com.cn/bbs/thread-o-200055-50803100-1.html'
    # scrapy shell 'http://club.autohome.com.cn/bbs/thread-o-200055-33259696-1.html'
    # scrapy shell 'http://club.autohome.com.cn/bbs/thread-o-200055-50785548-1.html'
    # hxs.select('//div[@class="conright fr"]/div/h1/div/text()').extract()
    # hxs.select('//div[@class="conright fr"]/div/div[@class="conttxt"]/div[@class="w740"]/text()|//div[@class="conright fr"]/div/div[@class="conttxt"]/div[@class="w740"]/p/span/font/span/text()|//div[@class="conright fr"]/div/div[@class="conttxt"]/div[@class="w740"]/p/span/text()').extract()
    # hxs.select('//div[@id="maxwrap-reply"]/div/div/div/div/div/text()').extract()

    info_title=doc.xpath('//div[@class="conright fr"]/div/h1/div/text()')
    if(len(info_title)>0):
      print "title:"+info_title[0].strip()
      fsw.write("title:"+info_title[0].strip()+"\n") 

    info_conttxt=doc.xpath('//div[@class="conright fr"]/div/div[@class="conttxt"]/div[@class="w740"]/text()|//div[@class="conright fr"]/div/div[@class="conttxt"]/div[@class="w740"]/p/span/font/span/text()|//div[@class="conright fr"]/div/div[@class="conttxt"]/div[@class="w740"]/p/span/text()')
    for info in info_conttxt:
      if(len(info.strip())>0): # 过滤空字符串
        print info.strip()
    	fsw.write(info.strip()+"\n") 

    info_content=doc.xpath('//div[@id="maxwrap-reply"]/div/div/div/div/div/text()')
    for info in info_content:         
      if(len(info.strip())>0): # 过滤空字符串
        print info.strip()
        fsw.write(info.strip()+"\n")

    # 暂停下载
    #time.sleep(random.randint(3, 30))

  print 'end'
