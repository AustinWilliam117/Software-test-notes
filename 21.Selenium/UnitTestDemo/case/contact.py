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
from public.logcreate import LogCreate
from public.phone import create_phone

# 客户姓名，客户电话
username = "蒙珣"+str(randint(0,100000))
phone = create_phone()

# 客户职业，客户来源，客户级别
profession = randint(1,8)
source = randint(1,10)
level = randint(1,3)

# 合同id，随机生成10位数。后续可升级位随机10位，且不重复
contract_id = str(randint(0, 99999999)).zfill(10)

# 合同名称
contract_name = "天地大同"+str(randint(0,100000))

class TestContact(unittest.TestCase):
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
        filedir = "D:/test/screenshot/contact/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/','test','screenshot','contact'))
        print("EndTime:" + time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()

    def testCreateContact01_01(self):
        """
        新建客户
        """
        LogCreate(self.driver).logcreate()

        # 点击“新建”
        cilck_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div[2]/div[2]/div/div/button')))
        ActionChains(self.driver).click(cilck_element).perform()

        try:
            time.sleep(2)
            # 切换alert
            alertInfo = self.driver.switch_to.alert
            # 驳回警告信息
            alertInfo.dismiss()
        except:
            pass

        # 填写客户名称，随机生成手机号 (尝试使用循环)     
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="el-form crm-create-box el-form--label-top"]>div:nth-child(1)>div>div>input'))).send_keys(username)
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="el-form crm-create-box el-form--label-top"]>div:nth-child(2)>div>div>input'))).send_keys(phone)

        """
        非select的ul下拉框
        使用随机数生成
        """
        # 选择客户行业
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="el-form crm-create-box el-form--label-top"]>div:nth-child(5)>div>div>div>input')))
        ActionChains(self.driver).click(click_element).perform()

        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'html>body>div:last-child>div>div>ul>li:nth-child(%d)'%profession)))
        ActionChains(self.driver).click(click_element).perform()

        # 点击选择客户来源
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body>div:nth-child(10)>div>div>div>div>div>div>div>div>form>div:nth-child(4)>div>div>div>input')))
        ActionChains(self.driver).click(click_element).perform()
       
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body>div:nth-child(12)>div.el-scrollbar>div.el-select-dropdown__wrap.el-scrollbar__wrap>ul>li:nth-child(%d)'%source)))
        ActionChains(self.driver).click(click_element).perform()

        # 选择客户级别
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body>div:nth-child(10)>div>div.el-card__body>div>div.crm-create-flex>div>div.content>div>div>form>div:nth-child(6)>div>div>div>input')))
        ActionChains(self.driver).click(click_element).perform()

        # 点击客户级别
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body>div:last-child>div>div>ul>li:nth-child(%d)'%level)))
        ActionChains(self.driver).click(click_element).perform()

        # 点击保存
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body>div:nth-child(10)>div>div>div>div:nth-child(3)>button:last-child'))).click()

    def testCreateContact01_02(self):
        """
        检查客户是否建立成功
        """
        
        Mylogin(self.driver).login()

        # 点击客户管理
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body>div>section>header>div>div>div>a:nth-child(2)'))).click()
        time.sleep(20)
        # 点击待办事项
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#app>section>section>aside>div>ul>a:nth-child(2)>li'))).click()
        # 点击“待进入公海的客户”
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="crm-main-container"]/div/div/div[2]/div/div[1]/div[4]')))
        ActionChains(self.driver).click(click_element).perform()
        # 获取公海里的第一条个人信息
        # 客户名称
        user_name = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="crm-table"]/div[3]/table/tbody/tr[1]/td[1]/div'))).text
        # 手机号
        user_phone = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="crm-table"]/div[3]/table/tbody/tr[1]/td[2]/div'))).text
        # 客户来源
        user_source = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="crm-table"]/div[3]/table/tbody/tr[1]/td[4]/div'))).text
        # 客户行业
        user_profession = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="crm-table"]/div[3]/table/tbody/tr[1]/td[5]/div'))).text
        # 客户级别
        user_level = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="crm-table"]/div[3]/table/tbody/tr[1]/td[6]/div'))).text
        # 断言结果
        self.assertEqual(username,user_name)
        self.assertEqual(phone,user_phone)
        self.assertEqual(source,user_source)
        self.assertEqual(profession,user_profession)
        self.assertEqual(level,user_level)

    def testCreateContact01_03(self):
        """
        新建联系人
        """
        LogCreate(self.driver).logcreate()
        
        # 点击“联系人”
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div/div[2]')))
        ActionChains(self.driver).click(click_element).perform()

        # 点击“新建”
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body>div:nth-child(9)>div>div:nth-child(2)>div:nth-child(2)>div:nth-child(2)>div>button'))).click()

        try:
            time.sleep(2)
            # 切换alert
            alertInfo = self.driver.switch_to.alert
            # 驳回警告信息
            alertInfo.dismiss()
        except:
            pass

        # 填写客户名称，随机生成手机号    
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div[1]/div/div[2]/div/div[2]/div/div/form/div[1]/div/div[1]/input'))).send_keys(username)
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div[1]/div/div[2]/div/div[2]/div/div/form/div[3]/div/div/input'))).send_keys(phone)

        # 点击保存
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div[1]/div/div[3]/button[2]'))).click()

    def testCreateContact01_04(self):
        """
        检查联系人是否创建成功
        """
        Mylogin(self.driver).login()

        # 点击客户管理
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body>div>section>header>div>div>div>a:nth-child(2)'))).click()
        time.sleep(20)
        # 点击待办事项
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/section/section/aside/div/ul/a[5]/li')))
        ActionChains(self.driver).click(click_element).perform()
        # 获取联系人的第一条个人信息
        # 联系人名称
        user_name = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="crm-table"]/div[3]/table/tbody/tr[1]/td[2]/div'))).text
        # 手机号
        user_phone = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="crm-table"]/div[3]/table/tbody/tr[1]/td[4]/div'))).text
        # 断言结果
        self.assertEqual(username,user_name)
        self.assertEqual(phone,user_phone)

    def testCreateContact01_05(self):
        """
        新建商机
        """
        LogCreate(self.driver).logcreate()

        # 点击商机
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div/div[3]')))
        ActionChains(self.driver).click(click_element).perform()

        # 点击“新建”
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body>div:nth-child(9)>div>div:nth-child(2)>div:nth-child(2)>div:nth-child(3)>div>button'))).click()

        try:
            time.sleep(2)
            # 切换alert
            alertInfo = self.driver.switch_to.alert
            # 驳回警告信息
            alertInfo.dismiss()
        except:
            pass
        
        # 点击客户名称
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div[1]/div/div[2]/div/div[2]/div/div/form/div[2]/div/span/div[2]')))
        ActionChains(self.driver).click(click_element).perform()

        # 关联第一个客户
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[6]/div[1]/div[2]/div/div/div[2]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span')))
        ActionChains(self.driver).click(click_element).perform()
        # 点击确定
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[6]/div[1]/div[3]/button[2]'))).click()

        # 点击商机状态组
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div[1]/div/div[2]/div/div[2]/div/div/form/div[6]/div/div/div/input'))).click()
        # 选择商机组1，后续可通过循环，获取列表，再用循环得到不同的商机阶段，提高覆盖率
        time.sleep(2)
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//span[contains(text(),"商机组1")]')))
        ActionChains(self.driver).click(click_element).perform()

        # 点击商机阶段
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div[1]/div/div[2]/div/div[2]/div/div/form/div[7]/div/div/div[1]/input'))).click()
        time.sleep(2)
        # 选中第一个商机阶段
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//span[contains(text(),"看不见")]')))
        ActionChains(self.driver).click(click_element).perform()

        # 点击保存
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div[1]/div/div[3]/button[2]'))).click()

    def testCreateContact01_06(self):
        """
        核对商机是否新建成功
        """
        Mylogin(self.driver).login()

        # 点击客户管理
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body>div>section>header>div>div>div>a:nth-child(2)'))).click()
        time.sleep(20)
        # 点击商机
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/section/section/aside/div/ul/a[7]/li')))
        ActionChains(self.driver).click(click_element).perform()

        # 获取商机状态组
        business_group = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="crm-table"]/div[3]/table/tbody/tr[1]/td[7]/div'))).text
        # 断言结果
        self.assertEqual('商机组1',business_group)
        
        # 获取商机阶段
        business_stage = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="crm-table"]/div[3]/table/tbody/tr[1]/td[8]/div'))).text
        # 断言结果
        self.assertEqual('看不见',business_stage)

        # 创建用户
        create_user = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="crm-table"]/div[3]/table/tbody/tr[1]/td[12]/div'))).text
        # 断言结果
        self.assertEqual('mengxun',create_user)

        # 后续添加时间校验与随机校验

    def testCreateContact01_07(self):
        """
        新建合同
        """
        LogCreate(self.driver).logcreate()

        # 点击合同
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div/div[4]')))
        ActionChains(self.driver).click(click_element).perform()        
        
        # 点击新建
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body>div:nth-child(9)>div>div:nth-child(2)>div:nth-child(2)>div:nth-child(4)>div>button'))).click()

        try:
            time.sleep(2)
            # 切换alert
            alertInfo = self.driver.switch_to.alert
            # 驳回警告信息
            alertInfo.dismiss()
        except:
            pass

        # 输入合同编号
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div[1]/div/div[2]/div[1]/div[2]/div/div/form/div[1]/div/div/input'))).send_keys(contract_id)
        # 输入合同名称
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div[1]/div/div[2]/div[1]/div[2]/div/div/form/div[2]/div/div[1]/input'))).send_keys(contract_name)

        # 客户名称
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div[1]/div/div[2]/div[1]/div[2]/div/div/form/div[3]/div/span/div[2]')))
        ActionChains(self.driver).click(click_element).perform()
        # 选择第一个客户
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[6]/div/div/div/div/div[2]/div[3]/table/tbody/tr[1]/td/div/label/span/span')))
        ActionChains(self.driver).click(click_element).perform()
        # 点击确定
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[6]/div[1]/div[3]/button[2]'))).click()
        
        # 点击提交审核
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div[1]/div/div[3]/button[3]'))).click()

    def testCreateContact01_08(self):
        """
        核对合同是否新建成功
        """

        Mylogin(self.driver).login()

        # 点击客户管理
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body>div>section>header>div>div>div>a:nth-child(2)'))).click()
        time.sleep(20)
        # 点击合同
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/section/section/aside/div/ul/a[8]/li')))
        ActionChains(self.driver).click(click_element).perform()

        # 获取合同编号
        id = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="crm-table"]/div[4]/div[2]/table/tbody/tr[1]/td[2]/div'))).text
        
        # 获取和同名称
        name = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="crm-table"]/div[3]/table/tbody/tr[1]/td[3]/div'))).text

        # 获取状态
        status = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="crm-table"]/div[5]/div[2]/table/tbody/tr[1]/td[20]/div/div'))).text

        # 断言结果
        self.assertEqual(id,contract_id)
        self.assertEqual(name,contract_name)
        self.assertEqual(status,'待审核')
    
    def testCreateContact01_09(self):
        """
        核对新建客户必填信息提示是否正确
        """ 
        LogCreate(self.driver).logcreate()

        # 点击“新建”
        cilck_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div[2]/div[2]/div/div/button')))
        ActionChains(self.driver).click(cilck_element).perform()

        try:
            time.sleep(2)
            # 切换alert
            alertInfo = self.driver.switch_to.alert
            # 驳回警告信息
            alertInfo.dismiss()
        except:
            pass

        # 点击保存
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body>div:nth-child(10)>div>div>div>div:nth-child(3)>button:last-child'))).click()

        time.sleep(2)
        # 获取客户名称提示信息
        username_alert = WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(),"客户名称不能为空")]'))).text
        # 手机号提示信息
        phone_alert = WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(),"手机不能为空")]'))).text
        # 客户来源提示信息
        source_alert = WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(),"客户来源不能为空")]'))).text
        # 客户行业提示信息
        profession_alert = WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(),"客户行业不能为空")]'))).text
        # 客户级别提示信息
        level_alert = WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(),"客户级别不能为空")]'))).text

        # 断言结果
        self.assertEqual('客户名称不能为空',username_alert)
        self.assertEqual('手机不能为空',phone_alert)
        self.assertEqual('客户来源不能为空',source_alert)
        self.assertEqual('客户行业不能为空',profession_alert)
        self.assertEqual('客户级别不能为空',level_alert)

    def testCreateContact01_10(self):
        """
        核对新建联系人必填信息提示是否正确
        """ 
        LogCreate(self.driver).logcreate()

        # 点击“联系人”
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div/div[2]')))
        ActionChains(self.driver).click(click_element).perform()

        # 点击“新建”
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body>div:nth-child(9)>div>div:nth-child(2)>div:nth-child(2)>div:nth-child(2)>div>button'))).click()

        try:
            time.sleep(2)
            # 切换alert
            alertInfo = self.driver.switch_to.alert
            # 驳回警告信息
            alertInfo.dismiss()
        except:
            pass

        # 点击保存
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div[1]/div/div[3]/button[2]'))).click()
        time.sleep(2)
        # 获取姓名提示信息
        name_alert = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//div[contains(text(),"姓名不能为空")]'))).text
        # 断言结果
        self.assertEqual(name_alert,'姓名不能为空')

    def testCreateContact01_11(self):
        """
        核对新建商机必填信息提示是否正确
        """ 
        LogCreate(self.driver).logcreate()

        # 点击商机
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div/div[3]')))
        ActionChains(self.driver).click(click_element).perform()

        # 点击“新建”
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body>div:nth-child(9)>div>div:nth-child(2)>div:nth-child(2)>div:nth-child(3)>div>button'))).click()

        try:
            time.sleep(2)
            # 切换alert
            alertInfo = self.driver.switch_to.alert
            # 驳回警告信息
            alertInfo.dismiss()
        except:
            pass

        # 点击保存
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div[1]/div/div[3]/button[2]'))).click()
        time.sleep(2)
        # 获取客户名称提示
        username_alert = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//div[contains(text(),"客户名称不能为空")]'))).text
        # 获取商机状态组提示信息
        group_alert = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//div[contains(text(),"商机状态组不能为空")]'))).text
        # 获取商机阶段提示信息
        business_stage_alert = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//div[contains(text(),"商机阶段不能为空")]'))).text

        # 断言结果
        self.assertEqual("客户名称不能为空",username_alert)
        self.assertEqual("商机状态组不能为空",group_alert)
        self.assertEqual("商机阶段不能为空",business_stage_alert)

    def testCreateContact01_12(self):
        """
        核对新建合同必填项提示信息是否正确
        """
        LogCreate(self.driver).logcreate()

        # 点击合同
        click_element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div/div[4]')))
        ActionChains(self.driver).click(click_element).perform()        
        
        # 点击新建
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body>div:nth-child(9)>div>div:nth-child(2)>div:nth-child(2)>div:nth-child(4)>div>button'))).click()

        try:
            time.sleep(2)
            # 切换alert
            alertInfo = self.driver.switch_to.alert
            # 驳回警告信息
            alertInfo.dismiss()
        except:
            pass
        
        # 点击提交审核
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div[1]/div/div[3]/button[3]'))).click()
        time.sleep(2)
        # 获取合同编号提示信息
        contract_id_alert = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//div[contains(text(),"合同编号不能为空")]'))).text
        # 获取合同名称提示信息
        contract_name_alert = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//div[contains(text(),"合同名称不能为空")]'))).text
        # 获取客户名称提示信息
        status_alert = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//div[contains(text(),"客户名称不能为空")]'))).text

        # 断言结果
        self.assertEqual("合同编号不能为空",contract_id_alert)
        self.assertEqual("合同名称不能为空",contract_name_alert)
        self.assertEqual("客户名称不能为空",status_alert)