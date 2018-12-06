#-*- coding:utf-8 -*-
#!/usr/bin/env python
#*********************************
#*******买家使用优惠券**************
#*********************************
#导入依赖模块
import xlrd,xlwt
import time
from selenium import webdriver
from xlutils.copy import copy
from datetime import datetime
import sys
from lib2to3.tests.support import driver
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium.webdriver.common.keys import Keys
import traceback
import win32gui
import win32con

#打开用例文件，读取对应用例的用户名等数据
casefile = xlrd.open_workbook('D:\\Python27\\TestData\\H5TestData.xls', formatting_info=True)
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
print u"****Case--AmezMallH5_013_UseCoupons买家使用优惠券--开始运行****"

try:
    errorFlag = 0
    print u"---***商家用户登录新增优惠券***---"
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
    #进入营销管理页面
    driver.find_element_by_xpath("//*[@id='subapp']/header/div/nav/ul/li[4]/a/p").click()
    time.sleep(1)
    #点击新增套餐按钮
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[1]/a[2]/button").click()
    time.sleep(1)
    #在新增优惠券页面输入名称：
    CouponsName =  u"满500减488_" + str(datetime.now())
    print "CouponsName:",CouponsName
    ws.write(336,5,CouponsName)
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
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[4]/div/div/input").send_keys("488")
    time.sleep(1)
    #输入可发放总数
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[5]/div/div/input").send_keys("1")
    time.sleep(1)
    #选择每人限领
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[6]/div/div/div/input").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[1]").click()
    #消费金额为:
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[7]/div/div/input").send_keys("500")
    time.sleep(1)
    #代金券描述：
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[8]/div/div/textarea").send_keys(u"满500减488")
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
    ws.write(338,5,CouponsName1)
    if (CouponsName == CouponsName1):
        print u"发布代金券成功！！"
    else:
        print u"发布代金券失败！！"
    time.sleep(3)
    #关闭浏览器
    driver.quit()
    
#买家登录领取优惠券
    #定义H5机型
    print u"\n买家登录领取优惠券"
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
    el=driver.find_element_by_xpath("//*[@id='app']/div/div[17]/section/div/a[5]/p")
    driver.execute_script("arguments[0].click();", el)
    time.sleep(2)
    #跳转至登录页面输入用户名密码,登录 
    driver.find_element_by_xpath("//*[@id='accountLogin']/div[2]/div[1]/input").send_keys(userName)
    driver.find_element_by_xpath("//*[@id='accountLogin']/div[2]/div[2]/input").send_keys(passWord,Keys.ENTER)
    time.sleep(2)
    #搜索框输入要搜索的商品
    ReadGoods = table.cell(4,5).value
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
        time.sleep(3)
        #遍历所有可领取的优惠券
        for i in range(0,100):
                CouponsList = driver.find_elements_by_class_name("actTypeName")[i].text
                print "CouponsList:",CouponsList
                if (u"本店满500减488" in CouponsList):
                    print u"存在可用的优惠券：",CouponsList
                    #确定此优惠券位于第几行
                    print u"优惠券位于第%d行" % int(i+1)
                    break
        #点击对应领取按钮
        el = driver.find_elements_by_class_name("button")[i]
        driver.execute_script("arguments[0].click();", el)
        time.sleep(2)
        #进入优惠券列表页面，查看所有可领取优惠券
        for j in range(0,100):
            CouponsList1 = driver.find_element_by_xpath("//*[@id='app']/div/section[10]/div[2]/ul").find_elements_by_tag_name("li")[j].text
            print "CouponsList1:",CouponsList1
            if ("满500减488" in CouponsList1):
                print "找到需要领取的优惠券！！！位于第%d行！！！" % int(j+1)
                break
        #点击对应行的立即领取按钮
        el = driver.find_elements_by_class_name("receive")[j]
        driver.execute_script("arguments[0].click();", el)
        time.sleep(2)
        #确定
        el=driver.find_element_by_xpath("//*[@id='app']/div/section[10]/div[2]/div")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(2)
        #关闭浏览器
        driver.quit()
            
#买家进入我的--优惠券页面查看优惠券是否存在
    print u"买家查看优惠券是否领取成功！\n"
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
    el=driver.find_element_by_xpath("//*[@id='app']/div/div[17]/section/div/a[5]/p")
    driver.execute_script("arguments[0].click();", el)
    time.sleep(2)
    #跳转至登录页面输入用户名密码,登录 
    driver.find_element_by_xpath("//*[@id='accountLogin']/div[2]/div[1]/input").send_keys(userName)
    driver.find_element_by_xpath("//*[@id='accountLogin']/div[2]/div[2]/input").send_keys(passWord,Keys.ENTER)
    time.sleep(2)
    #进入我的--优惠券页面查看
    el=driver.find_element_by_xpath("//*[@id='app']/div/div[17]/section/div/a[5]/p")
    driver.execute_script("arguments[0].click();", el)
    time.sleep(2)
    el=driver.find_element_by_xpath("//*[@id='app']/div/div[4]/ul/li[5]/p[2]")
    driver.execute_script("arguments[0].click();", el)
    time.sleep(2)
    #查看第一行是否存在刚才领的优惠券
    couponsName3 = driver.find_element_by_xpath("//*[@id='coupons']/div[3]/ul/li/div/div/p[2]").text
    if (couponsName3==u"满500可使用"):
        print u"优惠券领取成功，状态为待使用！"
    else:
        print u"优惠券领取失败，不存在刚才领取的优惠券！"
    #关闭浏览器
    driver.quit()
    
