# -*- coding: utf-8 -*-
import urllib
import urllib.request
import re
import os

class Spider:

    def __init__(self):
        self.siteURL = 'http://www.gjxfj.gov.cn/xfgj/dxtj_2.htm'

    def getPage(self,url):
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        return response.read().decode('utf-8')

    def getContents(self):
        page = self.getPage(self.siteURL)
        pattern = re.compile('<li><a href="(.*?)".*?>(.*?)</a>.*?</li>', re.S)
        items = re.findall(pattern, page)
        for item in items:
            self.savedoc(item[1],item[0])

    def makedir(self,path):
        self.path=path.strip()
        isExists=os.path.exists(self.path)
        if not isExists:
            os.makedirs(self.path)
            return True

    def savedoc(self,title,contentURL):
        page=self.getPage(contentURL)
        pattern = re.compile('<p.*?>(.*?)</p>',re.S)
        items = re.findall(pattern,page)
        doc=self.path+"/"+title+".txt"
        doc = doc.replace(':','：')
        print(doc)
        f=open(doc,"w+")
        for item in items:
            item = item.replace(u'\xa0', u' ')
            item = re.sub(re.compile('<.*?>'),"",item)
            item = re.sub(re.compile('【.*?】'),"",item)
            item = re.sub(re.compile('&nbsp;'),"",item)
            f.write(item)


spider = Spider()
spider.makedir("信访文档")
spider.getContents()