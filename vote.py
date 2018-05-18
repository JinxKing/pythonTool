import requests
import time
import random
# import json

for i in range(2000):
	response = requests.get("http://www.lsqingfeng.com/wap/ldqc/vote.php?act=soso")
	time.sleep(2)
	cookies = {"PHPSESSID":response.cookies["PHPSESSID"]}
	requests.get("http://www.lsqingfeng.com/wap/ldqc/vote.php?act=getvote&number=LDQQGZ17049",cookies=cookies)
	time.sleep(1)
	resp = requests.get("http://www.lsqingfeng.com/wap/ldqc/vote.php?act=getvote&number=LDQQGZ17049",cookies=cookies)
	print(time.asctime(time.localtime(time.time())))
	print(resp.text)##1743
	time.sleep(random.random()*10)