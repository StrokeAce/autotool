# 微信小程序：向僵尸开炮

import time, pyautogui, datetime
from pywinauto.application import Application
from general_operation import GeneralOperation

class Zombie:
    def __init__(self):
        self.gen = GeneralOperation()
        self.imagelist = {"applet":"./data/applet.png",
                          "zombie":"./data/zombie/zombie.png", 
                        }
        self.fightlist={"start_game":"./data/zombie/start_game.png",
                        "game_end":"./data/zombie/game_end.png",                        
                        "gun":"./data/zombie/gun.png",
                        "wind":"./data/zombie/wind.png",
                        "fire":"./data/zombie/fire.png",
                        "uav":"./data/zombie/uav.png",
                        "ray":"./data/zombie/ray.png",
                        "press":"./data/zombie/press.png",
                        "laser":"./data/zombie/laser.png",
                        "tank":"./data/zombie/tank.png",
                        "ice":"./data/zombie/ice.png",
                        "plane":"./data/zombie/plane.png",
                        "electric":"./data/zombie/electric.png",
                        "snow":"./data/zombie/snow.png",
                        "knife":"./data/zombie/knife.png",
                        "jump":"./data/zombie/jump.png",
                        "reconnect":"./data/zombie/reconnect.png",
                        "receive":"./data/zombie/receive.png",
                        "blank":"./data/zombie/blank.png",
                        "blank2":"./data/zombie/blank2.png"
                        }

    def start(self):
        
        self.gen.open_app()
        time.sleep(2)

        # 小程序入口
        self.gen.click_button(self.imagelist['applet'])
        time.sleep(5)

        # 向僵尸开炮入口
        self.gen.click_button(self.imagelist['zombie'])
        time.sleep(8)

        self.running()
    
    # 持续运行
    def running(self):
        waittime = 0
        while True:
            time.sleep(1) 
            s_now = datetime.datetime.fromtimestamp(int(time.time()))
            # print("==start:", s_now)
            self.control_fight()
            s_now = datetime.datetime.fromtimestamp(int(time.time()))
            # print("==end:", s_now)

    def control_fight(self):

        check_list = self.gen.check_image_list(self.fightlist)
        if check_list:            
            if self.find_button(check_list, 'gun'):
                self.click_button(check_list, 'gun')
            elif self.find_button(check_list, 'wind'):
                self.click_button(check_list, 'wind')
            elif self.find_button(check_list, 'fire'):
                self.click_button(check_list, 'fire')
            elif self.find_button(check_list, 'uav'):
                self.click_button(check_list, 'uav')
            elif self.find_button(check_list, 'ray'):
                self.click_button(check_list, 'ray')
            elif self.find_button(check_list, 'press'):
                self.click_button(check_list, 'press')
            elif self.find_button(check_list, 'laser'):
                self.click_button(check_list, 'laser')
            elif self.find_button(check_list, 'tank'):
                self.click_button(check_list, 'tank')
            elif self.find_button(check_list, 'ice'):
                self.click_button(check_list, 'ice')
            elif self.find_button(check_list, 'electric'):
                self.click_button(check_list, 'electric')
            elif self.find_button(check_list, 'snow'):
                self.click_button(check_list, 'snow')            
            elif self.find_button(check_list, 'plane'):
                self.click_button(check_list, 'plane')
            elif self.find_button(check_list, 'knife'):
                self.click_button(check_list, 'knife')
            elif self.find_button(check_list, 'jump'):
                self.click_button(check_list, 'jump')
            elif self.find_button(check_list, 'blank'):
                self.click_button(check_list, 'blank')            
            elif self.find_button(check_list, 'start_game'):
                self.click_button(check_list, 'start_game')
            elif self.find_button(check_list, 'game_end'):
                self.click_button(check_list, 'game_end')
            elif self.find_button(check_list, 'blank2'):
                self.click_button(check_list, 'blank2')
            elif self.find_button(check_list, 'reconnect'):
                self.click_button(check_list, 'reconnect')
            elif self.find_button(check_list, 'receive'):
                self.click_button(check_list, 'receive')

    def find_button(self, check_list, button):

        for item in check_list:
            if button in item:
                return True
        return False

    def click_button(self, check_list, button):

        for item in check_list:
            if button in item:
                pyautogui.click(item[button][0], item[button][1])