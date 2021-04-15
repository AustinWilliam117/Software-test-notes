from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import os
import unittest
import time

class TestLogin(unittest.TestCase):
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
        # self.driver.get('http://101.133.169.100:8088/index.html#/login?redirect=%2F404')
        
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        print("StartTime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))

    def tearDown(self):
        filedir = "D:/test/screenshot/login/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/','test','screenshot','login'))
        print("EndTime:" + time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()

    def testLogin01_01(self):
        """
        输入正确账号密码后正常登录
        """
        # 输入账号
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.NAME,'username'))).send_keys('17610832710')
        # 输入密码
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.NAME,'password'))).send_keys('123456')
        # 点击登录
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//button[@type="button"]'))).click()
        time.sleep(5)
        url = self.driver.current_url
        # 断言结果，判断页面url是否为http://101.133.169.100:8088/index.html#/workbench/index
        self.assertEqual("http://101.133.169.100:8088/index.html#/workbench/index",url)
        # 点击首页小箭头
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/section/header/div/span[2]/div[2]/i')))
        ActionChains(self.driver).click(click_element).perform()
        # 点击个人中心个人中心
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="handel-items"]>div>i')))
        ActionChains(self.driver).click(click_element).perform()
        # 获取手机号
        phone = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="section"]>div:nth-child(2)>div:nth-child(3)>div>div:last-child'))).text
        # 断言手机号是否一致
        self.assertEqual("17610832710",phone)
        # 获取姓名
        name = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="section"]>div:nth-child(2)>div>div>div:last-child'))).text
        # 断言姓名是否一致
        self.assertEqual("mengxun",name)

    def testLogin01_02(self):
        """
        验证不输入账号，是否出现提示信息
        """
        # 点击登录按钮
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[type="button"]'))).click()
        # 等待2秒，不然取不到值，我也不知道为什么就取不到。不都显示等待了吗？
        time.sleep(2)
        # 获取账号提示信息
        account_tip = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="el-form-item__error"]'))).text
        # 断言结果
        self.assertEqual("请输入账号",account_tip)

    def testLogin01_03(self):
        """
        验证不输入密码，是否出现提示信息
        """
        # 点击登录按钮
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[type="button"]'))).click()
        # 等待2秒，不然取不到值，我也不知道为什么就取不到。不都显示等待了吗？
        time.sleep(2)
        # 获取密码提示信息
        passwd_tip = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#app>div>div.right>form>div:nth-child(3)>div>div.el-form-item__error'))).text
        # 断言结果
        self.assertEqual('密码不能小于5位',passwd_tip)

    def testLogin01_04(self):
        """
        输入密码小于5位，提示密码不能小于5位
        """
        # 输入账号
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.NAME,'username'))).send_keys('17610832710')
        # 输入密码
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.NAME,'password'))).send_keys('123')
        # 点击登录
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//button[@type="button"]'))).click()
        # 等待2秒，不然取不到值，我也不知道为什么就取不到。不都显示等待了吗？
        time.sleep(2)
        # 获取密码提示信息
        passwd_tip = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#app>div>div.right>form>div:nth-child(3)>div>div.el-form-item__error'))).text
        # 断言结果
        self.assertEqual('密码不能小于5位',passwd_tip)

"""
偶然测试发现账号输入3次也能登录
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep,ctime

driver = webdriver.Chrome()
driver.get('http://101.133.169.100:8088/index.html#/workbench/index')

sleep(2)

driver.find_element_by_name('username').send_keys('17610832710')
driver.find_element_by_name('password').send_keys('123456')
driver.find_element_by_xpath('//button[@type="button"]').click()

driver.maximize_window()
# 输入账号
WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.NAME,'username'))).send_keys('17610832710')
# 输入密码
WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.NAME,'password'))).send_keys('123456')
# 点击登录
WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//button[@type="button"]'))).click()
# 点击首页小箭头
WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="el-icon-caret-bottom mark"]'))).click()
# 点击个人中心个人中心
WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="handel-items"]>div>i'))).click()
# 查看手机号是否一致
phone = WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="section"]>div:nth-child(2)>div:nth-child(3)>div>div:last-child'))).text
# 获取姓名
name = WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="section"]>div:nth-child(2)>div>div>div:last-child'))).text

print(name,phone)
"""