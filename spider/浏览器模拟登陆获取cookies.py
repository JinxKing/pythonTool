# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import requests
from bs4 import BeautifulSoup
import re

driver = webdriver.Chrome(r'C:\Users\L\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe')
driver.get("http://www.ycjw.zjut.edu.cn/")
# assert "百度" in driver.title
select = Select(driver.find_element_by_name('Cbo_LX'))
select.select_by_index(2)

elem2 = driver.find_element_by_name("Txt_UserName")
elem2.send_keys("201307260205")
elem3 = driver.find_element_by_name("Txt_Password")
elem3.send_keys("7379695")

elem3.send_keys(Keys.RETURN)
# print (driver.page_source)

cookie= driver.get_cookies()#返回list（包含多个字典，每个cookie单独为个字典包括name和value）
# print(cookie)
#输出#[{'domain': 'www.ycjw.zjut.edu.cn', 'httpOnly': True, 'name': 'ASP.NET_SessionId', 'path': '/', 'secure': False, 'value': 'diq2fmidydgh12552lzdjp55'}, {'domain': 'www.ycjw.zjut.edu.cn', 'httpOnly': True, 'name': 'ASP.NET_SessionId_NS_Sig', 'path': '/', 'secure': False, 'value': 'oenCV6mdzWdh_VC_'}]
# print(cookie[0]['value']+"\t"+cookie[1]['value'])

url = 'http://www.ycjw.zjut.edu.cn//stdgl/ksbm/Web_DJKCJ.aspx'
cookies={cookie[0]['name']:cookie[0]['value'],cookie[1]['name']:cookie[1]['value']}
print(cookies)
r = requests.get(url, cookies=cookies)
soup=BeautifulSoup(r.text, "html.parser")
print(soup.find(id="Stdinfo1_lbl_stdinfo").string)

pattern=re.compile(r'<span id="DJKCJ.*?>(.*?)<.*?id="DJKCJ.*?">(.*?)<.*?id="DJKCJ.*?">(.*?)<',re.S)
results=re.findall(pattern, r.text)
for item in results:
	print(item[0],item[1],item[2])
