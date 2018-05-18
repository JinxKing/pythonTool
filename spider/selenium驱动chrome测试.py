# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r'C:\Users\L\AppData\Local\Google\Chrome\Application\chromedriver.exe')
driver.get("https://www.baidu.com/")
assert "百度" in driver.title
elem = driver.find_element_by_name("wd")
elem.send_keys("pycon")

elem.send_keys(Keys.RETURN)

print (driver.page_source)#此处返回js动态显示html代码，即“网页渲染后的源代码”