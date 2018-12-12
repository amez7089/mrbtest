#-*- coding:utf-8 -*-
#!/usr/bin/env python
#*************************************
#*******积分商城搜索商品****************
#*************************************
#导入依赖模块
import xlrd,xlwt
import time
from selenium import webdriver
from xlutils.copy import copy
from datetime import datetime
import sys
import re
from lib2to3.tests.support import driver
from cgitb import text
# from Scripts.runxlrd import result
# from pip._vendor.retrying import Attempt
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
print u"****Case--AmezMallUI_017_IntegralMallBuyGoods积分商城购买商品--开始运行****"

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
    #点击积分商城
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[1]/div[2]/div/ul/li[2]").click()
    time.sleep(2)
    #搜索栏中输入指定文字进行商品搜索
    searchtext = table.cell(265,5).value
    print "searchtext:",searchtext
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[1]/div[1]/div[2]/div[2]/div/input").send_keys(searchtext)
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[1]/div[1]/div[2]/div[2]/button").click()
    time.sleep(2)
    SearchResult = driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[3]/ul/li/a/div/div[1]").text
    print "SearchResult:",SearchResult
    ws.write(266,5,SearchResult)
    if ("小米电视" in SearchResult):
        print u"积分商城搜索到指定商品！！！"
        #进入商品详情页
        driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[3]/ul/li/a/div/div[1]").click()
        time.sleep(1)
        #确认当前窗口句柄
        for handle in driver.window_handles:
            driver.switch_to_window(handle)
        time.sleep(2)
        #立即兑换
        driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[1]/div[1]/div[2]/div[9]/button").click()
        time.sleep(2)
        #进入订单确认页面查看应付金额信息
        NeedPay = driver.find_element_by_xpath("//*[@id='footer_total']/div/div/p").text
        print u"订单应付金额为:",NeedPay
        #买家留言：
        driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[2]/ul/li/input").send_keys(u"请保证质量！")
        #提交订单
        driver.find_element_by_xpath("//*[@id='footer_total']/div/div/button").click()   
        time.sleep(1)     
        #输入支付密码
        driver.find_element_by_xpath("//*[@id='ids_undefined']/input[1]").send_keys("1")
        driver.find_element_by_xpath("//*[@id='ids_undefined']/input[2]").send_keys("2")
        driver.find_element_by_xpath("//*[@id='ids_undefined']/input[3]").send_keys("3")
        driver.find_element_by_xpath("//*[@id='ids_undefined']/input[4]").send_keys("4")
        driver.find_element_by_xpath("//*[@id='ids_undefined']/input[5]").send_keys("5")
        driver.find_element_by_xpath("//*[@id='ids_undefined']/input[6]").send_keys("6")
        #点击立即兑换
        driver.find_element_by_xpath("//*[@id='am_content']/div/div[3]/div[2]/div[2]/div[2]/button[1]").click()
        time.sleep(1)
        #选择余额支付
        driver.find_element_by_xpath("//*[@id='am_content']/div/div[3]/div[1]/span[3]").click()
        PayButton = driver.find_element_by_xpath("//*[@id='am_content']/div/div[3]/div[1]/span[3]").text
        print "PayButton:",PayButton
        #确定支付
        driver.find_element_by_xpath("//*[@id='am_content']/div/div[4]/div/button").click()
        #确认当前窗口句柄
        for handle in driver.window_handles:
            driver.switch_to_window(handle)
        time.sleep(2)
        #支付完成后关闭弹出的窗口
        driver.find_element_by_xpath("//*[@id='am_content']/div/div[3]/div[2]/div[1]/span").click()
        #确认当前窗口句柄
        for handle in driver.window_handles:
            driver.switch_to_window(handle)
        time.sleep(1)
        Successfulpayment = driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]").text
        print Successfulpayment
        if (Successfulpayment == u"支付成功"):
            print u"订单支付成功"
        #点击查看订单，此订单出现在订单列表第一行
        OrderNumber = driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[3]/p[1]").text
        #提取订单号
        print u"获取到的订单号为：",OrderNumber
        OrderNumber = str(OrderNumber)
        OrderNumber = re.findall(r"订单号：(.*)", OrderNumber)
        print u"正则后订单号为：",OrderNumber
        OrderNumber = ''.join(OrderNumber)
        print "OrderNumber:",OrderNumber
        #保存订单编号
        ws.write(272,5,OrderNumber)
        driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/a").click()
        #进入订单页面，确认当前窗口句柄
        for handle in driver.window_handles:
            driver.switch_to_window(handle)
        time.sleep(1)
        #进入订单详情页面
        driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/ul/li[2]/div/div/div/button[1]").click()
        time.sleep(2)
        #查看订单
        OrderStatus = driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/h4").text
        print "OrderStatus:",OrderStatus
        OrderNumber1 = driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[1]/span[2]").text
        print "OrderNumber1:",OrderNumber1
        #提取订单号
        print u"获取到的订单号为：",OrderNumber1
        OrderNumber1 = str(OrderNumber1)
        OrderNumber1 = re.findall(r"订单编号：(.*)", OrderNumber1)
        print u"正则后订单号为：",OrderNumber1
        OrderNumber1 = ''.join(OrderNumber1)
        print "OrderNumber:",OrderNumber1
        #保存订单编号
        ws.write(274,5,OrderNumber)
        if (OrderStatus == u"待发货" and OrderNumber1 == OrderNumber ):
            print u"积分商城购买商品并付款成功！！"
            print (u"Case--AmezMallUI_017_IntegralMallBuyGoods积分商城购买商品---结果：Pass!")
            ws.write(259,7, 'Pass')
            #如果成功，将错误日志覆盖
            ws.write(259,10,'')
        else:
            print u"积分商城购买商品并付款失败！！"
            ws.write(259,7, 'Failed',style2)    
            ws.write(259,10, u'积分商城购买商品并付款失败',style2)
    
    #将失败标志置为1，表示脚本执行完成        
    errorFlag = 1
    
except Exception as e:
    print(e)
    #抛出异常
    traceback.format_exc()
    #写入异常至用例文件中：
    errorInfo = str(traceback.format_exc())
    print "****errorInfo:",errorInfo
    ws.write(259,10,errorInfo,style2)
        
finally :
    if(errorFlag == 0):
        print (u"Case--AmezMallUI_017_IntegralMallBuyGoods积分商城购买商品--结果：Failed!")
        ws.write(259,7, 'Failed',style2)
    ws.write(259,9, 'zhouchuqi')
    ws.write(259,8, datetime.now(), style1)    
    #利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
    wb.save('E:\\gitworksqace\\mrbdome1\\test1\\amez_test\\UITestData.xls')
    #退出浏览器
#     driver.quit()
    print u"Case--AmezMallUI_017_IntegralMallBuyGoods.py运行结束！！！"