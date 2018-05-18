import os
import pymysql

def getTitle(rootdir):
    for parent,dirnames,filenames  in os.walk(rootdir):
        titles=[]
        for filename in filenames:
            titles.append(filename.replace(".txt",""))
    return titles

def getTXT(title):
    path = "信访文档/" + title + ".txt"
    if os.path.exists(path):
        f = open(path, "r")
        content = f.read().strip()
        path = "回复/" + title + "（回复）.txt"
        if os.path.exists(path):
            f = open(path, "r")
            content += f.read().strip()
        else:
            print("回复缺失"+title)
    else:
        content=""
        print("文档丢失"+title)
    return content

if __name__=='__main__':
    rootdir = "F:\Programing\Python\信访文档"
    db=pymysql.connect("119.29.185.127","gjz","gjz509","bm",charset="utf8")
    items=getTitle(rootdir)
    for item in items:#item为标题
        content=getTXT(item)
        cursor = db.cursor()
        sql ="INSERT INTO t_document (title,content,isPetitionField) VALUES('%s','%s','1')"%(item,content)
        try:
            cursor.execute(sql)  # 执行sql语句
            db.commit()
        except:  # 发生错误时回滚
            print("fail"+item)
            db.rollback()
    db.close()
