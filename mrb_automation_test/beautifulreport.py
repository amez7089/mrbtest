# -*- coding: utf-8 -*-
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import HTMLTestRunnerCN
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
    rrunner = HTMLTestRunner(
        stream=fp,
        title=u'自动化测试报告',
        #description='详细测试用例结果',    #不传默认为空
        tester=u"Findyou"     #测试人员名字，不传默认为QA
        )
    runner.run(Suite())
    #关闭报告文件
    fp.close()
