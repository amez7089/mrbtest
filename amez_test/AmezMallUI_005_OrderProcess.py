#-*- coding:utf-8 -*-
#!/usr/bin/env python
#*********************************************
#*******订单完整流程--依赖上一脚本***************
#*********************************************
#导入依赖模块
import xlrd,xlwt
import time
# from selenium.webdriver.support.ui import  WebDriverWait
from selenium import webdriver
from xlutils.copy import copy
from datetime import datetime
from selenium.common.exceptions import StaleElementReferenceException
import sys
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
print u"****Case--AmezMallUI_005_OrderProcess订单完整流程 --开始运行****"

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
    #点击左上角的会员中心标签进入会员中心    
    driver.find_element_by_xpath("//*[@id='app']/div[1]/div/ul/li[2]/div[1]").click()
    time.sleep(1)
    #点击全部订单标签进入订单页面
    #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[1]/div/div/div[1]/ul/li/a").click() 
    time.sleep(1) 
    orderGoodName = driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/dl[1]/dd/p[1]").text
    print u"订单页面商品为：",orderGoodName
    #订单列表中的商品名称：
    readMi = table.cell(49,5).value
    if (orderGoodName == readMi):
        print u"订单列表中的商品正确！"
    else:
        print u"订单列表中的商品不是我们需要的！" 
    #关闭浏览器
    driver.quit()
    
    #商家用户登录商家端查看订单并发货
    print u"\n---***商家用户登录商家端查看订单并发货***---"
    #读取用户名
    ShopuserName = table.cell(51,5).value
    print ShopuserName
    #读取密码
    ShoppassWord = table.cell(52,5).value
    print ShoppassWord
    #打开谷歌浏览器
    driver = webdriver.Chrome()
    #最大化浏览器
    driver.maximize_window()
    #打开商城登录地址
    Shoploginadress = table.cell(50,5).value
    driver.get(Shoploginadress)
    #输入用户名
    driver.find_element_by_xpath("//*[@id='my-form']/div[1]/div/input").send_keys(ShopuserName)
    #输入密码
    driver.find_element_by_xpath("//*[@id='my-form']/div[2]/div/input").send_keys(ShoppassWord)
    #点击登录
    driver.find_element_by_xpath("//*[@id='my-form']/div[3]/button[1]/span").click()
    time.sleep(3)
    #进入待发货页面，查看订单
    #等待登录成功
#     wait = WebDriverWait(driver,100)
#     wait.until(lambda driver: driver.find_element_by_xpath("//*[@id='layui-layer3']/div[3]").find_element_by_class_name("layui-layer-btn1"))
    driver.implicitly_wait(30)
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/ul/li[3]/div/ul/li[2]/div/a/button").click()
    time.sleep(1)
    #查看待发货订单页面第一条是不是我们需要的商品
    orderXiaoMi = driver.find_element_by_xpath("//*[@id='main']/div[2]/div/div[6]/div[2]/div/ul/li[1]/div/div[2]/p[1]/a").text 
    print u"待发货订单页面第一行为：",orderXiaoMi
    if (orderXiaoMi == readMi):
        #点击发货按钮，进入发货页面
        driver.find_element_by_xpath("//*[@id='main']/div[2]/div/div[6]/div[2]/div/ul/li[5]/button").click()
        time.sleep(1)
        #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
        for handle in driver.window_handles:
            driver.switch_to_window(handle)
        time.sleep(2)
        #填写发货备忘
        driver.find_element_by_xpath("//*[@id='orderList']/div/div[2]/div/div[2]/div/textarea").send_keys(u"已安排发货！")
        #填写物流单号
        trackingNumber = table.cell(56,5).value
        print u"物流单号为：",trackingNumber
        driver.find_element_by_xpath("//*[@id='main']/div[2]/div/div[7]/div[3]/table/tbody/tr/td[2]/div/div/input").send_keys(trackingNumber)
        #点击确认发货
        driver.find_element_by_xpath("//*[@id='main']/div[2]/div/div[7]/div[3]/table/tbody/tr/td[3]/div/button/span").click()
        print u"已经发货完成，运单号为：",trackingNumber
    #进入发货中页面，查看是否有订单是发货中
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div/ul[1]/li[2]").click()
    time.sleep(1)
    orderXiaoMi1 = driver.find_element_by_xpath("//*[@id='main']/div[2]/div/div[2]/div/div[2]/ul/li/div[2]/a").text
    if (orderXiaoMi1 == readMi):
        print u"发货中页面存在该订单：",orderXiaoMi1
    #关闭浏览器
    driver.quit()
    
    print u"\n---***买家进入订单页面点击确认收货***---"
    #打开谷歌浏览器
    driver = webdriver.Chrome()
    #最大化浏览器
    driver.maximize_window()
    #买家进入订单页面点击确认收货
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
    #待收货页面查看是否有待收货订单
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[3]/div[1]/ul/li[3]/p/span[1]").click()
    #查看待收货页面第一条数据是否为我们需要的订单
    #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(2)
    orderGoodName2 = driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/dl[1]/dd/p[1]").text
    if (orderGoodName2 == readMi):
        print u"待收货页面第一条订单正确:",orderGoodName2
        #点击确认收货
        driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[2]/ul/li[2]/div/div/div/button[1]").click()
        time.sleep(1)
        #弹出确认对话框，点击确认
        driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[2]/ul/li[2]/div/div[2]/div[2]/div[2]/div/button[1]").click()
        #等待页面弹窗提示完成
        time.sleep(1)
    else:
        print u"待收货页面第一条订单错误:",orderGoodName2
    #进入待评价页面，查看是否有待评价订单
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[2]/ul/li[5]/span[1]").click()
    #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(2)
    orderGoodName3 = driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/dl[1]/dd/p[1]").text
    if (orderGoodName3 == readMi):
        print u"待评价页面第一条订单正确：",orderGoodName3
        #点击评价按钮输入评价内容
        driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[2]/ul/li[2]/div/div/div/button[1]").click()
        #选择好评
        evaluation = table.cell(58,5).value
        evaluation1 = evaluation + str(datetime.now())
