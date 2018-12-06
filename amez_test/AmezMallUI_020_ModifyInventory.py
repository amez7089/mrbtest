#-*- coding:utf-8 -*-
#!/usr/bin/env python
#***************************************
#*******修改库存为0的商品库存后可购买*******
#***************************************
#导入依赖模块
import xlrd,xlwt
import time
from selenium import webdriver
from xlutils.copy import copy
from datetime import datetime
import sys
from lib2to3.tests.support import driver
from selenium.common.exceptions import StaleElementReferenceException
from cgitb import text
reload(sys)
sys.setdefaultencoding('utf-8')
import traceback

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
print u"****Case--AmezMallUI_020_ModifyInventory修改库存为0的商品库存后可购买--开始运行****"

try:
#商家登录修改对应商品库存
    #失败标志
    errorFlag = 0
    print u"\n---***商家登录修改对应商品库存***---"
    #读取用户名
    ShopuserName = table.cell(297,5).value
    print ShopuserName
    #读取密码
    ShoppassWord = table.cell(298,5).value
    print ShoppassWord
    #打开谷歌浏览器
    driver = webdriver.Chrome()
    #最大化浏览器
    driver.maximize_window()
    #打开商城登录地址
    Shoploginadress = table.cell(296,5).value
    driver.get(Shoploginadress)
    #输入用户名
    driver.find_elements_by_class_name("el-input__inner")[0].send_keys(ShopuserName)
    #输入密码
    driver.find_elements_by_class_name("el-input__inner")[1].send_keys(ShoppassWord)
    #点击登录
    driver.find_element_by_class_name("el-button--medium").click()
    time.sleep(3)
    #进入商品管理--出售中的商品
    driver.find_element_by_xpath("//*[@id='leftAside']/ul/a[2]/li/span").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='leftAside']/ul/li[2]/span").click()
    time.sleep(1)
    #查看出售中的商品
    for i in range(0,100):
        GoodList = driver.find_elements_by_class_name("goods-params-name")[i].text
        print u"出售中的商品存在:%s" % GoodList
        Kucun0 = driver.find_elements_by_class_name("online-goods-detail-box")[i].find_element_by_class_name("goods-storage").text
        print "Kucun0:",Kucun0
        #选择需要下架的商品
        if("海尔对开门冰箱" in GoodList and "0件" in Kucun0):
            driver.find_elements_by_class_name("el-icon-edit-outline")[i].click()
            break
    time.sleep(1)
    #在展开页面修改商品库存 
    driver.find_elements_by_class_name("store-online-sku-detail")[i].find_element_by_class_name("el-input__inner").clear()
    time.sleep(0.5)
    driver.find_elements_by_class_name("store-online-sku-detail")[i].find_element_by_class_name("el-input__inner").send_keys("1")
    time.sleep(0.5)
    #提交
    driver.find_elements_by_class_name("online-goods-detail-box")[i].find_element_by_class_name("mt10").click()
    time.sleep(5)
    #查看库存是否为1
    Kucun1 = driver.find_elements_by_class_name("online-goods-detail-box")[i].find_element_by_class_name("goods-storage").text
    print "Kucun1:",Kucun1
    if ("1件" in Kucun1):
        print u"修改商品库存为1成功！！！"
    else:
        print u"修改商品库存为1失败！！！"   
    
