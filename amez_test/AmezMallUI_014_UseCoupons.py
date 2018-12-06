#-*- coding:utf-8 -*-
#!/usr/bin/env python
#*********************************************
#*******买家使用优惠券--依赖上一脚本*************
#*********************************************
#导入依赖模块
import xlrd,xlwt
import time
from selenium import webdriver
from xlutils.copy import copy
from datetime import datetime
import sys
from lib2to3.tests.support import driver
from cgitb import text
# from Scripts.runxlrd import result
# from pip._vendor.retrying import Attempt
from selenium.common.exceptions import StaleElementReferenceException
reload(sys)
sys.setdefaultencoding('utf-8')
import traceback
import win32gui
import win32con
from selenium.webdriver.support.ui import Select
#导入商家发布优惠券脚本
# execfile('AmezMallUI_013_ReceivesCoupons.py')

#打开用例文件，读取对应用例的用户名等数据
casefile = xlrd.open_workbook('E:\\gitworksqace\\mrbdome1\\test1\\amze_test\\UITestData.xls', formatting_info=True)
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
print u"****Case--AmezMallUI_014_UseCoupons买家使用优惠券--开始运行****"

try:
    errorFlag = 0
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
    CouponsName =  u"满1024减1000_" + str(datetime.now())
    print "CouponsName:",CouponsName
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[1]/div/div/input").send_keys(CouponsName)
    time.sleep(1)
    #选择领取日期
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[2]/div/div[1]/input").send_keys("2018-01-01 00:00:00")
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("2038-01-01 00:00:00")
    time.sleep(1)
    #选择有效期
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[3]/div/div[1]/input").send_keys("2018-01-01 00:00:00")
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[3]/div/div[2]/input").send_keys("2038-01-01 00:00:00")
    time.sleep(1)
    #点击无效区域关闭时间控件
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[9]/div/p[2]").click()      
    #输入面额
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[4]/div/div/input").send_keys("1000")
    time.sleep(1)
    #输入可发放总数
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[5]/div/div/input").send_keys("1")
    time.sleep(1)
    #选择每人限领
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[6]/div/div/div/input").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[1]").click()
    #消费金额为2000
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[7]/div/div/input").send_keys("1024")
    time.sleep(1)
    #代金券描述：
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[8]/div/div/textarea").send_keys(u"满1024减1000")
    time.sleep(1)
    #上传图片
    upload = driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[9]/div/div/label/span").click()
    time.sleep(5)
    #win32gui 
    # 对话框 
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
    time.sleep(3)
    #关闭浏览器
    driver.quit()

