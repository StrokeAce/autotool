from send_to_wechat import SendToWechat
from general_operation import GeneralOperation
from zombie import Zombie

def main():
    # send = SendToWechat()
    # send.send_txt("一鹿上有你", "自动消息：你好啊")
    # gen = GeneralOperation()
    # gen.operate_postman()

    zo = Zombie()
    zo.start()

if __name__ == '__main__':
    main()