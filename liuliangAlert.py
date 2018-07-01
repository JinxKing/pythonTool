#!/usr/bin/python3
import Email163
import requests
import time
from bs4 import BeautifulSoup
import re

IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/liuliangAlert/with/key/Drm4rxJRpz4Gu96LSNRl-'
PAYLOAD = {'login_id': 'S1710W0778', 'password': 'a7379695','s_ticket': '2388', 'null': 'teacher'}
REACHER="462590148@qq.com"


def post_ifttt_webhook(data):
    # ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)
    response = requests.post(IFTTT_WEBHOOKS_URL, json=data)
    print(time.asctime(time.localtime(time.time()))+'\t'+response.text)

def check_liuliang():
	r = requests.post("http://its-diy.hnu.edu.cn/liuliang1/Default.aspx", data=PAYLOAD)
	soup = BeautifulSoup(r.text, "html.parser")
	resultStr = soup.find(id="Label14").string
	print(time.asctime(time.localtime(time.time()))+'\t'+resultStr)
	pattern = re.compile('本月下载流量：(.*?)GB',re.S)
	counts = re.findall(pattern,resultStr)
	return counts[0]


if __name__ == "__main__":
	while (1):
	    costLiuliang = check_liuliang()
	    if(float(costLiuliang)>19):
	    	data = {'value1': costLiuliang}
	    	post_ifttt_webhook(data)
	    	email=Email163.Email(REACHER)
	    	# params:title+content
	    	email.sendText("标题","内容")
	    	time.sleep(60*15)
	    	continue
	    if(float(costLiuliang)>18):
	    	data = {'value1': costLiuliang}
	    	post_ifttt_webhook(data)
	    	time.sleep(60*30)
	    	continue
	    time.sleep(60*60)
    