#买家登录领取并使用优惠券    
    print "\n---***买家登录领取并使用优惠券***---"
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
    searchtext = table.cell(206,5).value
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
                pass
            Attempts += 1
        return result
    #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    sreach_window=driver.current_window_handle[1]
    time.sleep(2)
    textMi = retryingFindClick("//*[@id='am_content']/div/div[2]/div[3]/div[2]/div[2]/ul/li[1]/a/div/div[1]")
    print "textMi:",textMi
    readMi = table.cell(219,5).value
    print "readMi:",readMi
    if (textMi == readMi):
        print u"会员搜索商品成功！！"
    else:
        print u"会员搜索商品失败！！"
    #点击商品进入商品详情页面
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[3]/div[2]/div[2]/ul/li[1]/a/div/div[1]").click()
    time.sleep(1)
    #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(2)
    #遍历所有可领取的优惠券
    for i in range(0,100):
            CouponsList = driver.find_elements_by_class_name("row")[i].text
            print "CouponsList:",CouponsList
            if (u"满1024减1000_" in CouponsList):
                print u"存在可用的优惠券：",CouponsList
                #确定此优惠券位于第几行
                print u"优惠券位于第%d行" % int(i+1)
                break
    #点击对应领取按钮
    el = driver.find_elements_by_class_name("row")[i].find_element_by_link_text("领取")
    driver.execute_script("arguments[0].click();", el)
    time.sleep(5)
    #点击立即购买
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[1]/div[1]/div[2]/div[9]/button[2]").click()
    #进入订单确认页面
    #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(2)
    #填写买家留言
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[2]/ul/li[1]/input").send_keys(u"请保证好质量尽快发货！")
    time.sleep(1)
    #获取商品实价
    GoodsPrice = driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[1]/ul/li/ul/li[4]").text
    print u"此商品的实价为:",GoodsPrice
    #查看所有可用优惠券
    CouponsList = driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[2]/ul/li[2]/select")
    #选择对应的优惠券
    Select(CouponsList).select_by_visible_text(u"使用 满1024.00减1000.00 减免 1000.00 元")
    #获取应付金额
    AmountPayable = driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[2]/div/p[2]/span").text
    print u"使用优惠券后的应付金额为:",AmountPayable
    if (AmountPayable == "￥1299.00"):
        print u"优惠券使用后减少1000应付金额，实付为：",AmountPayable
    else:
        print u"没有可用的优惠券！！！"
    #提交订单
    driver.find_element_by_xpath("//*[@id='footer_total']/div/div/button").click()
    #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(2)
    #选择支付方式为余额支付
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[3]/div[1]/span[3]").click()
    changeBalance = driver.find_element_by_xpath("//*[@id='am_content']/div/div[3]/div[1]/span[2]").text
    print u"零钱余额为：",changeBalance   
    #输入支付密码
    driver.find_element_by_xpath("//*[@id='ids_undefined']/input[1]").send_keys("1")
    driver.find_element_by_xpath("//*[@id='ids_undefined']/input[2]").send_keys("2")
    driver.find_element_by_xpath("//*[@id='ids_undefined']/input[3]").send_keys("3")
    driver.find_element_by_xpath("//*[@id='ids_undefined']/input[4]").send_keys("4")
    driver.find_element_by_xpath("//*[@id='ids_undefined']/input[5]").send_keys("5")
    driver.find_element_by_xpath("//*[@id='ids_undefined']/input[6]").send_keys("6")
    #确认支付
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[4]/div/button").click()
    time.sleep(1)
    #支付完成后关闭弹出的窗口
    #进入在线支付页面，确认当前窗口句柄
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[3]/div[2]/div[1]/span").click()
    #进入在线支付页面，确认当前窗口句柄
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(1)
    Successfulpayment = driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]").text
    print Successfulpayment
    if (Successfulpayment == u"支付成功"):
        print u"订单支付成功"
    #点击查看订单，此订单出现在订单列表第一行
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/a").click()
    time.sleep(2)
    #进入会员中心--我的优惠券--已使用页面查看第一条是否为刚才使用的优惠券
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[1]/div/div/div[3]/ul/li[2]/a").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div/ul/li[2]").click()
    time.sleep(2)
    #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(2)
    #我的优惠券--已使用页面查看第一条是否为刚才使用的优惠券
    CouponsName = driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div/div[1]/ul/li[1]/div[1]/div[2]").text
    if(CouponsName == u"满1024元使用"):
        print u"优惠券使用成功！"
        ws.write(212,7, 'Pass')
        #如果成功，将错误日志覆盖
        ws.write(212,10,'')
    else:
        print u"优惠券使用不成功！"
        ws.write(212,7, 'Failed',style2)
        ws.write(212,10, u'优惠券使用不成功！',style2)
        
    #回滚数据，将商家发布的优惠券置为无效
    #新开窗口,商家登录
    NewWindow = 'window.open("http://company.test.amyun.cn");'
    driver.execute_script(NewWindow)
    print u"\n---***商家用户登录回滚数据，将优惠券置为无效！***---"
    #读取用户名
    ShopuserName = table.cell(129,5).value
    print ShopuserName
    #读取密码
    ShoppassWord = table.cell(130,5).value
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
    #点击营销管理
    driver.find_element_by_xpath("//*[@id='subapp']/header/div/nav/ul/li[4]/a/p").click()
    time.sleep(2)
    #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(2)
    #将优惠券置为无效
    couponsStatus = driver.find_element_by_xpath("//*[@id='main']/div[2]/div[3]/div/div[3]/table/tbody/tr/td[5]/div").text
    if (couponsStatus == u"使用中"):
        print u"此优惠券现在的状态为:",couponsStatus
        #将状态置为无效,点击无效按钮
        driver.find_element_by_xpath("//*[@id='main']/div[2]/div[3]/div/div[3]/table/tbody/tr[1]/td[6]/div/button[2]/span").click()
    #刷新页面，查看优惠券状态
    driver.refresh()
    time.sleep(5) 
    couponsStatus1 = driver.find_element_by_xpath("//*[@id='main']/div[2]/div[3]/div/div[3]/table/tbody/tr/td[5]/div").text
    print u"此优惠券候为无效后的状态为:",couponsStatus1
    print u"优惠券已经被置为无效状态！！！"
    
    errorFlag = 1

except Exception as e:
    print(e)
    #抛出异常
    traceback.format_exc()
    #写入异常至用例文件中：
    errorInfo = str(traceback.format_exc())
    print "****errorInfo:",errorInfo
    ws.write(212,10,errorInfo,style2)
        
finally :
    if(errorFlag == 0):
        print (u"Case--AmezMallUI_014_UseCoupons买家使用优惠券--结果：Failed!")
        ws.write(212 ,7, 'Failed',style2)
    ws.write(212,9, 'zhouchuqi')
    ws.write(212,8, datetime.now(), style1)    
    #利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
    wb.save('E:\\gitworksqace\\mrbdome1\\test1\\amze_test\\UITestData.xls')
    #退出浏览器
    driver.quit()
    print u"Case--AmezMallUI_014_UseCoupons买家使用优惠券.py运行结束！！！"