#         print type(evaluation1)
        print u"合并后为:evaluation",evaluation1
        #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
        for handle in driver.window_handles:
            driver.switch_to_window(handle)
        time.sleep(2)
        driver.find_element_by_id("ping1").click()
        driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/textarea").send_keys(evaluation1)
        #发表评价
        driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[3]/div[2]/button").click()
    time.sleep(2)    
    #查看评价是否成功
    #进入商城首页，搜索商品，跳至评价页面，第一条是否是刚才提交的评价
    driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div/a[1]").click()
    #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(2)
    #搜索栏中输入指定文字进行商品搜索
    searchtext = table.cell(31,5).value
    print  u"搜索文本为：",searchtext
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[1]/div[1]/div[2]/div[2]/div/input").send_keys(searchtext)
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[1]/div[1]/div[2]/div[2]/button").click()
    #因为在点击时页面刷新，导致元素找不到，所以此函数作用是当找不到元素时，再次获取   
    def retryingFindClick(by):
        result = False
        Attempts = 0
        while Attempts < 5:
            try:
                result = driver.find_element_by_xpath(by).text
                break
            except StaleElementReferenceException,e:
                print (e)
                pass
            Attempts += 1
        return result
    #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    sreach_window=driver.current_window_handle[1]
    time.sleep(2)
    textMi = retryingFindClick("//*[@id='am_content']/div/div[2]/div[3]/div[2]/div[2]/ul/li[1]/a/div/div[1]")
    print u"搜索出的商品为：",textMi
    #读取商品名称
    readMi = table.cell(33,5).value
    if (textMi == readMi):
        print u"会员搜索商品成功！！"
    else:
        print u"会员搜索商品失败！！"
    #点击搜索到的商品，进入商品详情页面
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[3]/div[2]/div[2]/ul/li[1]/a/div/div[1]").click()
    time.sleep(1)
    #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(2)
    #点击评价标签
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div[2]/ul/li[2]").click()
    #获取第一条评价
    evaluation2 = driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div[2]/div/div/div/ul/li[1]/div[2]/div[1]").text
    if (evaluation2 == evaluation1):
        print u"评价成功！"
        print (u"Case--AmezMallUI_005_OrderProcess订单完整流程---结果：Pass!")
        ws.write(43,7, 'Pass')
        #如果成功，将错误日志覆盖
        ws.write(43,10,'')
    else:
        print u"评价失败！"
        print (u"Case--AmezMallUI_005_OrderProcess订单完整流程---结果：Fail!")
        ws.write(43,7, 'Failed',style2)  
        ws.write(43,10, u'评价失败',style2)  
    errorFlag = 1
    
except Exception as e:
    print(e)
    #抛出异常
    traceback.format_exc()
    #写入异常至用例文件中：
    errorInfo = str(traceback.format_exc())
    print "****errorInfo:",errorInfo
    ws.write(43,10,errorInfo,style2)
    
finally :
    if(errorFlag == 0):
        print (u"Case--AmezMallUI_005_OrderProcess订单完整流程---结果：Failed!")
        ws.write(43,7, 'Failed',style2)
    ws.write(43,9, 'zhouchuqi')
    ws.write(43,8, datetime.now(), style1)    
    #利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
    wb.save('E:\\gitworksqace\\mrbdome1\\test1\\amez_test\\UITestData.xls')
    #退出浏览器
    driver.quit()
    print u"****Case--AmezMallUI_005_OrderProcess订单完整流程--结束运行****"