#买家登录使用优惠券购买商品
    print u"\n买家登录使用优惠券购买商品!!!"
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
    el=driver.find_element_by_xpath("//*[@id='app']/div/div[17]/section/div/a[5]/p")
    driver.execute_script("arguments[0].click();", el)
    time.sleep(2)
    #跳转至登录页面输入用户名密码,登录 
    driver.find_element_by_xpath("//*[@id='accountLogin']/div[2]/div[1]/input").send_keys(userName)
    driver.find_element_by_xpath("//*[@id='accountLogin']/div[2]/div[2]/input").send_keys(passWord,Keys.ENTER)
    time.sleep(2)
    #搜索商品并使用优惠券购买
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
        #确认订单页面选择优惠券
        el=driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div[2]/div[2]/span[1]")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(2)
        #查看可用优惠券列表
        for i in range(1,100):
            CouponsList = driver.find_elements_by_class_name("discount_name")[i].text
            print "CouponsList:",CouponsList
            if ("满500.00减488.00" in CouponsList):
                print "存在可用的优惠券：",CouponsList
                #确定此优惠券位于第几行
                print "优惠券位于第%d行" % int(i+1)
                break
        print u"得到的行数为:",int(i+1)
        #选择此优惠券使用
        el = driver.find_elements_by_name("coupon")[i]
        driver.execute_script("arguments[0].click();", el)
        time.sleep(1)
        #确定
        el = driver.find_element_by_xpath("//*[@id='app']/div/section[4]/div[2]/button")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(2)  
        #提交订单
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
        #保存订单编号 
        el=driver.find_element_by_xpath("//*[@id='app']/div/div/section[1]/div[2]/ul/li/div[2]/p[1]")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(3)
        OrderNumber = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section[3]/div[3]/p/span[1]").text
        print "OrderNumber:",OrderNumber
        #将提取出的List类型转化为str类型
        OrderNumber = ''.join(OrderNumber)
        ws.write(343,5,OrderNumber)
    #退出浏览器
    driver.quit()
    
#买家进入我的--优惠券--已使用页面，查看是否存在刚才已使用的优惠券
    #打开谷歌浏览器
    print u"买家进入我的--优惠券--已使用页面，查看是否存在刚才已使用的优惠券\n"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation',mobile_emulation)
    driver = webdriver.Chrome(chrome_options=options)
    #最大化浏览器
    driver.maximize_window()
    #打开商城登录地址
    driver.get(loginadress)
    time.sleep(2)
    #点击我的
    el=driver.find_element_by_xpath("//*[@id='app']/div/div[17]/section/div/a[5]/p")
    driver.execute_script("arguments[0].click();", el)
    time.sleep(2)
    #跳转至登录页面输入用户名密码,登录 
    driver.find_element_by_xpath("//*[@id='accountLogin']/div[2]/div[1]/input").send_keys(userName)
    driver.find_element_by_xpath("//*[@id='accountLogin']/div[2]/div[2]/input").send_keys(passWord,Keys.ENTER)
    time.sleep(2)
    #进入我的--优惠券--已使用页面查看
    el=driver.find_element_by_xpath("//*[@id='app']/div/div[17]/section/div/a[5]/p")
    driver.execute_script("arguments[0].click();", el)
    time.sleep(2)
    el=driver.find_element_by_xpath("//*[@id='app']/div/div[4]/ul/li[5]/p[2]")
    driver.execute_script("arguments[0].click();", el)
    time.sleep(2)
    el=driver.find_element_by_xpath("//*[@id='coupons']/div[1]/span[2]")
    driver.execute_script("arguments[0].click();", el)
    time.sleep(2)
    #查看第一行是否存在刚才使用的优惠券
    couponsName4 = driver.find_element_by_xpath("//*[@id='coupons']/div[3]/ul/li[1]/div/div/p[2]").text
    print "couponsName4:",couponsName4
    if (couponsName4 == u"满500可使用"):
        print u"优惠券领取成功，状态为待使用！"
        ws.write(344,5,couponsName4)
        print (u"Case--AmezMallH5_013_UseCoupons买家使用优惠券---结果：Pass!")
        ws.write(334,7, 'Pass')
        #如果成功，将错误日志覆盖
        ws.write(334,10,'')
    else:
        print u"优惠券使用失败，不存在刚才使用的优惠券！"
        print (u"Case--AmezMallH5_013_UseCoupons买家使用优惠券---结果：Failed!")
        ws.write(334,7, 'Failed',style2)
        ws.write(334,10, u"优惠券使用失败！！",style2)    
    #退出浏览器
    driver.quit()

#商家登录回滚数据，将优惠券置为无效
    print u"\n商家登录回滚数据，将优惠券置为无效!!!"
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
    
    #将失败标志置为1，表示脚本执行完成           
    errorFlag = 1
    #退出浏览器
    driver.quit()
    
except Exception as e:
    print(e)
    #抛出异常
    traceback.format_exc()
    #写入异常至用例文件中：
    errorInfo = str(traceback.format_exc())
    print "****errorInfo:",errorInfo
    ws.write(334,10,errorInfo,style2)
    
finally :
    if(errorFlag == 0):
        print (u"Case--AmezMallH5_013_UseCoupons买家使用优惠券---结果：Failed!")
        ws.write(334,7, 'Failed',style2)
    ws.write(334,9, 'lilei')
    ws.write(334,8, datetime.now(), style1)    
    #利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
    wb.save('D:\\Python27\\TestData\\H5TestData.xls')
    print u"****Case--AmezMallH5_013_UseCoupons.py--结束运行****"