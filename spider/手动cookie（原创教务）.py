import requests
from bs4 import BeautifulSoup
import re

def login():
	# rqs=requests.get("http://www.ycjw.zjut.edu.cn//stdgl/cxxt/byshmx.aspx")
	url = 'http://www.ycjw.zjut.edu.cn//stdgl/ksbm/Web_DJKCJ.aspx'
	cookies = {"ASP.NET_SessionId":"2svc0crs4r2kpun3xxz3cw55","ASP.NET_SessionId_NS_Sig":"oenCV6mdm31m-lC_"}
	r = requests.get(url, cookies=cookies)
	soup=BeautifulSoup(r.text, "html.parser")
	print(soup.find(id="Stdinfo1_lbl_stdinfo").string)

	pattern=re.compile(r'<span id="DJKCJ.*?>(.*?)<.*?id="DJKCJ.*?">(.*?)<.*?id="DJKCJ.*?">(.*?)<',re.S)
	results=re.findall(pattern, r.text)
	for item in results:
		print(item[0],item[1],item[2])

login()