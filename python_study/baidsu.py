# -*- encoding: utf-8 -*-

from selenium import webdriver
import unittest,time
import HTMLTestRunner #引入HTMLTestRunner 包


class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"


    #百度搜索用例

    def test_bd_search(self):
        driver = self.driver
        driver.get(self.base_url)
        i='kw'
        driver.find_element_by_id(i).send_keys("HTMLTestRunner")
        driver.find_element_by_id("su").click()


    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == "__main__":#41621892

#测试套件
    suit = unittest.TestSuite()

#添加测试用例到测试套件中
    suit.addTest(Baidu('test_bd_search'))

#定义个报告存放路径
    filename = 'd:\\result5.html'
    # fp = file(filename,'wb')
    # fp=open(filename,'wb')
    file_prefix = time.strftime("%Y-%m-%d  %H_%M_%S", time.localtime())
    print(file_prefix)
    fp = open("./" + file_prefix + "_result.html", "wb")

#定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='百度搜索测试报告',
                                           description = u'用例执行情况:')

#运行测试用例
    runner.run(suit)
#关闭报告文件
    fp.close()