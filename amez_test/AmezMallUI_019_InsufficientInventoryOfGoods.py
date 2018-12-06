#-*- coding:utf-8 -*-
#!/usr/bin/env python
#*********************************
#*******搜索查看库存为0的商品*******
#*********************************
#导入依赖模块
import xlrd,xlwt
import time
from selenium import webdriver
from xlutils.copy import copy
from datetime import datetime
import sys
from lib2to3.tests.support import driver
from selenium.common.exceptions import StaleElementReferenceException
from cgitb import text
reload(sys)
sys.setdefaultencoding('utf-8')
import traceback

#打开用例文件，读取对应用例的用户名等数据
casefile = xlrd.open_workbook('D:\\Python27\\TestData\\UITestData.xls', formatting_info=True)
#设置日期格式
style1 = xlwt.XFStyle()
style1.num_format_str = 'YYYY-MM-DD HH:MM:SS'
#设置单元格背景颜色
font0 = xlwt.Font()
font0.name = 'Times New Roman' #字体
font0.colour_index = 2  #颜色
font0.bold = True #加粗
style2 = xlwt.XFStyle()
style2.font = font0
#准备向用例文件中写入测试结果
wb = copy(casefile)
ws = wb.get_sheet(0)
# 打开第一张表
table = casefile.sheets()[0]
print u"****Case--AmezMallUI_019_InsufficientInventoryOfGoods搜索查看库存为0的商品--开始运行****"

try:
#商家登录下架对应商品
    #失败标志
    errorFlag = 0
    #读取用户名
    userName = table.cell(5,5).value
    print userName
    #读取密码
    passWord = table.cell(6,5).value
    print passWord
    #打开谷歌浏览器
    driver=webdriver.Chrome()
    #最大化浏览器
    driver.maximize_window()
    #打开商城登录地址
    loginadress = table.cell(3,5).value
    driver.get(loginadress)
    #点击请登录/注册按钮
    driver.find_element_by_xpath("//*[@id='app']/div[1]/div/ul/li[1]").click()
    time.sleep(1)
    #输入用户名
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div/div[2]/div[2]/div[1]/input").send_keys(userName)
    #输入密码
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div/div[2]/div[2]/div[2]/input").send_keys(passWord)
    #点击登录
    driver.find_element_by_id("loginBtn").click()
    time.sleep(1)
    driver.implicitly_wait(30)
    #判断是否登录成功，如果左上角出现“欢迎来到艾美e族商城”，则判断用户登录成功
    text = driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div/span").text
    print text
    if (text == u"欢迎来到艾美e族商城"):
        print u"登录成功！！"
    else:
        print u"登录失败！！"
    #搜索栏中输入指定文字进行商品搜索
    searchtext = table.cell(292,5).value
    print searchtext
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[1]/div[1]/div[2]/div[2]/div/input").send_keys(searchtext)
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[1]/div[1]/div[2]/div[2]/button").click()
    #因为在点击时页面刷新，导致元素找不到，所以此函数作用是当找不到元素时，再次获取
    def retryingFindClick(by):
        result = False
        Attempts = 0
        while Attempts < 2:
            try:
                result = driver.find_element_by_xpath(by).text
                break
            except StaleElementReferenceException, e:
                print (e)
                pass
            Attempts += 1
        return result
    textGoods = retryingFindClick("//*[@id='am_content']/div/div[2]/div[3]/div[2]/div[2]/ul/li[1]/a/div/div[1]")
    print "textGoods:",textGoods
    readGoods = table.cell(293,5).value
    print "readGoods:",readGoods
    if (textGoods == readGoods):
        print u"搜索商品成功！！"
        #进入商品详情页面
        driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[3]/div[2]/div[2]/ul/li[1]/a/div/div[1]").click()
        time.sleep(2)
        #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
        for handle in driver.window_handles:
            driver.switch_to_window(handle)
        time.sleep(2)
        #查看是否显示库存不足
        KuChun = driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[1]/div[1]/div[2]/div[8]/button").text
        print "KuChun:",KuChun
        if (KuChun == u"库存不足"):
            print (u"Case--AmezMallUI_019_InsufficientInventoryOfGoods搜索查看库存为0的商品---结果：Pass!") 
            ws.write(287,7, 'Pass')
            #如果成功，将错误日志覆盖
            ws.write(287,10,'')
        else:
            print (u"Case--AmezMallUI_019_InsufficientInventoryOfGoods搜索查看库存为0的商品---结果：Failed!")
            ws.write(287,7, 'Failed',style2)
    
    #将失败标志置为1，表示脚本执行完成           
    errorFlag = 1
    
except Exception as e:
    print(e)
    #抛出异常
    traceback.format_exc()
    #写入异常至用例文件中：
    errorInfo = str(traceback.format_exc())
    print "****errorInfo:",errorInfo
    ws.write(287,10,errorInfo,style2)
    #退出浏览器
    driver.quit()
    
finally :
    if(errorFlag == 0):
        print (u"Case--AmezMallUI_019_InsufficientInventoryOfGoods搜索查看库存为0的商品---结果：Failed!")
        ws.write(287,7, 'Failed',style2)
    ws.write(287,9, 'lilei')
    ws.write(287,8, datetime.now(), style1)
    #利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
    wb.save('D:\\Python27\\TestData\\UITestData.xls')
    #退出浏览器
    driver.quit()
    print u"****Case--AmezMallUI_019_InsufficientInventoryOfGoods.py--结束运行****"