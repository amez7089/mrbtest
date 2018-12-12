#-*- coding:utf-8 -*-
#!/usr/bin/env python
#*********************************
#*******会员搜索商品****************
#*********************************
#导入依赖模块
import xlrd,xlwt
import time
from selenium import webdriver
from xlutils.copy import copy
from datetime import datetime
import sys
from lib2to3.tests.support import driver
from cgitb import text
from selenium.common.exceptions import StaleElementReferenceException
reload(sys)
sys.setdefaultencoding('utf-8')
import traceback

#打开用例文件，读取对应用例的用户名等数据
casefile = xlrd.open_workbook('E:\\gitworksqace\\mrbdome1\\test1\\amez_test\\UITestData.xls', formatting_info=True)
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
print u"****Case--AmezMallUI_002_SearchGood会员搜索商品--开始运行****"

try:
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
    driver.find_element_by_class_name("login").click()
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
    text = driver.find_element_by_class_name("left").text
    print text
    if (text == u"欢迎来到艾美e族商城"):
        print u"登录成功！！"
    else:
        print u"登录失败！！"
    #搜索栏中输入指定文字进行商品搜索
    searchtext = table.cell(13,5).value
    print searchtext
    driver.find_element_by_class_name("searchIn").send_keys(searchtext)
    driver.find_element_by_class_name("searchBtn").click()
    time.sleep(2)
    #因为在点击时页面刷新，导致元素找不到，所以此函数作用是当找不到元素时，再次获取
    def retryingFindClick(by):
        result = False
        Attempts = 0
        while Attempts < 5:
            try:
                result = driver.find_elements_by_class_name(by)[0].text
                break
            except StaleElementReferenceException, e:
                print(e)
                pass
            Attempts += 1
        return result
    #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    sreach_window=driver.current_window_handle[1]
    time.sleep(2)
    textMi = retryingFindClick("goodsName")
    print "textMi:",textMi
    readMi = table.cell(14,5).value
    print "readMi:",readMi
    if (textMi == readMi):
        print u"会员搜索商品成功！！"
        ws.write(8,7, 'Pass')
        #如果成功，将错误日志覆盖
        ws.write(8,10,'')
    else:
        print u"会员搜索商品失败！！"
        ws.write(8,7, 'Failed',style2)
    errorFlag = 1
    
except Exception as e:
    print(e)
    #抛出异常
    traceback.format_exc()
    #写入异常至用例文件中：
    errorInfo = str(traceback.format_exc())
    print "****errorInfo:",errorInfo
    ws.write(8,10,errorInfo,style2)
        
finally :
    if(errorFlag == 0):
        print (u"Case--AmezMallUI_002_SearchGood会员搜索商品--结果：Failed!")
        ws.write(8,7, 'Failed',style2)
    ws.write(8,9, 'zhouchuqi')
    ws.write(8,8, datetime.now(), style1)    
    #利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
    wb.save('E:\\gitworksqace\\mrbdome1\\test1\\amez_test\\UITestData.xls')
    #退出浏览器
    driver.quit()
    print u"Case--AmezMallUI_002_SearchGood.py运行结束！！！"