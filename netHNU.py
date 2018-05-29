import requests
import time

def connect(user):
    print(time.asctime(time.localtime(time.time())))
    data = {'ac_id': '1', 'action': 'login', 'ajax': '1',
            'password': user['pwd'], 'save_me': '1', 'username': user['usr']}
    response = requests.post(
        "http://10.62.65.185/include/auth_action.php", data=data)
    if(-1 != response.text.find('login_ok')):
        print('登录成功！')
        return 1
    time.sleep(11)
    connect(user)


def net_dect():
    try:
        requests.get('https://www.baidu.com/')
    except:
        print('网络异常,准备重连...')
        return 500
    return 200


if __name__ == '__main__':
    GL = {'usr': 'S1710W0778', 'pwd': '{B}NzM3OTY5NWc='}
    ZTY = {'usr': 'S171000923', 'pwd': '{B}dGlhbnl1bjEyMzEyMw=='}
    Now = ZTY

    while (1):
        if(500 == net_dect()):
            connect(Now)
        else:
            time.sleep(60*15)
