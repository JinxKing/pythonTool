#-*- coding:utf-8 -*-
import requests
import re
import config
from bs4 import BeautifulSoup
# from pyquery import PyQuery as pq
import random
import os
from multiprocessing import Process

def getAllURL():
    UA=random.choice(config.user_agent_list)
    headers = {'User-Agent': UA}
    url="http://zhainanshe.xyz/tuinvlang/list_1_1.html"
    response=requests.get(url,headers=headers)
    pattern=re.compile(r'发布于 (.*?)阅读',re.S)
    return re.findall(pattern,response.text.encode(response.encoding).decode('gbk'))

def getPage(content):
    soup=BeautifulSoup(content,"html.parser")
    parameter=soup.find_all("a", class_="thumbnail")[0]
    return 'http://zhainanshe.xyz'+parameter['href']

def downloadPage(url):
    UA=random.choice(config.user_agent_list)
    headers = {'User-Agent': UA}
    response=requests.get(url,headers=headers)
    response.encoding='gbk'
    soup=BeautifulSoup(response.text,"html.parser")
    article=(soup.find("article"))
    pattern=re.compile(r'<img alt="(.*?)" src="(.*?)"/>',re.S)
    items=re.findall(pattern,str(article))
    for item in items:
        title=item[0]
        path=title+"/"+item[1][-10:-4]+".jpg"
        if not os.path.exists(title):
            os.makedirs(title)
        url='http://zhainanshe.xyz'+item[1]
        response=requests.get(url,headers=headers)
        try:
            f=open(path,"ab")
            f.write(response.content)
            f.close()
            print(path)
        except OSError:
            print("跳过一张图片")




if __name__=='__main__':
    items=getAllURL()
    for item in items:
        url=getPage(item)
        downloadPage(url)
