import requests 
import random
import agentConfig
from bs4 import BeautifulSoup
import telnetlib
import time

url = 'http://www.xicidaili.com/wt'
def get_ip_list(url=url):
    # UA=random.choice(agentConfig.user_agent_list)
    headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3"}
    ip_list = []
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, "html5lib")
    # ul_list = soup.find_all('tr', limit=20)
    ul_list = soup.find_all('tr')
    # print(len(ul_list))
    for i in range(2, len(ul_list)):
        line = ul_list[i].find_all('td')
        ip = line[1].text
        port = line[2].text
        address = ip + ':' + port
        ip_list.append(address)
    return ip_list

def get_proxy(aip):
    """构建格式化的单个proxies"""
    proxy_ip = 'http://' + aip
    proxy_ips = 'https://' + aip
    proxy = {'https': proxy_ips, 'http': proxy_ip}
    return proxy

def checkIP(ip_list):
    for ip in ip_list:
        hd, port = ip.split(':')
        try:
            telnetlib.Telnet(hd, port=port, timeout=20)
            UA=random.choice(agentConfig.user_agent_list)
            headers = {'User-Agent': UA,'Content-Type':'application/x-www-form-urlencoded'}
            proxies = get_proxy(ip)
            response = requests.get("http://www.lsqingfeng.com/wap/ldqc/vote.php?act=soso", headers=headers, proxies=proxies)
            cookies = {"PHPSESSID":response.cookies["PHPSESSID"]}
            # time.sleep(1)
            requests.get("http://www.lsqingfeng.com/wap/ldqc/vote.php?act=getvote&number=LDQQGZ17049", headers=headers, proxies=proxies, cookies=cookies)
            # time.sleep(2)
            resp = requests.get("http://www.lsqingfeng.com/wap/ldqc/vote.php?act=getvote&number=LDQQGZ17049", headers=headers, proxies=proxies, cookies=cookies)
            print(time.asctime(time.localtime(time.time())))
            print(ip)
            print(resp.text)
        except:
            ('vote失败')


for i in range(50):
    checkIP(get_ip_list())