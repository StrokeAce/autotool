# 实现一些小的通用操作

from pywinauto.application import Application
import pyautogui, os, cv2
import numpy as np 

class GeneralOperation:
    # 打开微信
    def open_app(self):
        self.app = Application(backend="uia").start(r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")

    # 点击按钮
    def click_button(self, button_image):
        # 截取全屏  
        screenshot = pyautogui.screenshot()
        print("current folder:", os.getcwd()) 
        # 加载图像  
        image = cv2.imread(button_image, 0)  # 0 表示以灰度模式读取  
        w, h = image.shape[::-1]

        # 将 PIL 图像转换为 NumPy 数组  
        screenshot_array = np.array(screenshot)
        
        # 将截图转换为灰度图像  
        gray = cv2.cvtColor(screenshot_array, cv2.COLOR_BGR2GRAY)  
        
        # 使用模板匹配  
        res = cv2.matchTemplate(gray, image, cv2.TM_CCOEFF_NORMED)  
        threshold = 0.8  # 你可以调整这个阈值  
        loc = np.where(res >= threshold)  
        
        # 在截图中标记所有匹配项  
        for pt in zip(*loc[::-1]):  
            cv2.rectangle(screenshot_array, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)  

        if loc[0].size > 0:  
            # 获取第一个匹配项的位置（注意：这里需要调整坐标以匹配pyautogui的期望）  
            x, y = loc[1][0], loc[0][0]  
            
            # 考虑模板的宽度和高度来更精确地定位点击位置  
            click_x, click_y = x + w // 2, y + h // 2  
            
            # 模拟点击  
            pyautogui.click(click_x, click_y)

    # 检查某个图标是否存在
    def check_image(self, button_image):
        # 截取全屏  
        screenshot = pyautogui.screenshot()

        # 加载图像  
        image = cv2.imread(button_image, 0)  # 0 表示以灰度模式读取  
        w, h = image.shape[::-1]

        # 将 PIL 图像转换为 NumPy 数组  
        screenshot_array = np.array(screenshot)
        
        # 将截图转换为灰度图像  
        gray = cv2.cvtColor(screenshot_array, cv2.COLOR_BGR2GRAY)  
        
        # 使用模板匹配  
        res = cv2.matchTemplate(gray, image, cv2.TM_CCOEFF_NORMED)  
        threshold = 0.8  # 你可以调整这个阈值  
        loc = np.where(res >= threshold)  
        
        # 在截图中标记所有匹配项  
        for pt in zip(*loc[::-1]):  
            cv2.rectangle(screenshot_array, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)  

        if loc[0].size > 0:
            return True
        
        return False
    
    # 检查图标列表，返回存在的
    def check_image_list(self, image_list):
        # 截取全屏  
        screenshot = pyautogui.screenshot()

        # 将 PIL 图像转换为 NumPy 数组  
        screenshot_array = np.array(screenshot)
        
        # 将截图转换为灰度图像  
        gray = cv2.cvtColor(screenshot_array, cv2.COLOR_BGR2GRAY) 

        check_list = []

        for name,path in image_list.items():
              
            image = cv2.imread(path, 0)  # 0 表示以灰度模式读取  
            w, h = image.shape[::-1]
        
            # 使用模板匹配  
            res = cv2.matchTemplate(gray, image, cv2.TM_CCOEFF_NORMED)  
            threshold = 0.8  # 你可以调整这个阈值  
            loc = np.where(res >= threshold)  
            
            # 在截图中标记所有匹配项  
            for pt in zip(*loc[::-1]):  
                cv2.rectangle(screenshot_array, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)  

            if loc[0].size > 0:
                x, y = loc[1][0], loc[0][0]

                click_x, click_y = x + w // 2, y + h // 2  

                item_image = {}
                item_image[name] = [click_x, click_y]
                check_list.append(item_image)

        return check_list
            