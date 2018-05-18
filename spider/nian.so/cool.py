import requests
import re

def getContents():
    url="http://nian.so/about.php"
    responses=requests.get(url)
    responses=responses.text.encode(responses.encoding).decode('utf-8')
    pattern = re.compile('<div class="album_inner">.*?href="#!/dream/(.*?)".*?href="#!/user/(.*?)"',re.S)
    results=re.findall(pattern,responses)
    return results

if __name__=='__main__':
    items=getContents()
    for item in items:
        print(item[0]+"\t"+item[1])
