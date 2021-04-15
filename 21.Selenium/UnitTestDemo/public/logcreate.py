from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from public.login import Mylogin

class LogCreate(object):
    def __init__(self,driver):
        self.driver = driver

    def logcreate(self):
        Mylogin(self.driver).login()

        # 鼠标悬停
        element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.button-name')))
        ActionChains(self.driver).move_to_element(element).perform()

        # 点击日志
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.quick-add>div>p')))
        ActionChains(self.driver).click(click_element).perform()

        # 隐式等待10秒
        self.driver.implicitly_wait(10)

        # # 获取当前窗口句柄
        # handles = driver.current_window_handle
        # # 切换窗口
        # driver.switch_to.window(handles[1])

        # 点击第三个输入框，然后tab到最底部
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="form"]>div:nth-child(3)>div>textarea'))).send_keys("1")

        for i in range(0,8):
            ActionChains(self.driver).send_keys(Keys.TAB).perform()
            # sleep(2)


        # 模拟鼠标点击p标签
        cilck_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="add-file el-popover__reference"]')))
        ActionChains(self.driver).click(cilck_element).perform()

        # # 切换alert
        # driver.switch_to.alert