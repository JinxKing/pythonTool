# # -*- coding:utf-8 -*-
 
# import requests
# import re
 
# class Spider:
 
#     #页面初始化
#     def __init__(self):
#         # self.siteURL = 'http://2.famecl.com/idleFish-F2e/app-basic/item.html?itemid=563677697983'
#         self.siteURL = "http://h5api.m.taobao.com/h5/mtop.taobao.idle.item.detail/3.0/?jsv=2.4.2&appKey=12574478&t=1515310122004&sign=474e0299a1934254f7cb555158d012c8&api=mtop.taobao.idle.item.detail&v=3.0&dataType=json&AniCreep=true&AntiFlool=true&jsonpIncPrefix=weexcb&ttid=2018@weex_h5_0.12.11&type=originaljson&c=00860c6f376b0ea4cd3b3186233c57d0_1515312642428;c20f01c74cd58cac1d147121e80feabb&data={%22itemId%22:563677697983}"

#     def getPage(self):
#         url = self.siteURL
#         headers = {'Content-Encoding':'gzip','Referer':'http://www.mzitu.com','MTOP-x-provider':'e70f55be7a0f9df6dff8095ee0f1cee8692aac86058b8e25caf22989df4731e8'}
#         response=requests.get(url,headers=headers)
#     	# pattern =re.compile('<a onclick=\'window.open.*?index.html.(.*?)".*?title=\'(.*?)\'',re.S)
#    		# results=re.findall(pattern,str(response.text))
#         return response.text

# spider = Spider()
# print(spider.getPage

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import requests
from bs4 import BeautifulSoup
import re

driver = webdriver.Chrome(r'C:\Users\L\AppData\Local\Google\Chrome\Application\chromedriver.exe')
driver.get("http://2.famecl.com/idleFish-F2e/app-basic/item.html?itemid=563677697983")
# assert "百度" in driver.title
# select = Select(driver.find_element_by_name('Cbo_LX'))
# select.select_by_index(2)


# elem3.send_keys(Keys.RETURN)
print (driver.page_source)

cookie= driver.get_cookies()#返回list（包含多个字典，每个cookie单独为个字典包括name和value）
# print(cookie)
#输出#[{'domain': 'www.ycjw.zjut.edu.cn', 'httpOnly': True, 'name': 'ASP.NET_SessionId', 'path': '/', 'secure': False, 'value': 'diq2fmidydgh12552lzdjp55'}, {'domain': 'www.ycjw.zjut.edu.cn', 'httpOnly': True, 'name': 'ASP.NET_SessionId_NS_Sig', 'path': '/', 'secure': False, 'value': 'oenCV6mdzWdh_VC_'}]
# print(cookie[0]['value']+"\t"+cookie[1]['value'])

# url = 'http://www.ycjw.zjut.edu.cn//stdgl/ksbm/Web_DJKCJ.aspx'
# cookies={cookie[0]['name']:cookie[0]['value'],cookie[1]['name']:cookie[1]['value']}
# print(cookies)
# r = requests.get(url, cookies=cookies)
# soup=BeautifulSoup(r.text, "html.parser")
# print(soup.find(id="Stdinfo1_lbl_stdinfo").string)

# pattern=re.compile(r'<span id="DJKCJ.*?>(.*?)<.*?id="DJKCJ.*?">(.*?)<.*?id="DJKCJ.*?">(.*?)<',re.S)
# results=re.findall(pattern, r.text)
# for item in results:
# 	print(item[0],item[1],item[2])
