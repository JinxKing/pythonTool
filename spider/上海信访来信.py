import requests
import re
from multiprocessing import Pool

def getPage(page):
    print("获取第"+page+"页")
    url='http://wsxf.sh.gov.cn/xf_swldxx/areaSearch/hfxdAll.aspx?nav=&pageindex='+str(page)
    response=requests.get(url)
    pattern =re.compile('<a onclick=\'window.open.*?index.html.(.*?)".*?title=\'(.*?)\'',re.S)
    results=re.findall(pattern,str(response.text))
    return results

def saveNews(url,title):
    url='http://wsxf.sh.gov.cn/xf_swldxx/areaSearch/hfxd_info.aspx?'+url
    response=requests.get(url)
    pattern=re.compile('<span id="LaDisposition".*?>(.*?)</span>',re.S)
    result=re.search(pattern,response.text)
    content=result.group(1)
    content=re.sub(re.compile('<.*?>'),"",content)
    path="信访文档/"+title.strip()+"（回复）.txt"
    try:
        f=open(path,"w+")
        f.write(content)
    except OSError:
        print("丢失一个文档")
def getTxt(i):
    items=getPage(str(i))
    for item in items:
        saveNews(item[0],item[1])

if __name__=='__main__':
    pool=Pool()
    for i in range(1000,1150):
        pool.apply_async(getTxt, (i,))
    pool.close()
    pool.join()

