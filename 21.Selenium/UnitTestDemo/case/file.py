from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from random import randint

import os
import unittest
import time

from public.login import Mylogin

content = "这是我创建的一条工作遇到问题日志内容，我的名称为mengxun"

class UpFile(unittest.TestCase):

    def setUp(self):
        # Firefox Headless模式
        # firefox_options = webdriver.FirefoxOptions()
        # firefox_options.add_argument('--headless')
        # self.driver = webdriver.Firefox(firefox_options=firefox_options)
        # self.driver.get('http://101.133.169.100:8088/index.html#/workbench/index')

        # Chrome Headless
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get('http://101.133.169.100:8088/index.html#/workbench/index')

        # self.driver = webdriver.Chrome()
        # self.driver.get('http://101.133.169.100:8088/index.html#/workbench/index')
        
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        print("StartTime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))

    def tearDown(self):
        filedir = "D:/test/screenshot/file/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/','test','screenshot','file'))
        print("EndTime:" + time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()

    def testUpfile01_01(self):
        """
        写日志，并上传文件
        """

        Mylogin(self.driver).login()

        # 鼠标悬停
        element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.button-name')))
        ActionChains(self.driver).move_to_element(element).perform()
        # 点击日志
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.quick-add>div>p')))
        ActionChains(self.driver).click(click_element).perform()
        # 隐式等待10秒
        self.driver.implicitly_wait(10)
        # 点击第三个输入框，然后tab到最底部
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="form"]>div:nth-child(3)>div>textarea'))).send_keys(content)
        # ActionChains(driver).click(cilck_element).perform()

        for i in range(0,8):
            ActionChains(self.driver).send_keys(Keys.TAB).perform()
            # sleep(2)

        file_ele = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div/div/div[2]/div[2]/div[4]/p/div/div/input')))
        # 上传本地图片
        file_ele.send_keys(r"C:\Users\quanxh\Desktop\goutou.png")

        # 点击提交
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div/div/div[3]/button[1]'))).click()

        # 返回用例执行完成时间，通过时间戳比对时间
        return time.time()

    def testUpfile01_02(self):
        """
        检查日志和上传的文件
        """
        Mylogin(self.driver).login()

        # 获取文件名称
        filename = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="cell-body"]>span'))).text
        # 断言结果
        self.assertEqual('goutou.png',filename)
        # 获取日志信息
        logContent = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="text"]>p:nth-child(1)'))).text
        logContent = logContent.split('：',1)[1]
        # 断言结果
        self.assertEqual(content,logContent)

        # 获取创建时间，调用testUpfile01_01返回的时间戳，和新日志对比。
        time_1 = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="journal-cell0"]/div[1]/div[1]/div[2]/span'))).text

        # 格式化时间转时间戳
        def get_timestamp_from_formattime(format_time):
            struct_time = time.strptime(format_time, '%Y-%m-%d %H:%M')
            return time.mktime(struct_time)

        # 时间戳比较
        def compare_time(time_1, time_2):
            if time_1 and time_2:
                time_stamp_1 = time.mktime(time.strptime(time_1, '%Y-%m-%d %H:%M'))
                time_stamp_2 = time.mktime(time.strptime(time_2, '%Y-%m-%d %H:%M'))
                if int(time_stamp_1) == int(time_stamp_2):
                    return True
                else:
                    return False
                
        get_timestamp_from_formattime(time_1)
        time_2 = UpFile().testUpfile01_01()

        # 断言结果
        self.assertTrue(compare_time(time_1, time_2))