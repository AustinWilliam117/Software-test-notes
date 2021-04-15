import unittest
import time
import os,sys
from report import HTMLTestRunner

# 获取当前py文件路径地址，并进行路径分割（分割成目录路径和文件名称）
dirname,filename = os.path.split(os.path.abspath(sys.argv[0]))

print(dirname,filename)
case_path = ".\\case\\"
result = dirname + "\\report\\"

def creatsuite():
    # 定义单元测试容器
    testunit = unittest.TestSuite()

    # 定义搜索用例文件的方法
    discover = unittest.defaultTestLoader.discover(case_path,pattern='*.py',top_level_dir=None)

    # 将测试用例加入测试容器中
    for test_suite in discover:
        for casename in test_suite:
            testunit.addTest(casename)
        # print(testunit)
    return testunit

# 调用函数creatsuite()
test_case = creatsuite()

# 获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime((time.time())))

# 定义报告存储路径，支持相对路径
tdresult = result + day

# 检验路径下文件夹是否存在，不存在创建文件夹
if not os.path.exists(tdresult):
    os.mkdir(tdresult)

# 命名文件
filename = tdresult + "\\" + now + "_result.html"
fp = open(filename,'wb')
# 定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(
    stream = fp,
    title = "CRM测试报告",
    description = "执行情况: "
)
# 运行测试用例
# runner = unittest.TextTestRunner(verbosity=2)
runner = unittest.TextTestRunner()
runner.run(test_case)
# 关闭文件
fp.close()
