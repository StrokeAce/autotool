# 微信小程序：向僵尸开炮

import time, pyautogui
from pywinauto.application import Application
from general_operation import GeneralOperation

class Zombie:
    def __init__(self):
        self.gen = GeneralOperation()
        self.imagelist = {"applet":"D:\\homework\\auto-tool-develop\\autotool\\data\\applet.png",
                          "zombie":"D:\\homework\\auto-tool-develop\\autotool\\data\\zombie\\zombie.png", 
                        }
        self.fightlist={"start_game":"D:\\homework\\auto-tool-develop\\autotool\\data\\zombie\\start_game.png",
                        "game_end":"D:\\homework\\auto-tool-develop\\autotool\\data\\zombie\\game_end.png",
                        "blank":"D:\\homework\\auto-tool-develop\\autotool\\data\\zombie\\blank.png",
                        "gun":"D:\\homework\\auto-tool-develop\\autotool\\data\\zombie\\gun.png",
                        "wind":"D:\\homework\\auto-tool-develop\\autotool\\data\\zombie\\wind.png",
                        "fire":"D:\\homework\\auto-tool-develop\\autotool\\data\\zombie\\fire.png",
                        "uav":"D:\\homework\\auto-tool-develop\\autotool\\data\\zombie\\uav.png",
                        "ray":"D:\\homework\\auto-tool-develop\\autotool\\data\\zombie\\ray.png",
                        "press":"D:\\homework\\auto-tool-develop\\autotool\\data\\zombie\\press.png",
                        "laser":"D:\\homework\\auto-tool-develop\\autotool\\data\\zombie\\laser.png",
                        "tank":"D:\\homework\\auto-tool-develop\\autotool\\data\\zombie\\tank.png",
                        "ice":"D:\\homework\\auto-tool-develop\\autotool\\data\\zombie\\ice.png",
                        "electric":"D:\\homework\\auto-tool-develop\\autotool\\data\\zombie\\electric.png"
                        }

    def start(self):
        
        self.gen.open_app()
        time.sleep(2)

        # 小程序入口
        self.gen.click_button(self.imagelist['applet'])
        time.sleep(5)

        # 向僵尸开炮入口
        self.gen.click_button(self.imagelist['zombie'])

        self.running()
    
    # 持续运行
    def running(self):
        waittime = 0
        while True:
            time.sleep(1) 
            
            self.control_fight()

    def control_fight(self):

        check_list = self.gen.check_image_list(self.fightlist)
        if check_list:
            if self.find_button(check_list, 'start_game'):
                self.click_button(check_list, 'start_game')
            elif self.find_button(check_list, 'game_end'):
                self.click_button(check_list, 'game_end')
            elif self.find_button(check_list, 'blank'):
                self.click_button(check_list, 'blank')
            elif self.find_button(check_list, 'gun'):
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

    def find_button(self, check_list, button):

        for item in check_list:
            if button in item:
                return True
        return False

    def click_button(self, check_list, button):

        for item in check_list:
            if button in item:
                pyautogui.click(item[button][0], item[button][1])