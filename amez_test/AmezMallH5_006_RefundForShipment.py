#-*- coding:utf-8 -*-
#!/usr/bin/env python
#*************************************
#*******待发货订单退款，商家同意*********
#*************************************
#导入依赖模块
import xlrd,xlwt
import time
from selenium import webdriver
from xlutils.copy import copy
from datetime import datetime
import sys
import re
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
print u"****Case--AmezMallH5_006_RefundForShipment待发货订单退款，商家同意--开始运行****"

try:
    print u"会员登录购买商品！"
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
    el=driver.find_element_by_xpath("//*[@id='app']/div/div[19]/section/div/a[5]/p")
    driver.execute_script("arguments[0].click();", el)
    time.sleep(2)
    #跳转至登录页面输入用户名密码,登录 
    driver.find_element_by_xpath("//*[@id='accountLogin']/div[2]/div[1]/input").send_keys(userName)
    driver.find_element_by_xpath("//*[@id='accountLogin']/div[2]/div[2]/input").send_keys(passWord,Keys.ENTER)
    time.sleep(2)
    #搜索框输入要搜索的商品
    ReadGoods = table.cell(27,5).value
    #点击搜索栏进入搜索页面
    driver.find_element_by_xpath("//*[@id='app']/div/div[1]/input").click()
    time.sleep(1)
    #输入要搜索的商品
    driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[1]/form/input").send_keys(ReadGoods,Keys.ENTER)
    time.sleep(3)
    #查看被搜索出来的商品第一条
    SearchGoods = driver.find_element_by_xpath("//*[@id='app']/div/section[2]/ul/li[1]/div[2]/div[1]").text
    print "SearchGoods:",SearchGoods
    if (SearchGoods == u"小米（MI）小米电视4X 55英寸 L55M5-AD 2GB+8GB HDR 4K超高清 蓝牙语音遥"):
        print u"搜索商品成功，搜索出的第一条商品为：",SearchGoods
        #点击商品进入商品详情
        driver.find_element_by_xpath("//*[@id='app']/div/section[2]/ul/li[1]/div[2]/div[1]").click()
        time.sleep(2)
        #点击立即购买
        #JS点击立即购买按钮
        js = 'document.getElementsByClassName("ljgm")[0].click();'
        driver.execute_script(js)
        time.sleep(2)
        #选择规格
        #小米电视4
        el=driver.find_element_by_xpath("//*[@id='app']/div/section[8]/section/div[2]/div[1]/div/span[1]")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(1)
        #75英寸
        el=driver.find_element_by_xpath("//*[@id='app']/div/section[8]/section/div[2]/div[2]/div/span[1]")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(1)
        #点击确定
        js = 'document.getElementsByClassName("but_full_square_outer")[0].click();'
        driver.execute_script(js)
        time.sleep(3)
        #确认订单页面点击提交订单
        el=driver.find_element_by_xpath("//*[@id='app']/div/section[6]/button")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(3)
        #收银台页面选择余额支付
        el=driver.find_element_by_xpath("//*[@id='app']/div/div[1]/section/ul/li[4]/label/span[1]/i[1]")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(1)
        #确定
        el=driver.find_element_by_xpath("//*[@id='app']/div/div[1]/section/a")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(2)
        #输入支付密码
        el=driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[3]/ul/li[1]")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(0.5)
        el=driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[3]/ul/li[2]")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(0.5)
        el=driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[3]/ul/li[3]")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(0.5)
        el=driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[3]/ul/li[4]")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(0.5)
        el=driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[3]/ul/li[5]")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(0.5)
        el=driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[3]/ul/li[6]")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(5)
        #待支付成功后，关掉弹框，查看订单
        el=driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div/span")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(1)
        #点击查看订单
        el=driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div[3]/div[1]")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(3)
        #在待发货页面，申请退款
        OrderGoods = driver.find_element_by_xpath("//*[@id='app']/div/div/section[1]/div[2]/ul/li/div[2]/p[1]").text
        OrderStatus = driver.find_element_by_xpath("//*[@id='app']/div/div/section[1]/div[1]/span").text
        print "OrderGoods:",OrderGoods
        print "OrderStatus",OrderStatus
        if (OrderGoods == u"小米（MI）小米电视4X 55英寸 L55M5-AD 2GB+8GB HDR 4K超高清 蓝牙语音遥" and OrderStatus == u"待发货"):
            print u"订单支付成功！！！"
            #点击商品进入订单详情页面
            el=driver.find_element_by_xpath("//*[@id='app']/div/div/section[1]/div[2]/ul/li/div[2]/p[1]")
            driver.execute_script("arguments[0].click();", el)
            time.sleep(2)
            #保存订单编号
            OrderNumber = str(driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section[3]/div[3]/p/span[1]").text)
            print "OrderNumber:",OrderNumber
            #提取出订单编号 
            OrderNumber = re.findall(r"订单编号：(.*)", OrderNumber)
            #将提取出的List类型转化为str类型
            OrderNumber = ''.join(OrderNumber)
            print "提取后的OrderNumber:",OrderNumber
            ws.write(88,5,OrderNumber)
            #申请退款
            el=driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section[2]/div[2]/ul/li/div[2]/div/div/span/a")
            driver.execute_script("arguments[0].click();", el)
            time.sleep(2)
            #选择货物状态--仅退款
            el=driver.find_element_by_xpath("//*[@id='moneyBack']/div[2]/span[2]")
            driver.execute_script("arguments[0].click();", el)
            time.sleep(1)
            el=driver.find_element_by_xpath("//*[@id='radio' and @value='0']")
            driver.execute_script("arguments[0].click();", el)
            time.sleep(1)
            el=driver.find_element_by_xpath("//*[@id='moneyBack']/section/div[2]/div[2]")
            driver.execute_script("arguments[0].click();", el)
            time.sleep(1)
            #选择退款原因--不喜欢/不想要
            el=driver.find_element_by_xpath("//*[@id='moneyBack']/div[3]/span[2]")
            driver.execute_script("arguments[0].click();", el)
            time.sleep(1)
            el=driver.find_element_by_xpath("//*[@id='radio' and @value='10']")
            driver.execute_script("arguments[0].click();", el)
            time.sleep(1)
            el=driver.find_element_by_xpath("//*[@id='moneyBack']/section/div[2]/div[2]")
            driver.execute_script("arguments[0].click();", el)
            time.sleep(1)
            #填写退款说明
            driver.find_element_by_xpath("//*[@id='moneyBack']/textarea").send_keys(u"突然不想要了！！！")
            time.sleep(1)
            #确定
            el=driver.find_element_by_xpath("//*[@id='moneyBack']/div[8]/span")
            driver.execute_script("arguments[0].click();", el)
            time.sleep(5)
            #待提交成功，验证按钮是否变成退款中
            ButtonStatus = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section[2]/div[2]/ul/li/div[2]/div/div/span/a").text
            print u"退款申请提交后，按钮状态变为：",ButtonStatus
            if (ButtonStatus == u"退款中"):
                print u"退款申请成功，请等待商家处理！！！"
            else:
                print u"退款申请失败！！！"
    #关闭浏览器
    driver.quit()
    
#商家用户登录处理退款请求
    print u"\n---***商家用户登录处理退款请求***---"
    #读取用户名
    ShopuserName = table.cell(66,5).value
    print ShopuserName
    #读取密码
    ShoppassWord = table.cell(67,5).value
    print ShoppassWord
    #打开谷歌浏览器
    driver = webdriver.Chrome()
    #最大化浏览器
    driver.maximize_window()
    #打开商城登录地址
    Shoploginadress = table.cell(65,5).value
    driver.get(Shoploginadress)
    #输入用户名
    driver.find_element_by_xpath("//*[@id='my-form']/div[1]/div/input").send_keys(ShopuserName)
    #输入密码
    driver.find_element_by_xpath("//*[@id='my-form']/div[2]/div/input").send_keys(ShoppassWord)
    #点击登录
    driver.find_element_by_xpath("//*[@id='my-form']/div[3]/button[1]/span").click()
    time.sleep(3)
    driver.implicitly_wait(30)
    #进入退款处理页面
    driver.find_element_by_xpath("//*[@id='subapp']/header/div/nav/ul/li[6]/a/p").click()
    #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(2) 
    #获取订单编号 
    OrderNumber1 = driver.find_element_by_xpath("//*[@id='main']/div[2]/div[3]/div/div[3]/table/tbody/tr[1]/td[1]/div/div/ul/li[2]/p[2]/span[2]").text
    print u"商家退款记录页面第一条订单号为:",OrderNumber1
    if (OrderNumber1 == OrderNumber):
        print u"订单正确！！！"
    #点击处理
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[3]/div/div[3]/table/tbody/tr[1]/td[6]/div/button/span").click()
    #点击同意并填写备注信息
    driver.find_element_by_xpath("//*[@id='main']/div[2]/ul/li[1]/div[2]/div[1]/label[1]/span[2]").click()
    driver.find_element_by_xpath("//*[@id='main']/div[2]/ul/li[1]/div[2]/div[2]/div/textarea").send_keys(u"买家不想要了！！！")
    #点击提交意见
    driver.find_element_by_xpath("//*[@id='main']/div[2]/ul/li[1]/div[3]/button[1]/span").click()
    time.sleep(5)
    #待提交完成，查看处理状态
    #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(2) 
    OrderStatus1 = driver.find_element_by_xpath("//*[@id='main']/div[2]/ul/li[1]/div[2]/p[1]/span[2]").text
    RefundNumber = driver.find_element_by_xpath("//*[@id='main']/div[2]/ul/li[1]/div[1]/p[1]/span[2]").text
    #保存退款编号
    ws.write(99,5,RefundNumber)
    print u"商家处理退款申请结果为：",OrderStatus1
    if (OrderStatus1 == u"同意"):
        print u"商家同意退款！！"
    #关闭浏览器
    driver.quit()
    
#买家进入售后退款页面查看订单状态是否为退款成功：
    print u"\n---***买家进入售后退款页面查看订单状态是否为退款成功***---"
    #定义H5机型
    mobile_emulation = {'deviceName': 'iPhone X'}
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
    time.sleep(2)
    #点击我的---售后退款
    el=driver.find_element_by_xpath("//*[@id='app']/div/div[19]/section/div/a[5]/p")
    driver.execute_script("arguments[0].click();", el)
    time.sleep(2)
    el=driver.find_element_by_xpath("//*[@id='app']/div/div[2]/ul/li[5]")
    driver.execute_script("arguments[0].click();", el)
    time.sleep(2)
    #售后退款页面点击第一条订单,进入订单详情页面
    el=driver.find_element_by_xpath("//*[@id='app']/div/ul/li[1]/div/a/div[2]/p[1]")
    driver.execute_script("arguments[0].click();", el)
    time.sleep(3)
    #读取退款编号 
    RefundNumber1 = str(driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div[2]/p/span[5]").text)
    print "RefundNumber1:",RefundNumber1
    #提取出订单编号 
    RefundNumber1 = re.findall(r"退款编号：(.*)", RefundNumber1)
    #将提取出的List类型转化为str类型
    RefundNumber1 = ''.join(RefundNumber1)
    print "提取后的RefundNumber1:",RefundNumber1
    #查看订单状态：
    OrderStatus2 = driver.find_element_by_xpath("//*[@id='app']/div/div[1]/h4").text
    print u"退款申请状态为：",OrderStatus2
    if (RefundNumber1 == RefundNumber and OrderStatus2 == u"卖家已同意，退款成功"):
        print u"买家申请退款成功！！！"
        #保存退款编号
        ws.write(102,5,RefundNumber1)
        #保存退款状态
        ws.write(103,5,OrderStatus2)
        print (u"Case--AmezMallH5_006_RefundForShipment待发货订单退款，商家同意---结果：Pass!")
        ws.write(74,7, 'Pass')
        #如果成功，将错误日志覆盖
        ws.write(74,10,'')
    else:
        print u"买家申请退款失败！！！"
        print (u"Case--AmezMallH5_006_RefundForShipment待发货订单退款，商家同意---结果：Fail!")
        ws.write(74,7, 'Failed',style2)  
        ws.write(74,10, u'买家申请退款失败',style2)
    #将失败标志置为1，表示脚本执行完成           
    errorFlag = 1
    
except Exception as e:
    print(e)
    #抛出异常
    traceback.format_exc()
    #写入异常至用例文件中：
    errorInfo = str(traceback.format_exc())
    print "****errorInfo:",errorInfo
    ws.write(74,10,errorInfo,style2)
    
finally :
    if(errorFlag == 0):
        print u"Case--AmezMallH5_006_RefundForShipment待发货订单退款，商家同意--结果：Failed!"
        ws.write(74,7, 'Failed',style2)
    #写入执行人员
    ws.write(74,9, 'zhouchuqi')
    #写入执行日期
    ws.write(74,8, datetime.now(), style1)    
    #利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
    wb.save('E:\\gitworksqace\\mrbdome1\\test1\\amez_test\\H5TestData.xls')
    #退出浏览器
    driver.quit()
    print u"Case--AmezMallH5_006_RefundForShipment.py运行结束！！！"