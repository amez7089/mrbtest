from uiautomator import device as d
import unittest
class Test(unittest.TestCase):
    #初始化工作
    def setUp(self):
        print("初始化工作")
    #退出清理工作
    def tearDown(self):
        print("测试结束")

    #测试点击QQ
    def test_first(self):
        d.screen.on()
        d(text="QQ").click()
        print("点击测试完成")

    #测试登录QQ
    def test_second(self):
        #登录qq
        login()
        print ("登录测试完成")            

    #测试滑动操作
    def test_third(self):
        doSthing()
        print ("测试3完成"  )       


if __name__ == '__main__':
        unittest.main()
