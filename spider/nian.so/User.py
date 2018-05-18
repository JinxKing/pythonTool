# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

class User:
    def __init__(self,UID=532086):
        self.__initURL='http://nian.so/'
        self.__username=''
        self.__UID=UID


    # def login(self):
    #
    #
    # def getUID(self):
    #
    def getUsername(self):
        return self.__username


    def getAlbums(self):#返回记本id、记本url，修改username
        url=self.__initURL+'user_dream.php?uid='+str(self.__UID)
        contents=requests.get(url)
        contents=contents.text.encode(contents.encoding).decode('utf-8')
        pattern = re.compile('<div class="album_inner">.*?id=(.*?)\'.*?class="album_title".*?>(.*?)</div>',re.S)
        responses = re.findall(pattern,contents)
        soup=BeautifulSoup(contents,"html.parser")
        username=soup.find(attrs={'class':'album_user'})
        pattern=re.compile('<.*?>(.*?)<',re.S)
        result=re.search(pattern,str(username))
        if not result:
            self.__username="咸鱼用户"
        else:
            self.__username=result.group(1)
        return responses





# spider=User(36981)
# spider.saveAllImgs()
