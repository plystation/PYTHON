
from urllib import request
import time
import json
import os
import re
import sys
import subprocess
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
#先提取各个po文的url
driver=webdriver.Chrome()
driver.get('http://m.xiaohongshu.com/user/profile/58995f1550c4b40be9a71202')
element1=driver.find_element_by_tag_name('body')
pages=0
while pages<=60:
    scoll=element1.send_keys(Keys.PAGE_DOWN)
    pages+=1
    time.sleep(0.5)
url=[]
content=driver.find_elements_by_css_selector('.note-item.note-item')
b=0
for a  in content:
    tag=content[b].find_element_by_tag_name('a')
    url1=tag.get_attribute('href')
    url.append(url1)
    b+=1
    time.sleep(0.5)
print(len(url))
#抓取title及desc
descs=[]
des=driver.find_elements_by_class_name('note-desc')
d=0
for count1 in des:
    desc=des[d].get_attribute('textContent')
    descs.append(desc)
    d+=1
    time.sleep(0.5)
f1=open('简介.txt','w',encoding='utf-8')
f1.write(str(descs))
f1.close()
titles=[]
e=0
titl=driver.find_elements_by_class_name('note-title')
for count2 in titl:
   title=titl[e].get_attribute('textContent')
   titles.append(title)
   e+=1
   time.sleep(0.5)
f2=open('标题.txt','w',encoding='utf-8')
f2.write(str(titles))
f2.close()
#打开po问url抓取数据
likes=[]
comments=[]
collects=[]
for count3 in range(len(url)):
    broswer=webdriver.Chrome()
    broswer.get(url[count3])
    spans=broswer.find_element_by_class_name('note-data')
    info=spans.find_elements_by_tag_name('span')
    for spans in info:
        like=info[0].get_attribute('textContent')
        comment=info[1].get_attribute('textContent')
        collect=info[2].get_attribute('textContent')
    likes.append(like)
    comments.append(comment)
    collects.append(collect)
    broswer.close()
    time.sleep(0.5)
l1=open("点赞.txt",'w',encoding='utf-8')
l1.write(str(likes))
l1.close()
c1=open("评论.txt",'w',encoding='utf-8')
c1.write(str(comments))
c1.close()
c2=open("收藏.txt",'w',encoding='utf-8')
c2.write(str(collects))
c2.close()




