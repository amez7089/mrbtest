# -*- coding: utf-8 -*-
import unittest
import HTMLTestRunnerCN
import time
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.age = 32
        self.name = "小D课堂"
        print("setUp method=====")
    def tearDown(self):
        print("tearDown method====")

        self.assertEqual("foo".upper(),"FOO")



    def test_one(self):
        print("test_one 二当家小D 来了")
        self.assertEqual(self.name,"小D课堂",msg= "名字不对" )

    def test_two(self):
        print("test_two 前端 来了")
        self.assertFalse("xd". isupper(),msg="不是大写")
        #self.assertEqual(True, False)


    def test_three(self):
        print("test_three 后端 来了")
        self.assertEqual(self.age, 32)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase("test_one"))
    suite.addTest(MyTestCase("test_two"))
    suite.addTest(MyTestCase("test_three"))

#定义个报告存放路径
    filename = 'd:\\result.html'
    file_prefix = time.strftime("%Y-%m-%d  %H_%M_%S", time.localtime())
    print(file_prefix)
    fp = open("./" + file_prefix + "_result.html", "wb")
    # fp = file(filename,'wb')

#定义测试报告
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp,
                                           title='小D课堂',
                                           description = u'用例执行情况:',
                                            tester=u'周楚奇'
                                             )

#运行测试用例
    runner.run(suite)

#关闭报告文件
    fp.close()
