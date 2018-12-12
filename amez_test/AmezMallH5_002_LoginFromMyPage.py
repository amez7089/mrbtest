#-*- coding:utf-8 -*-
#!/usr/bin/env python
#*************************************
#*******会员从我的页面登录**************
#*************************************
#导入依赖模块
import xlrd,xlwt
import time
from selenium import webdriver
from xlutils.copy import copy
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import traceback
from selenium.webdriver.common.keys import Keys

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
print u"****Case--AmezMallH5_002_LoginFromMyPage会员从我的页面登录--开始运行****"

try:
    #失败标志
    errorFlag = 0
    #读取用户名
    userName = table.cell(9,5).value
    print userName
    #读取密码
    passWord = table.cell(10,5).value
    print passWord
    #定义H5机型
    mobile_emulation = {'deviceName': 'iPhone X'}
    #打开谷歌浏览器
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation',mobile_emulation)
    driver = webdriver.Chrome(chrome_options=options)
    #最大化浏览器
    driver.maximize_window()
    #打开商城登录地址
    loginadress = table.cell(3,5).value
    driver.get(loginadress)
    time.sleep(2)
    #点击我的
    el=driver.find_element_by_xpath("//*[@id='app']/div/div[17]/section/div/a[5]/p")
    driver.execute_script("arguments[0].click();", el)
    time.sleep(2)
    #跳转至登录页面输入用户名密码,登录 
    driver.find_element_by_xpath("//*[@id='accountLogin']/div[2]/div[1]/input").send_keys(userName)
    driver.find_element_by_xpath("//*[@id='accountLogin']/div[2]/div[2]/input").send_keys(passWord,Keys.ENTER)
    #再次点击我的，判断是否登录成功 
    time.sleep(2)
    el=driver.find_element_by_xpath("//*[@id='app']/div/div[17]/section/div/a[5]/p")
    driver.execute_script("arguments[0].click();", el)
    time.sleep(2)
    ShowUserName = driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[2]").text
    print u"我的页面显示的用户名为：",ShowUserName
    ReadUserName = table.cell(21,5).value
    if (ShowUserName == ReadUserName):
        print u"登录成功！！！"
        print (u"Case--AmezMallH5_002_LoginFromMyPage会员从我的页面登录--结果：Pass!")
        ws.write(15,7, 'Pass')    
        #如果成功，将错误日志覆盖
        ws.write(15,10,'')
    else:
        print u"登录失败！！！"
        print (u"Case--AmezMallH5_002_LoginFromMyPage会员从我的页面登录--结果：Failed!")
        ws.write(15,7, 'Failed',style2) 
    errorFlag = 1
except Exception as e:
    print(e)
    #抛出异常
    traceback.format_exc()
    #写入异常至用例文件中：
    errorInfo = str(traceback.format_exc())
    print "****errorInfo:",errorInfo
    ws.write(15,10,errorInfo,style2)
    
finally :
    if(errorFlag == 0):
        print (u"Case--AmezMallH5_002_LoginFromMyPage会员从我的页面登录--结果：Failed!")
        ws.write(15,7, 'Failed',style2)
    #写入执行人员
    ws.write(15,9, 'zhouchuqi')
    #写入执行日期
    ws.write(15,8, datetime.now(), style1)    
    #利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
    wb.save('E:\\gitworksqace\\mrbdome1\\test1\\amez_test\\H5TestData.xls')
    #退出浏览器
    driver.quit()
    print u"Case--AmezMallH5_002_LoginFromMyPage会员从我的页面登录.py运行结束！！！"