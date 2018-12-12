#-*- coding:utf-8 -*-
#!/usr/bin/env python
#*********************************
#*******买家领取的优惠券过期********
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
import win32gui
import win32con

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
print u"****Case--AmezMallH5_014_CouponExpired买家领取的优惠券过期--开始运行****"

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
    CouponsName =  u"满666减555_" + str(datetime.datetime.now())
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
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[4]/div/div/input").send_keys("555")
    time.sleep(1)
    #输入可发放总数
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[5]/div/div/input").send_keys("1")
    time.sleep(1)
    #选择每人限领
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[6]/div/div/div/input").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[1]").click()
    #消费金额为:
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[7]/div/div/input").send_keys("666")
    time.sleep(1)
    #代金券描述：
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[2]/form/div[8]/div/div/textarea").send_keys(u"满666减555")
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
    ws.write(349,5,CouponsName1)
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
                if (u"本店满666减555" in CouponsList):
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
            if ("满666减555" in CouponsList1):
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
        
    #等待两分钟,刷新页面,查看代金券状态
    for i in range(1,12):
        print u"等待优惠券过期中,请稍候..."
        time.sleep(10)
        
#商家登录查看优惠券状态是否为已过期
    print u"\n商家登录查看优惠券状态是否为已过期!!!"
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
    #查看第一条优惠券是否为过期状态
    TheFirstCoupons = driver.find_element_by_xpath("//*[@id='main']/div[2]/div[3]/div/div[3]/table/tbody/tr[1]/td[1]/div").text
    print "TheFirstCoupons:",TheFirstCoupons
    if ("满666减555" in TheFirstCoupons):
        TheFirstCouponsStatus = driver.find_element_by_xpath("//*[@id='main']/div[2]/div[3]/div/div[3]/table/tbody/tr[1]/td[5]/div").text
        print "TheFirstCouponsStatus:",TheFirstCouponsStatus
        if (TheFirstCouponsStatus == u"已过期"):
            print u"此优惠券状态为:",TheFirstCouponsStatus
            ws.write(353,5,TheFirstCouponsStatus)
        else:
            print u"此优惠券状态不是已过期！！！"
            ws.write(345,10,u"商家端优惠券没有过期！",style2)
            ws.write(353,5,TheFirstCouponsStatus,style2)
    #关闭浏览器
    driver.quit()    
    
#买家登录查看优惠券是否过期
    #打开谷歌浏览器
    print u"买家进入我的--优惠券--已过期页面，查看优惠券是否过期\n"
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
    #进入我的--优惠券--已过期页面查看
    el=driver.find_element_by_xpath("//*[@id='app']/div/div[17]/section/div/a[5]/p")
    driver.execute_script("arguments[0].click();", el)
    time.sleep(2)
    el=driver.find_element_by_xpath("//*[@id='app']/div/div[4]/ul/li[5]/p[2]")
    driver.execute_script("arguments[0].click();", el)
    time.sleep(2)
    el=driver.find_element_by_xpath("//*[@id='coupons']/div[1]/span[3]")
    driver.execute_script("arguments[0].click();", el)
    time.sleep(2)
    #查看第一行是否存在刚才使用的优惠券
#     NoCoupons = driver.find_element_by_xpath("//*[@id='notFind']/p").text
    couponsName4 = driver.find_element_by_xpath("//*[@id='coupons']/div[3]/ul/li[1]/div/div/p[2]").text
    print "couponsName4:",couponsName4
    if (couponsName4 == u"满666可使用"):
        print u"优惠券已过期！"
        ws.write(352,5,couponsName4)
        print (u"Case--AmezMallH5_014_CouponExpired买家领取的优惠券过期---结果：Pass!")
        ws.write(345,7, 'Pass')
        #如果成功，将错误日志覆盖
        ws.write(345,10,'')
        #退出浏览器
        driver.quit()
    else:
        print u"优惠券未过期，不存在过期的优惠券！"
        print (u"Case--AmezMallH5_014_CouponExpired买家领取的优惠券过期---结果：Failed!")
        ws.write(345,7, 'Failed',style2)
        ws.write(345,10, u"优惠券未过期！！",style2)    
    
    #将失败标志置为1，表示脚本执行完成           
    errorFlag = 1
    
except Exception as e:
    print(e)
    #抛出异常
    traceback.format_exc()
    #写入异常至用例文件中：
    errorInfo = str(traceback.format_exc())
    print "****errorInfo:",errorInfo
    ws.write(345,10,errorInfo,style2)
    #退出浏览器
    driver.quit()
    
finally :
    if(errorFlag == 0):
        print (u"Case--AmezMallH5_014_CouponExpired买家领取的优惠券过期---结果：Failed!")
        ws.write(345,7, 'Failed',style2)
    ws.write(345,9, 'zhouchuqi')
    ws.write(345,8, datetime.datetime.now(), style1)
    #利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
    wb.save('E:\\gitworksqace\\mrbdome1\\test1\\amez_test\\H5TestData.xls')
    print u"****Case--AmezMallH5_014_CouponExpired.py--结束运行****"