import User
import Album
import requests
import re
from multiprocessing import Pool

def search(page, key):
    url = "http://nian.so/search_user.php"
    data = {"page": page, "key": key}
    contents = requests.post(url, data=data)
    return contents.text.encode(contents.encoding).decode('utf-8')


def search_all(key):
    hasNext = True
    n = 1
    while hasNext:
        contents = search(n, key)
        n += 1
        pattern = re.compile(r'<div id="seupage."><img src="http://img.nian.so/images/wait.gif"></div>', re.S)
        result = re.search(pattern, contents)
        if not result:
            hasNext = False
        else:
            hasNext = True
        pattern = re.compile(r'<a href="#!/user/(.*?)".*?class="fo_user".*?>(.*?)</a>', re.S)
        results = re.findall(pattern, contents)
        if not results:
            print("找不到有「" + key + "」的用户..")
            return False
        else:
            for item in results:
                print(item[0], item[1])
def crawlProcess(id,name):
    print(name+id)
    album = Album.Album(name,id)
    album.saveAllImgs()





if __name__ == '__main__':
    keyword=input("***请输入用户名查找相关Id.."+"\n")
    search_all(keyword)
    Uid=input("***请输入你想get照片的用户id.."+"\n")
    user = User.User(Uid)
    Albums = user.getAlbums()
    print("开始存储..")
    pool = Pool()
    pool.starmap(crawlProcess, Albums)
    pool.close()
    pool.join()
    print("存储完成..")
