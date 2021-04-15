# coding=utf-8
from selenium import webdriver
from public.login import Mylogin
import unittest
import os
import time

class TestShouye(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://101.133.169.100/yuns/index.php")
        self.driver.maximize_window()
        time.sleep(5)
        print("starttime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))

    def tearDown(self):
        filedir = "D:/test/screenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/', 'test', 'screenshot'))
        print("endTime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()


    def testShouye01_01(self):
        '''测试首页导航文案显示是否正常'''
        Mylogin(self.driver).login()
        firstPageNavi = self.driver.find_element_by_xpath("//div[@class='top']/span")
        loginText = self.driver.find_element_by_css_selector("div.login>a:nth-child(1)")
        regisText = self.driver.find_element_by_css_selector("div.login>a:nth-child(3)")

        self.assertEqual("亲，欢迎您来到云商系统商城！",firstPageNavi.text)
        self.assertEqual("17731990979", loginText.text)
        self.assertEqual("退出", regisText.text)
        self.assertNotEqual("dd", regisText.text)

        self.assertIn("云商系统商城",firstPageNavi.text)

        self.assertTrue(self.driver.find_element_by_xpath("//div[@class='top']/span").is_displayed())
        self.assertFalse(firstPageNavi.is_displayed())

        if loginText.text == "177****0979":
            print("等于")
        else:
            print("不等于")
            self.driver.find_element_by_xpath("王麻子")



    def testShouye01_02(self):
        '''验证搜索内容无时，提示语是否正常'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[1]").send_keys("王麻子")
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[2]").click()
        time.sleep(2)
        searchText = self.driver.find_element_by_xpath("//div[@class='nomsg']")
        self.assertEqual(searchText.text, "抱歉，没有找到相关的商品")



if __name__ == "__main__":
    unittest.main()


