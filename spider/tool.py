import re
 
#处理页面标签类
class Tool:
    #去除img标签,1-7位空格, 
    removeImg = re.compile('<img.*?>| {1,7}| ')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')#出除标签仅保留内容
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    removeSpace = re.compile('&nbsp;')
    #将多行空行删除
    removeNoneLine = re.compile('\n+')

    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        x = re.sub(self.removeSpace,"",x)#替换后生成空行
        x = re.sub(self.removeNoneLine,"\n",x)#务必最后删空行
        #strip()将前后多余内容删除
        return x.strip()
