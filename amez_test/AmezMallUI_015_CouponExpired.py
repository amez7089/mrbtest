#-*- coding:utf-8 -*-
#!/usr/bin/env python
#*********************************
#*******优惠券过期*****************
#*********************************
#导入依赖模块
import xlrd,xlwt
import time
from selenium import webdriver
from xlutils.copy import copy
import datetime
# from datetime import datetime
import sys
from lib2to3.tests.support import driver
reload(sys)
sys.setdefaultencoding('utf-8')
import traceback
import win32gui
import win32con

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
print u"****Case--AmezMallUI_015_CouponExpired优惠券过期--开始运行****"

try:
    print u"---***商家用户登录发布优惠券***---"
    #读取用户名
    ShopuserName = table.cell(184,5).value
    print ShopuserName
    #读取密码
    ShoppassWord = table.cell(185,5).value
    print ShoppassWord
    #打开谷歌浏览器
    driver = webdriver.Chrome()
    #最大化浏览器
    driver.maximize_window()
    #打开商城登录地址
    Shoploginadress = table.cell(183,5).value
    driver.get(Shoploginadress)
    #输入用户名
    driver.find_element_by_xpath("//*[@id='my-form']/div[1]/div/input").send_keys(ShopuserName)
    #输入密码
    driver.find_element_by_xpath("//*[@id='my-form']/div[2]/div/input").send_keys(ShoppassWord)
    #点击登录
    driver.find_element_by_xpath("//*[@id='my-form']/div[3]/button[1]/span").click()
    time.sleep(3)
    #进入营销管理页面
    driver.implicitly_wait(30)
    driver.find_element_by_xpath("//*[@id='subapp']/header/div/nav/ul/li[4]/a/p").click()
    time.sleep(1)
    #点击新增套餐按钮
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[1]/a[2]/button").click()
    time.sleep(1)
    #在新增优惠券页面输入名称：
    CouponsName =  u"满100减99.99_" + str(datetime.datetime.now())
    print "CouponsName:",CouponsName
    ws.write(236,5,CouponsName)
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[1]/div/div/input").send_keys(CouponsName)
    time.sleep(1)
    #选择领取日期
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[2]/div/div[1]/input").send_keys("2018-01-01 00:00:00")
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("2038-01-01 00:00:00")
    time.sleep(1)
    #选择有效期
    StartValidity = (datetime.datetime.now() + datetime.timedelta(minutes=0)).strftime("%Y-%m-%d %H:%M:%S")
    print "StartValidity:",StartValidity
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[3]/div/div[1]/input").send_keys(StartValidity)
    time.sleep(1)
    EndValidity = (datetime.datetime.now() + datetime.timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M:%S")
    print "EndValidity:",EndValidity
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[3]/div/div[2]/input").send_keys(EndValidity)
    time.sleep(1)
    #点击无效区域关闭时间控件
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[9]/div/p[2]").click()      
    #输入面额
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[4]/div/div/input").send_keys("99.99")
    time.sleep(1)
    #输入可发放总数
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[5]/div/div/input").send_keys("1")
    time.sleep(1)
    #选择每人限领
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[6]/div/div/div/input").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[1]").click()
    #消费金额为2000
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[7]/div/div/input").send_keys("100")
    time.sleep(1)
    #代金券描述：
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[8]/div/div/textarea").send_keys(u"满100减99.9白送")
    time.sleep(1)
    #上传图片
    upload = driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[9]/div/div/label/span").click()
    time.sleep(5)
    #win32gui 
    #上传文件对话框 
    uploadwindow = win32gui.FindWindow('#32770', u"打开")
    print "uploadwindow:",uploadwindow 
    #这段代码是先定位到最上层的父窗口，再逐层定位到输入框（chrome于FF有所不同，FF下可以直接定位）
    parent=win32gui.FindWindowEx(uploadwindow,None,'ComboBoxEx32',None)
    Combobox_real=win32gui.FindWindowEx(parent,None,'ComboBox',None)
    Edit_box=win32gui.FindWindowEx(Combobox_real,None,'Edit',None)
    win32gui.SetForegroundWindow(Edit_box)
    time.sleep(1)
    #往输入框输入绝对地址
    win32gui.SendMessage(Edit_box,win32con.WM_SETTEXT,None,r'C:\Users\Lenovo\Pictures\AutoCasePic\CouponsPictrue.png')
    openbuttonname = u'打开(&O)'
    time.sleep(1)
    #定位“打开”按钮
    openbutton = win32gui.FindWindowEx(uploadwindow, None,"Button",openbuttonname)
    print "openbutton:",openbutton
    win32gui.PostMessage(openbutton, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
    win32gui.PostMessage(openbutton, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)
    time.sleep(3)
    #提交
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[10]/button").click()
    time.sleep(5)
    #查看代金券管理页面是否新增成功
    CouponsName1 = driver.find_element_by_xpath("//*[@id='main']/div[2]/div[3]/div/div[3]/table/tbody/tr[1]/td[1]/div").text
    print "CouponsName1:",CouponsName1
    if (CouponsName == CouponsName1):
        print u"发布代金券成功！！"
    else:
        print u"发布代金券失败！！" 
    #等待两分钟,刷新页面,查看代金券状态
    for i in range(1,12):
        print u"等待优惠券过期中,请稍候..."
        time.sleep(10)
    #刷新页面，查看优惠券状态
    driver.refresh()
    time.sleep(5) 
    couponsStatus = driver.find_element_by_xpath("//*[@id='main']/div[2]/div[3]/div/div[3]/table/tbody/tr/td[5]/div").text
    print "couponsStatus:",couponsStatus
    if(couponsStatus == u"无效"):
        print u"优惠券已经失效！！！"
        #如果成功,重置错误原因为空
        ws.write(231,10,"")
        print (u"Case--AmezMallUI_015_CouponExpired优惠券过期---结果：Pass!")
        ws.write(231,7, 'Pass')
    else:
        print u"优惠券没有失效！！！"
        print (u"Case--AmezMallUI_015_CouponExpired优惠券过期---结果：Failed!")
        ws.write(231,7, 'Failed',style2)
        ws.write(231,10,u"优惠券没有失效",style2)
    errorFlag = 1
    
except Exception as e:
    print(e)
    #抛出异常
    traceback.format_exc()
    #写入异常至用例文件中：
    errorInfo = str(traceback.format_exc())
    print "****errorInfo:",errorInfo
    ws.write(231,10,errorInfo,style2)
    
finally :
    if(errorFlag == 0):
        print (u"Case--AmezMallUI_015_CouponExpired优惠券过期---结果：Failed!")
        ws.write(231,7, 'Failed',style2)
    ws.write(231,9, 'zhouchuqi')
    ws.write(231,8, datetime.datetime.now(), style1)    
    #利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
    wb.save('E:\\gitworksqace\\mrbdome1\\test1\\amez_test\\UITestData.xls')
    #退出浏览器
    driver.quit()
    print u"****Case--AmezMallUI_015_CouponExpired优惠券过期--结束运行****"