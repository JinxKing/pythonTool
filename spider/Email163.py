#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

class Email:

    def __init__(self,reacher):
        self.sender='15700084566@163.com'    # 发件人邮箱账号
        self.passwd = '7379695g'              # 发件人邮箱SMTP授权码
        self.reacher=reacher

    def sendText(self,Subject,Text):
        ret=True
        try:
            msg=MIMEText(Text,'plain','utf-8')
            msg['From']=formataddr(["Python脚本",self.sender])  # 发件人邮箱昵称、发件人邮箱账号
            msg['To']=formataddr(["收件人昵称",self.reacher])              # 收件人邮箱昵称、收件人邮箱账号
            msg['Subject']=Subject               # 邮件的主题，也可以说是标题

            server=smtplib.SMTP_SSL("smtp.163.com")  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(self.sender,self.passwd)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.sender,[self.reacher,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret=False
        if ret:
            print("邮件发送成功")
        else:
            print("邮件发送失败")