#买家用户登录后购买此商品
    NewWindow = 'window.open("http://web.test.amyun.cn/");'
    driver.execute_script(NewWindow)
    time.sleep(3)
    print "\n---***买家用户登录后购买此商品***---"
    #读取用户名
    userName = table.cell(5,5).value
    print userName
    #读取密码
    passWord = table.cell(6,5).value
    print passWord
    #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(2)
    #点击请登录/注册按钮
    driver.find_element_by_class_name("login").click()
    driver.implicitly_wait(30)
    #输入用户名
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div/div[2]/div[2]/div[1]/input").send_keys(userName)
    #输入密码
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div/div[2]/div[2]/div[2]/input").send_keys(passWord)
    #点击登录
    driver.find_element_by_id("loginBtn").click()
    time.sleep(1)
    driver.implicitly_wait(30)
    #判断是否登录成功，如果左上角出现“欢迎来到艾美e族商城”，则判断用户登录成功
    text = driver.find_element_by_class_name("left").text
    print text
    if (text == u"欢迎来到艾美e族商城"):
        print u"登录成功！！"
    else:
        print u"登录失败！！"
    #搜索栏中输入指定文字进行商品搜索
    searchtext = table.cell(309,5).value
    print  u"搜索文本为：",searchtext
    driver.find_element_by_class_name("searchIn").send_keys(searchtext)
    driver.find_element_by_class_name("searchBtn").click()
    time.sleep(2)
    #因为在点击时页面刷新，导致元素找不到，所以此函数作用是当找不到元素时，再次获取   
    def retryingFindClick(by):
        result = False
        Attempts = 0
        while Attempts < 5:
            try:
                result = driver.find_elements_by_class_name(by)[0].text
                break
            except StaleElementReferenceException, e:
                print(e)
                pass
            Attempts += 1
        return result
    #查看搜索结果是否找到指定商品
    SearchResult = retryingFindClick("goodsName")
    print "SearchResult:",SearchResult
    if ("海尔对开门冰箱" in SearchResult):
        print u"找到指定商品!---CasePass!!!"
        #点击商品进入详情页面
        driver.find_elements_by_class_name("goodsName")[0].click()
        time.sleep(2)
        #详情页面查看库存数据
        #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
        for handle in driver.window_handles:
            driver.switch_to_window(handle)
        time.sleep(2)
        Kucun2 = driver.find_element_by_class_name("store").text
        print "Kucun2:",Kucun2
        if (Kucun2 == u"库存1件"):
            print u"此商品只剩一件库存！"
            #购买商品
            driver.find_element_by_class_name("buyNow").click()
            time.sleep(2)
            #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
            for handle in driver.window_handles:
                driver.switch_to_window(handle)
            time.sleep(2)
            #提交订单
            driver.find_element_by_class_name("linear").click()
            time.sleep(1)
            #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
            for handle in driver.window_handles:
                driver.switch_to_window(handle)
            time.sleep(2)
            driver.find_element_by_class_name("yu").click()
            time.sleep(1)
            #输入支付密码
            driver.find_elements_by_class_name("shortInput")[0].send_keys("1")
            time.sleep(0.5)
            driver.find_elements_by_class_name("shortInput")[1].send_keys("2")
            time.sleep(0.5)
            driver.find_elements_by_class_name("shortInput")[2].send_keys("3")
            time.sleep(0.5)
            driver.find_elements_by_class_name("shortInput")[3].send_keys("4")
            time.sleep(0.5)
            driver.find_elements_by_class_name("shortInput")[4].send_keys("5")
            time.sleep(0.5)
            driver.find_elements_by_class_name("shortInput")[5].send_keys("6")
            time.sleep(0.5)
            #确认支付
            driver.find_element_by_class_name("grad").click()
            time.sleep(2)
            #支付成功
            #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
            for handle in driver.window_handles:
                driver.switch_to_window(handle)
            time.sleep(2)
            driver.find_element_by_class_name("close_btn").click()
            #因为窗口变化，所以要定位当前的句柄，不然无法找到元素
            for handle in driver.window_handles:
                driver.switch_to_window(handle)
            time.sleep(2)
            PaySuccess = driver.find_element_by_class_name("successP").text
            if ("支付成功" in PaySuccess):
                print u"购买商品成功！"
            
#窗口切换到商家页面
    driver.switch_to_window(driver.window_handles[0])
    driver.refresh()
    time.sleep(3)
    #查看商品库存是否变为0
    for i in range(0,100):
        GoodList = driver.find_elements_by_class_name("goods-params-name")[i].text
        print u"出售中的商品存在:%s" % GoodList
        Kucun4 = driver.find_elements_by_class_name("online-goods-detail-box")[i].find_element_by_class_name("goods-storage").text
        print "Kucun0:",Kucun0
        #选择需要下架的商品
        if("海尔对开门冰箱" in GoodList and "0件" in Kucun4):
            print u"库存已变为0！！！---CasePass！！！"
            print (u"Case--AmezMallUI_020_ModifyInventory修改库存为0的商品库存后可购买---结果：Pass!") 
            ws.write(296,7, 'Pass')
            #如果成功，将错误日志覆盖
            ws.write(296,10,'')
            break           
        else:
            print (u"Case--AmezMallUI_020_ModifyInventory修改库存为0的商品库存后可购买---结果：Failed!")
            ws.write(296,7, 'Failed',style2)
    
    #将失败标志置为1，表示脚本执行完成           
    errorFlag = 1
    
except Exception as e:
    print(e)
    #抛出异常
    traceback.format_exc()
    #写入异常至用例文件中：
    errorInfo = str(traceback.format_exc())
    print "****errorInfo:",errorInfo
    ws.write(296,10,errorInfo,style2)
    #退出浏览器
    driver.quit()
    
finally :
    if(errorFlag == 0):
        print (u"Case--AmezMallUI_020_ModifyInventory修改库存为0的商品库存后可购买---结果：Failed!")
        ws.write(296,7, 'Failed',style2)
    ws.write(296,9, 'lilei')
    ws.write(296,8, datetime.now(), style1)
    #利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
    wb.save('E:\\gitworksqace\\mrbdome1\\test1\\amze_test\\UITestData.xls')
    #退出浏览器
    driver.quit()
    print u"****Case--AmezMallUI_020_ModifyInventory.py--结束运行****"