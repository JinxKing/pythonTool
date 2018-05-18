import requests
import time
import random
import agentConfig

def get_proxy(aip):
    """构建格式化的单个proxies"""
    proxy_ip = 'http://' + aip
    proxy_ips = 'https://' + aip
    proxy = {'https': proxy_ips, 'http': proxy_ip}
    return proxy

ip_list = [
    "1.119.193.36:8080",
    "27.190.25.218:8118",
    "183.159.93.55:18118",
    "125.127.134.108:61234",
    "101.27.22.3:61234",
    "1.196.203.5:808",
    "101.81.141.175:9999",
    "183.159.92.54:18118",
    "123.56.89.238:60443",
    "183.159.87.254:18118",
    "183.159.91.46:18118",
    "1.25.144.25:61234",
    "183.159.85.43:18118",
    "223.241.118.74:18118",
    "60.177.230.70:18118",
    "175.14.3.196:808",
    "183.128.35.137:18118",
    "49.79.193.180:61234",
    "183.159.80.242:18118",
    "27.28.232.31:61234",
    "49.79.195.227:61234",
    "223.241.118.74:18118",
    "183.128.35.137:18118",
    "175.14.3.196:808",
    "101.81.141.175:9999",
    "183.159.80.242:18118",
    "203.174.112.13:3128",
    "1.119.193.36:8080",
    "183.159.87.110:18118",
    "183.159.90.120:18118",
    "60.177.224.172:18118",
    "121.62.57.148:61234",
]

for i in range(500):
    try:
        UA = random.choice(agentConfig.user_agent_list)
        headers = {'User-Agent': UA}
        ip = random.choice(ip_list)
        proxies = get_proxy(ip)
        response = requests.get("http://www.lsqingfeng.com/wap/ldqc/vote.php?act=soso",headers=headers, proxies=proxies)
        time.sleep(2)
        cookies = {"PHPSESSID":response.cookies["PHPSESSID"]}
        requests.get("http://www.lsqingfeng.com/wap/ldqc/vote.php?act=getvote&number=LDQQGZ17049",cookies=cookies, headers=headers, proxies=proxies)
        time.sleep(4)
        resp = requests.get("http://www.lsqingfeng.com/wap/ldqc/vote.php?act=getvote&number=LDQQGZ17049",cookies=cookies, headers=headers, proxies=proxies)
        print(ip)
        print(resp.text)##1743
    except:
        print('time out')
