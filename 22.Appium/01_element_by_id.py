import os
import unittest
import time
from appium import webdriver


class AndroidTests(unittest.TestCase):
    def setUp(self):
        # 定义一个空字典
        desired_caps = {}
        # 平台名称
        desired_caps['platformName'] = 'Android'
        # 平台版本（手机版本号）
        desired_caps['platformVersion'] = '5.1'
        # 设备名称固定写Android Emulator不会强行校验值
        desired_caps['deviceName'] = 'Android Emulator'
        # 不清除app数据，清除后犹如新设备安装的新软件
        desired_caps['noReset'] = 'True'
        # app包名，app之间用唯一的包名区分
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
        # 一个界面就是一个activity，app中每个界面通过activity区分
        desired_caps['appActivity'] = '.ui.base.SplashActivity'
        # 初始化driver，远程连接，请求参数到appium server上
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        #self.driver.quit()
        pass

    def test_element_by_id(self):
        self.driver.implicitly_wait(60)
        el = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
        print(el[2].text)
        el[2].click()



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)