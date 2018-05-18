import requests
import re
from bs4 import BeautifulSoup

def getContents(url):
    print("新的一页")
    responses=requests.get(url)
    responses.encoding='gbk'
    soup=BeautifulSoup(responses.text,"html.parser")
    news=soup.find_all(attrs={'class':'uli14 pageList borderli-blue'})
    pattern = re.compile('<li><a href="(.*?)".*?>(.*?)<',re.S)
    results=re.findall(pattern,str(news))
    return results

def saveNews(url,title):
    initUrl='http://xfb.sh.gov.cn'
    url=initUrl+url.strip()
    response=requests.get(url)
    response.encoding='gbk'
    soup=BeautifulSoup(response.text,"html.parser")
    content=soup.find(id="ivs_content")
    content=str(content)
    content=re.sub(re.compile('\xa0'),"",content)
    content=re.sub(re.compile('<.*?>'),"",content)
    content=re.sub(re.compile('&ldquo;'),"",content)
    content=re.sub(re.compile('&rdquo;'),"",content)
    path="信访文档/"+title.strip()+".txt"
    try:
        f=open(path,"w+")
        f.write(content)
    except OSError:
        print("丢失一个文档")



if __name__=='__main__':
    for x in range(6,12):
        url='http://xfb.sh.gov.cn/xfb/xwzx/n15/index'+str(x)+'.html'
        items=getContents(url)
        for item in items:
            saveNews(item[0],item[1])
