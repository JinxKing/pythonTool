import jieba
import re
f=open("test.txt","r")
content=f.read()
content=re.sub(re.compile('\n+'),"",content)
# content=content.replace("，","")
# content=content.replace("。","")
# print(content)

seg_list = jieba.cut(content, cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式
# for item in seg_list:
#     print(item)