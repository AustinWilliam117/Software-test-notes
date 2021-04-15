"""
创建一个登录模块
"""

from time import sleep,ctime

class Mylogin(object):
    def __init__(self,driver):
        self.driver = driver

    def login(self):
        self.driver.find_element_by_name('username').send_keys('17610832710')
        self.driver.find_element_by_name('password').send_keys('123456')
        self.driver.find_element_by_xpath('//button[@type="button"]').click()
