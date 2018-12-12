#-*- coding:utf-8 -*-
#!/usr/bin/env python
#*********************************
#*******积分商城搜索商品************
#*********************************
#导入依赖模块
import xlrd,xlwt
import time
from selenium import webdriver
from xlutils.copy import copy
import datetime
import sys
from lib2to3.tests.support import driver
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium.webdriver.common.keys import Keys
import traceback

#打开用例文件，读取对应用例的用户名等数据
casefile = xlrd.open_workbook('E:\\gitworksqace\\mrbdome1\\test1\\amez_test\\H5TestData.xls', formatting_info=True)
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
print u"****Case--AmezMallH5_015_IntegralMallSearchProduct积分商城搜索商品--开始运行****"

try:
#买家登录积分商城搜索商品
    errorFlag = 0
    #定义H5机型
    print u"\买家登录积分商城搜索商品"
    #读取用户名
    userName = table.cell(9,5).value
    print userName
    #读取密码
    passWord = table.cell(10,5).value
    print passWord
    mobile_emulation = {'deviceName': 'iPhone X'}
    #商城登录地址
    loginadress = table.cell(3,5).value
    #打开谷歌浏览器
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation',mobile_emulation)
    driver = webdriver.Chrome(chrome_options=options)
    #最大化浏览器
    driver.maximize_window()
    #打开商城登录地址
    driver.get(loginadress)
    time.sleep(2)
    #点击我的
    el=driver.find_element_by_xpath("//*[@id='app']/div/div[19]/section/div/a[5]/p")
    driver.execute_script("arguments[0].click();", el)
    time.sleep(2)
    #跳转至登录页面输入用户名密码,登录 
    driver.find_element_by_xpath("//*[@id='accountLogin']/div[2]/div[1]/input").send_keys(userName)
    driver.find_element_by_xpath("//*[@id='accountLogin']/div[2]/div[2]/input").send_keys(passWord,Keys.ENTER)
    time.sleep(3)
    #进入积分商城
    el=driver.find_element_by_xpath("//*[@id='app']/div/div[3]/section/ul/a[2]/span")
    driver.execute_script("arguments[0].click();", el)
    time.sleep(2)
    #搜索框输入要搜索的商品
    ReadGoods = table.cell(4,5).value
    #点击搜索栏进入搜索页面
    driver.find_element_by_xpath("//*[@id='integralMall']/div/form/input").click()
    time.sleep(1)
    #输入要搜索的商品
    driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[1]/form/input").send_keys(ReadGoods,Keys.ENTER)
    time.sleep(3)
    #查看被搜索出来的商品第一条
    SearchGoods = driver.find_element_by_xpath("//*[@id='app']/div/section[2]/ul/li/div[2]/div[1]").text
    NeedIntegral = driver.find_element_by_xpath("//*[@id='app']/div/section[2]/ul/li/div[2]/div[3]/div/div/span[1]").text
    print "SearchGoods:",SearchGoods
    print "NeedIntegral:",NeedIntegral
    #保存搜索出来的商品信息及所需积分
    ws.write(361,5,SearchGoods)
    ws.write(362,5,NeedIntegral)
    if ("小米电视" in SearchGoods):
        print u"积分商城搜索商品成功！！！"
        ws.write(354,7, 'Pass')
        #如果成功，将错误日志覆盖
        ws.write(354,10,"")
        #退出浏览器
        driver.quit()
    else:
        print u"积分商城搜索商品失败！！！"
        ws.write(354,7, 'Failed',style2)
        #退出浏览器
        driver.quit()
    #将失败标志置为1，表示脚本执行完成           
    errorFlag = 1
    
except Exception as e:
    print(e)
    #抛出异常
    traceback.format_exc()
    #写入异常至用例文件中：
    errorInfo = str(traceback.format_exc())
    print "****errorInfo:",errorInfo
    ws.write(354,10,errorInfo,style2)
    #退出浏览器
    driver.quit()
    
finally :
    if(errorFlag == 0):
        print (u"Case--AmezMallH5_015_IntegralMallSearchProduct积分商城搜索商品---结果：Failed!")
        ws.write(354,7, 'Failed',style2)
    ws.write(354,9, 'zhouchuqi')
    ws.write(354,8, datetime.datetime.now(), style1)
    #利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
    wb.save('E:\\gitworksqace\\mrbdome1\\test1\\amez_test\\H5TestData.xls')
    print u"****Case--AmezMallH5_015_IntegralMallSearchProduct.py--结束运行****"