import requests
import re
import config
import random
import os
from multiprocessing import Process

def getAllURL():
    url="http://www.mzitu.com/all/"
    response=requests.get(url)
    pattern=re.compile('日: <a href="(.*?)".*?>(.*?)</a>',re.S)
    return re.findall(pattern,response.text)

def getPage(url):
    UA=random.choice(config.user_agent_list)
    headers = {'User-Agent': UA}
    response=requests.get(url,headers=headers)
    pattern=re.compile('<div class="main-image">.*?<img src="(.*?)01.jpg".*?…</span><a href=.*?<span>(.*?)</span>',re.S)
    result= re.findall(pattern,response.text)
    return result[0]#只匹配一个

def saveMZ(URL,count,title):
    UA=random.choice(config.user_agent_list)
    headers = {'User-Agent': UA,'Referer':'http://www.mzitu.com'}
    n=0
    if not os.path.exists(title):
        os.makedirs(title)
    for i in range(1,count+1):
        url=URL
        if i<10:
            url=url+'0'+str(i)+".jpg"
        else:
            url+=str(i)+".jpg"
        print(url)
        path=title+"/"+str(n)+".jpg"
        n+=1
        response=requests.get(url,headers=headers)
        try:
            f=open(path,"ab")
            f.write(response.content)
            f.close()
        except OSError:
            print("跳过一张图片")

def thread(begin,end,results):
    for i in range(begin,end+1):
        item=results[i]
        response=getPage(item[0])
        saveMZ(response[0],int(response[1]),item[1])

if __name__=='__main__':
    results=getAllURL()
    p1=Process(target=thread,args=(13,69,results,))
    p2=Process(target=thread,args=(69,127,results,))
    p3=Process(target=thread,args=(127,170,results,))
    p4=Process(target=thread,args=(170,211,results,))#4月
    p1.start()
    p2.start()
    p3.start()
    p4.start()
