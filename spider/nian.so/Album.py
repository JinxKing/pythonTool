# -*- coding: utf-8 -*-
import re
import os
import requests

class Album:

    def __init__(self,AlbumName,AlbumId):
        self.__AlbumName=AlbumName
        self.__AlbumId=AlbumId
        self.__moreURL='http://nian.so/more_step.php'
        self.__imginitURL='http://img.nian.so/step/'
        self.__userURL='http://nian.so/thing_right.php?id='
        self.__isHasNext=False

    def openAlbum(self,page):
        url=self.__moreURL
        data={'id':self.__AlbumId,'page':str(page)}
        contents=requests.post(url,data=data)
        contents=contents.text.encode(contents.encoding).decode('utf-8')
        pattern=re.compile(r'<a href="#!/images/(.*?)" class="img"',re.S)
        imgsURL=re.findall(pattern,contents)#匹配图片
        pattern=re.compile(r'<div id="step_more.*? class="step_more" onclick="loadmore.*?">更多</div>',re.S)
        result=re.search(pattern,contents)
        if result:
            self.isHasNext = True
        else:
            self.isHasNext = False
        return imgsURL

    def saveImg(self,path,imgURL):
        url=self.__imginitURL+imgURL
        contents=requests.get(url)
        with open(path,"wb") as f:
            f.write(contents.content)
            f.close()

    def getusername(self):
        url=self.__userURL+self.__AlbumId
        contents=requests.get(url)
        contents=contents.text.encode(contents.encoding).decode('utf-8')
        pattern= re.compile(r'class="thing_right_a_user">(.*?)<',re.S)
        result=re.search(pattern,contents)
        return result.group(1)

    def saveAllImgs(self):
            username=self.getusername()
            self.isHasNext=True
            countPage,countImge=0,0
            path=username+"/"+self.__AlbumName
            self.__makedir(path)
            while self.isHasNext:
                imgsURL=self.openAlbum(countPage)
                countPage+=1
                for imgURL in imgsURL:
                    imgpath=path+"/"+str(countImge)+".jpg"
                    self.saveImg(imgpath,imgURL)
                    countImge+=1

    def __makedir(self,path):
        path=path.strip()
        isExists=os.path.exists(path)
        if not isExists:
            os.makedirs(path)