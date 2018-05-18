#!/usr/bin/env python  
#coding=utf-8  
import os
import subprocess

def canConnect():
        fnull = open(os.devnull, 'w')
        result = subprocess.call('ping www.baidu.com', shell = True, stdout = fnull, stderr = fnull)
        fnull.close()
        if result:
            return False
        else:
            return True

print(canConnect())