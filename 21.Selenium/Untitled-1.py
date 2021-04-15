from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("file:///home/william/DYJ/software-test/21.Selenium/html/alert.html")

driver.find_element_by_id("prompt").click()
sleep(2)

# 返回alert弹出框中的文本信息
alertInfo = driver.switch_to.alert
print(alertInfo.text)

alertInfo.send_keys("输入啥")

# 接受警告信息
alertInfo.accept()

# 驳回警告信息
# alertInfo.dismiss()

sleep(2)
driver.quit()