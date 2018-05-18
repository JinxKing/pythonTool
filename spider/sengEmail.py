#!/usr/bin/python3
import Email163

reacher="lguo@hnu.edu.cn"
email=Email163.Email(reacher)
email.sendText("标题","内容")