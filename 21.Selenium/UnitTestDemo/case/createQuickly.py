from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import os
import unittest
import time

from public.login import Mylogin

todayLog = "这是我创建的一条今日工作日志内容，我的名称为mengxun"
tomorrowLog = "这是我创建的一条明日工作日志内容，我的名称为mengxun"
errorLog = "这是我创建的一条工作遇到问题日志内容，我的名称为mengxun"
username = "mengxun"

class TestCreateQuickly(unittest.TestCase):
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
        filedir = "D:/test/screenshot/cquick"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/','test','screenshot','cquick'))
        print("EndTime:" + time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()

    def testCreateQuickly01_01(self):
        """
        点击快速创建，创建日志
        """
        Mylogin(self.driver).login()

        # 鼠标悬停
        element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.button-name')))
        ActionChains(self.driver).move_to_element(element).perform()
        # 点击日志
        click_element = WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.quick-add>div>p')))
        ActionChains(self.driver).click(click_element).perform()
        # 隐式等待10秒
        self.driver.implicitly_wait(10)

        # FIREFOX需要获取当前窗口句柄
        # handles = self.driver.current_window_handle
        # 关闭当前窗口
        # driver.close()
        # 切换窗口
        # self.driver.switch_to.window(handles[1])

        # 尝试在今日工作内容书写信息，不成功返回信息
        try:
            WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="form"]>div:nth-child(1)>div>textarea'))).send_keys(todayLog)
            WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="form"]>div:nth-child(2)>div>textarea'))).send_keys(tomorrowLog)
            WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="form"]>div:nth-child(3)>div>textarea'))).send_keys(errorLog)
        except:
            print('selenium.common.exceptions.NoSuchWindowException: Message: Unable to locate window: 8')

        # 点击提交
        self.driver.find_element_by_css_selector('[class="btn-group"]>button').click()
        """
        # 获取首页第一篇日志信息
        userName = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="journal-cell0"]/div[1]/div[1]/div[2]/p[1]/span[1]'))).text
        userContent = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="journal-cell0"]/div[1]/div[2]/p/text()')))
        # 断言结果
        self.assertEqual('mengxun',userName)
        self.assertEqual('这是我创建的一条日志内容，我的名称为mengxun',userContent)
        """

    def testCreateQuickly01_02(self):

        Mylogin(self.driver).login()
        # 获取首页第一篇日志信息
        userName = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="journal-cell0"]/div[1]/div[1]/div[2]/p[1]/span[1]'))).text
        userContent = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="journal-cell0"]/div[1]/div[2]/p[1]'))).text
        userContent = userContent.split('：',1)[1]
        # 断言结果
        self.assertEqual(username,userName)
        self.assertEqual(todayLog,userContent)

    def testCreateQuickly01_03(self):

        Mylogin(self.driver).login()
        # 获取首页第一篇日志信息
        userName = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="journal-cell0"]/div[1]/div[1]/div[2]/p[1]/span[1]'))).text
        userContent = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="journal-cell0"]/div[1]/div[2]/p[2]'))).text
        userContent = userContent.split('：',1)[1]
        # 断言结果
        self.assertEqual(username,userName)
        self.assertEqual(tomorrowLog,userContent)

    def testCreateQuickly01_04(self):

        Mylogin(self.driver).login()
        # 获取首页第一篇日志信息
        userName = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="journal-cell0"]/div[1]/div[1]/div[2]/p[1]/span[1]'))).text
        userContent = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="journal-cell0"]/div[1]/div[2]/p[3]'))).text
        userContent = userContent.split('：',1)[1]
        # 断言结果
        self.assertEqual(username,userName)
        self.assertEqual(errorLog,userContent)

if __name__ == "__main__":
    unittest.main()