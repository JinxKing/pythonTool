#!/usr/bin/python  
import requests

url=r"http://media1.ccxx99.com/remote_control.php?time=1506243807&cv=13dca1db926771ee4f23b0545b7008a5&lr=0&cv2=93058fcdd9cc60f91f8f1d31b5cf1275&file=/videos/13000/13291/13291.mp4&cv3=dd08f223cfdc8446ff1e29009133acb7";    
response = requests.get(url)
print(response);