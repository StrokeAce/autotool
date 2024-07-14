# 微信发消息自动化

import time
from pywinauto.application import Application
from pywinauto.keyboard import send_keys

class SendToWechat:
    # def __init__(self, TaskProcessor):

    def send_txt(self, user_name, message):
        # 打开微信
        app = Application(backend="uia").start(r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")
        time.sleep(1)

        send_keys('^f')
        send_keys(user_name)
        time.sleep(1)
        send_keys('{ENTER}')

        # 需要发送的消息内容
        message =(message)
        time.sleep(1)

        # 输入聊天内容
        send_keys(message)

        # 回车发送消息
        send_keys('{ENTER}') 


