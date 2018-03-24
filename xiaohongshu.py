import time
from selenium import webdriver
import requests
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib import request,parse
import re
driver=webdriver.Chrome()
driver.get('http://www.xiaohongshu.com/explore?openPage=yes&tab=babycare')
time.sleep(0.5)
elem=driver.find_element_by_tag_name('body')
no_of_pagedowns=150
while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1
post_host=driver.find_elements_by_class_name('comment')
hosts=[]
for hoster in post_host:
    host=hoster.text
    hosts.append(host)
print(hosts)  

post_po=driver.find_elements_by_class_name('note-info')
pos=[]
for por in post_po:
    po=por.text
    pos.append(po)
print(len(pos))  
post_like=driver.find_elements_by_class_name('like')
likes=[]
for liker in post_like:
    like=liker.text
    likes.append(like)
print(len(likes))
h=open('hostfile.txt','w')
h.write(str(hosts))
h.close()
p=open('posfile.txt','w')
p.write(str(pos))
p.close()
l=open('likefile.txt','w')
l.write(str(likes))
l.close()
post_link=driver.find_elements_by_class_name('note-href')
links=[]
for link in post_link:
    linker=link.get_attribute('href')
    links.append(linker)
print(len(links))
d=open('poslinkfile.txt','w')
d.write(str(links))
d.close()
user_link=driver.find_elements_by_xpath('//a[@target="_blank"]')
userlinks=[]
for link in user_link:
    linker=link.get_attribute('href')
    getlink=re.findall(r'w.*\bprofile\b.*\d|w.*\bprofile\b.*\D',str(linker))
    userlinks.append(getlink)
finallink=[]
n=len(userlinks)
i=0
while i<int(n):
    if i%2!=0:
       finallink.append(str(userlinks[i]))
    i+=1
u=open('userfile.txt','w')
u.write(str(finallink))
u.close()
print(len(finallink))



