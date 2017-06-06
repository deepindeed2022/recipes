#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
import time
import random
import re

import urllib2
from bs4 import BeautifulSoup
import csv

from config import cites

reload(sys)
sys.setdefaultencoding('utf-8')

target_file = 'lianjia.csv'
def crawler_cite(cite, requesturl, pages):
   # 根据网页数设置范围
   for k in range(1, pages + 1):
      time.sleep(random.random()*120)
      # 根据网址获取网页
      req = urllib2.Request(requesturl % str(k))
      # 建立csv存储文件，wb写 a+追加模式
      csvfile = file(target_file, 'ab+')
      writer = csv.writer(csvfile)
      # 读取网页
      response = urllib2.urlopen(req)
      the_page = response.read()
      soup = BeautifulSoup(the_page, "lxml")
      # 解析网页
      list0 = []
      list1 = []
      list2 = []
      list3 = []
      list4 = []
      list5 = []
      list6 = []

      # 提取楼盘名称字段
      for tag in soup.find_all(name="div", attrs={"class": re.compile("col-1")}):
         ta1 = tag.find(name="a", attrs={"target": re.compile("_blank")})
         
         # 添加城市字段
         list0.append(cite)
         list1.append(ta1.string)
         
         # 提取建筑面积字段
         ta2 = tag.find(name="div", attrs={"class": re.compile("area")})

         list2.append(ta2.find(name="span").string if ta2 else '')

         # 提取在售状态字段
         ta3 = tag.find(name="span", attrs={"class": re.compile("onsold")})
         list3.append(ta3.string if ta3 else 0)
         # 提取住宅类型字段
         ta4 = tag.find(name="span", attrs={"class": re.compile("live")})
         list4.append(ta4.string if ta4 else 0)

      # 提取每平米均价字段
      for tag in soup.find_all(name="div", attrs={"class": re.compile("col-2")}):
         ta5 = tag.find(name="span", attrs={"class": re.compile("num")})
         list5.append(ta5.string if ta5 else 0)
         # 提取总价字段
         ta6 = tag.find(name="div", attrs={"class": re.compile("sum-num")})
         list6.append(ta6.find(name="span").string if ta6 else 0)

      # 将提取的数据合并
      data = []
      for i in range(0, len(soup.find_all(name="div", attrs={"class": re.compile("col-1")}))):
         data.append((list0[i], list1[i], list2[i],\
                      list3[i], list4[i], list5[i], list6[i]))
      # 将合并的数据存入csv
      writer.writerows(data)
      csvfile.close()
      print  "%s 第%d页完成" % (cite, k)


def main():
   for (cite, requesturl, pages) in cites[:1]:
      crawler_cite(cite, requesturl, pages)

if __name__ == '__main__':
   main()