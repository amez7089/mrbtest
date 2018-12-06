#-*- coding:utf-8 -*-
#!/usr/bin/env python
#******************************************
#*******待收货订单退款（仅退款），商家拒绝*****
#*****************************************
#导入依赖模块
import xlrd,xlwt
import time
import re
from datetime import datetime
from selenium import webdriver
from xlutils.copy import copy
import sys
from lib2to3.tests.support import driver
from cgitb import text
from selenium.webdriver.support.ui import Select
# from Scripts.runxlrd import result
# from pip._vendor.retrying import Attempt
# from selenium.common.exceptions import StaleElementReferenceException
reload(sys)
sys.setdefaultencoding('utf-8')
import traceback

#导入购买商品并付款用例创建订单
execfile('AmezMallUI_004_BuyGood.py')

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
print u"****Case--AmezMallUI_010_FailureToReceiveRefund待收货订单退款（仅退款），商家拒绝--开始运行****"

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
    #判断是否登录成功，如果左上角出现“欢迎来到艾美e族商城”，则判断用户登录成功
    text = driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div/span").text
    print text
    if (text == u"欢迎来到艾美e族商城"):
        print u"登录成功！！"
    else:
        print u"登录失败！！"
    #点击全部订单标签进入订单页面
    #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(2)
    #进入会员中心--待收货页面
    driver.find_element_by_xpath("//*[@id='app']/div[1]/div/ul/li[2]/div[1]").click()
    time.sleep(1)
    #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(2)
    #待收货页面查看是否有待发货订单
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[3]/div[1]/ul/li[2]/p/span[1]").click()
    #查看待发货页面第一条数据是否为我们需要的订单
    #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(2)
    #获取订单号：
    orderNumber = str(driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/ul/li/dl/dd[1]").text)
    #提取出订单编号 
    orderNumber = re.findall(r"订单号：(.*)", orderNumber)
    #将提取出的List类型转化为str类型
    orderNumber = ''.join(orderNumber)
#     print type(orderNumber)
    print "orderNumber:",orderNumber
    #保存订单编号
    ws.write(138,5,orderNumber)
    
    #打开新窗口，商家登录发货
    print u"\n卖家登录发货！"
    NewWindow = 'window.open("http://company.test.amyun.cn");'
    driver.execute_script(NewWindow)
    #读取用户名
    ShopuserName = table.cell(140,5).value
    print ShopuserName
    #读取密码
    ShoppassWord = table.cell(141,5).value
    print ShoppassWord
    #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(2) 
    #输入用户名
    driver.find_element_by_xpath("//*[@id='my-form']/div[1]/div/input").send_keys(ShopuserName)
    #输入密码
    driver.find_element_by_xpath("//*[@id='my-form']/div[2]/div/input").send_keys(ShoppassWord)
    #点击登录
    driver.find_element_by_xpath("//*[@id='my-form']/div[3]/button[1]/span").click()
    time.sleep(3)
    driver.implicitly_wait(30)
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/ul/li[3]/div/ul/li[2]/div/a/button").click()
    time.sleep(1)
    #查看待发货订单页面第一条是不是我们需要的商品
    orderNumber1 = driver.find_element_by_xpath("//*[@id='main']/div[2]/div/div[6]/div[2]/p/span[2]").text
    print u"orderNumber1：",orderNumber1
    if (orderNumber1 == orderNumber):
        print u"订单匹配成功！"
    #保存订单编号
    ws.write(142,5,orderNumber1)
    #点击发货按钮，进入发货页面
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div/div[6]/div[2]/div/ul/li[5]/button").click()
    time.sleep(1)
    #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(2)
    #填写发货备忘
    driver.find_element_by_xpath("//*[@id='orderList']/div/div[2]/div/div[2]/div/textarea").send_keys(u"已发货，请买家注意查收!！")
    #填写物流单号
    trackingNumber = table.cell(145,5).value
    print u"物流单号为：",trackingNumber
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div/div[7]/div[3]/table/tbody/tr/td[2]/div/div/input").send_keys(trackingNumber)
    #点击确认发货
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div/div[7]/div[3]/table/tbody/tr/td[3]/div/button/span").click()
    time.sleep(5)
    print u"已经发货完成，运单号为：",trackingNumber
    #进入发货中页面，查看是否有订单是发货中
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div/ul[1]/li[2]").click()
    time.sleep(1)
    orderNumber2 = driver.find_element_by_xpath("//*[@id='main']/div[2]/div/div[2]/div/div[1]/span[1]/em").text
    print "orderNumber2:",orderNumber2
    if (orderNumber2 == orderNumber):
        print u"发货中页面存在该订单：",orderNumber2
    
    #买家在待收货页面申请退款
    print u"\n买家在待收货页面申请退款！"
    #切换句柄到会员退款页面
    driver.switch_to_window(driver.window_handles[0])
    #刷新页面
    driver.refresh()
    time.sleep(2)
    #待收货页面获取订单编号
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[2]/ul/li[4]/span[1]").click()
    time.sleep(2)
    orderNumber3 = driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[2]/div[1]/div/ul/li/dl/dd[1]").text
    #提取订单号
    print u"获取到的待收货订单号为：",orderNumber3
    orderNumber3 = str(orderNumber3)
    orderNumber3 = re.findall(r"订单号：(.*)", orderNumber3)
#     print u"正则后订单号为：",orderNumber3
    orderNumber3 = ''.join(orderNumber3)
    print "orderNumber3:",orderNumber3
    #保存
    ws.write(147,5,orderNumber3)
    if(orderNumber3 == orderNumber):
        print u"会员待收货中页面存在该订单：",orderNumber3
    #待收货页面点击申请退款
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[2]/ul/li[2]/div/div/div/button[2]").click()
    #申请退款
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div/div/div[3]/ul/li[2]/div[6]/span").click()
    #申请状态
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div/div/div[4]/div[2]/div[2]/form/label[1]/span[1]/input").click()
    #货物状态
    Select(driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div/div/div[4]/div[2]/div[2]/form/label[2]/select")).select_by_value("0")
    #退款原因
    Select(driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div/div/div[4]/div[2]/div[2]/form/label[3]/select")).select_by_value("7天无理由退换货")
    #退款说明
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div/div/div[4]/div[2]/div[2]/form/label[5]/textarea").send_keys(u"突然不想要了！")
    #点击提交
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div/div/div[4]/div[2]/div[2]/form/label[7]/button").click()
    #判断是否提交成功
    showInfo = driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/h6").text
    if (showInfo == u"退款申请已提交，请等待卖家处理！"):
        print u"退款提交成功！"
        
    #商家进行退款审核
    print u"\n商家进行退款审核！"
    #切换句柄到商家页面
    driver.switch_to_window(driver.window_handles[1])
    #进入售后服务--售前退款--退款记录页面
    driver.find_element_by_xpath("//*[@id='subapp']/header/div/nav/ul/li[6]/a/p").click()
    #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(2) 
    #获取退款订单的订单编号 
    orderNumber5 = driver.find_element_by_xpath("//*[@id='main']/div[2]/div[3]/div/div[3]/table/tbody/tr[1]/td[1]/div/div/ul/li[2]/p[2]/span[2]").text
    print "orderNumber5:",orderNumber5
    if (orderNumber5 == orderNumber):
        print u"售前服务-售前退款-退款记录页面存在该订单：",orderNumber5 
    #点击处理按钮
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[3]/div/div[3]/table/tbody/tr[1]/td[6]/div/button/span").click()
    time.sleep(1)
    #拒绝并填写备注信息
    driver.find_element_by_xpath("//*[@id='main']/div[2]/ul/li[1]/div[2]/div[1]/label[2]/span[2]").click()
    driver.find_element_by_xpath("//*[@id='main']/div[2]/ul/li[1]/div[2]/div[2]/div/textarea").send_keys(u"已发货，此商品不能退货！")
    #提交
    driver.find_element_by_xpath("//*[@id='main']/div[2]/ul/li[1]/div[3]/button[1]/span").click()
    time.sleep(5)
    #切换句柄到会员退款页面，刷新页面，查看退款是否成功
    driver.switch_to_window(driver.window_handles[0])
    #刷新页面
    driver.refresh()
    time.sleep(2)
    orderStatus = driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/p[1]/span[2]").text
    print u"目前退款状态为：",orderStatus
    if (orderStatus == u"退款失败"):
        print (u"Case--AmezMallUI_010_FailureToReceiveRefund待收货订单退款（仅退款），商家拒绝---结果：Pass!")
        ws.write(137,7, 'Pass')
        #如果成功，将错误日志覆盖
        ws.write(137,10,'')
    else:
        print (u"Case--AmezMallUI_010_FailureToReceiveRefund待收货订单退款（仅退款），商家拒绝---结果：Failed!")
        ws.write(137,7, 'Failed',style2)
    errorFlag = 1

except Exception as e:
    print(e)
    #抛出异常
    traceback.format_exc()
    #写入异常至用例文件中：
    errorInfo = str(traceback.format_exc())
    print "****errorInfo:",errorInfo
    ws.write(137,10,errorInfo,style2)
    
finally :
    if(errorFlag == 0):
        print (u"Case--AmezMallUI_010_FailureToReceiveRefund待收货订单退款（仅退款），商家拒绝---结果：Failed!")
        ws.write(137,7, 'Failed',style2)
    ws.write(137,9, 'lilei')
    ws.write(137,8, datetime.now(), style1)    
    #利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
    wb.save('D:\\Python27\\TestData\\UITestData.xls')
    #退出浏览器
    driver.quit()
    print u"****Case--AmezMallUI_010_FailureToReceiveRefund待收货订单退款（仅退款），商家拒绝--结束运行****"