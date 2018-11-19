# -*- coding: utf-8 -*-
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
# import HTMLTestRunner

def Suite():
    testunit=unittest.TestSuite()
    test_dir = "E:\\gitworksqace\\mrbdome1\\test1\\mrb_automation_test"
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='api1.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit

if __name__=="__main__":
    #测试报告的存放路径
    test_report = "E:\\gitworksqace\\mrbdome1\\test1\\mrb_automation_test"
    #按照一定的格式获取当前的时间
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    #定义报告存放路径
    filename = test_report+'\\'+'Reportresult_'+now+'.html'
    fp = open(filename,'wb')
    #定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title=u'艾美商城接口测试报告,测试结果如下：',
                            description=u'测试用例执行情况：')
    #运行测试
    runner.run(Suite())
    #关闭报告文件
    fp.close()
