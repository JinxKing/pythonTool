from selenium import webdriver # 导入webdriver包

import time

# driver = webdriver.Firefox() # 初始化一个火狐浏览器实例：driver
driver = webdriver.Chrome(r'C:\Users\L\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe')
# driver.get("http://www.ycjw.zjut.edu.cn/")
 

# driver.maximize_window() # 最大化浏览器 

# time.sleep(5) # 暂停5秒钟


driver.get("https://detail.tmall.com/item.htm?id=562505222389") # 通过get()方法，打开一个url站点