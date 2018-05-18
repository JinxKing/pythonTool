# import requests 
# #假设此时有一已经格式化好的ip代理地址proxies
# proxies = {
#     "http": 'http://60.177.227.205:18118',
#     "https": 'https://60.177.227.205:18118',
# }
# # headers = {
# #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
# # }
# url = 'http://www.whatismyip.com.tw/'
# # try:
# page = requests.get(url, proxies=proxies)
# # except:
# #         print('失败')
# # else:
# #         print('成功')

import telnetlib

ip ='111.225.100.60:9999'
hd, port = ip.split(':')
try:
	telnetlib.Telnet(hd, port=port, timeout=20)
except:
    print( '失败')
else:
    print ('成功')