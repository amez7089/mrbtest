#-*- coding:utf-8 -*-
#!/usr/bin/env python
#*********************************
#*******搜索已下架商品**************
#*********************************
#导入依赖模块
import xlrd,xlwt
import time
from selenium import webdriver
from xlutils.copy import copy
from datetime import datetime
import sys
from lib2to3.tests.support import driver
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
print u"****Case--AmezMallUI_018_SaleOfGoods搜索已下架商品--开始运行****"

try:
#商家登录下架对应商品
    errorFlag = 0
    #定义H5机型
    print u"\n---***商家登录下架对应商品***---"
    #读取用户名
    ShopuserName = table.cell(276,5).value
    print ShopuserName
    #读取密码
    ShoppassWord = table.cell(277,5).value
    print ShoppassWord
    #打开谷歌浏览器
    driver = webdriver.Chrome()
    #最大化浏览器
    driver.maximize_window()
    #打开商城登录地址
    Shoploginadress = table.cell(275,5).value
    driver.get(Shoploginadress)
    #输入用户名
    driver.find_element_by_xpath("//*[@id='my-form']/div[1]/div/input").send_keys(ShopuserName)
    #输入密码
    driver.find_element_by_xpath("//*[@id='my-form']/div[2]/div/input").send_keys(ShoppassWord)
    #点击登录
    driver.find_element_by_xpath("//*[@id='my-form']/div[3]/button[1]/span").click()
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
        #选择需要下架的商品
        if("美的（Midea）" in GoodList):
            driver.find_elements_by_class_name("selectItem")[i].click()
            break
    time.sleep(2)
    #下架选中商品
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[4]/button[2]/span").click()
    time.sleep(3)
    #查看出售中商品中是否没有了刚才下架商品
    GoodList = driver.find_element_by_xpath("//*[@id='main']/div[2]").text
    print "商品下架后的出售中商品列表1：",GoodList
    #查看列表中是还存在下架商品
    if("美的（Midea）" not in GoodList):
        print u"出售中商品不存在刚才下架商品，下架成功！"
    else:
        print u"出售中商品存在刚才下架商品，下架失败！"
    time.sleep(2)

#新开窗口，买家用户登录搜索下架商品
    NewWindow = 'window.open("http://web.test.amyun.cn/");'
    driver.execute_script(NewWindow)
    time.sleep(3)
    print "\n---***买家用户登录搜索下架商品***---"
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
    driver.find_element_by_xpath("//*[@id='app']/div[1]/div/ul/li[1]").click()

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
    text = driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div/span").text
    print text
    if (text == u"欢迎来到艾美e族商城"):
        print u"登录成功！！"
    else:
        print u"登录失败！！"
    #搜索栏中输入指定文字进行商品搜索
    searchtext = table.cell(284,5).value
    print  u"搜索文本为：",searchtext
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[1]/div[1]/div[2]/div[2]/div/input").send_keys(searchtext)
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[1]/div[1]/div[2]/div[2]/button").click()
    time.sleep(2)
    #查看搜索结果是否找不到指定商品
    SearchResult = driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[3]/div[2]/div[3]/p[1]").text
    print "SearchResult:",SearchResult
    if (SearchResult == "非常抱歉，没有找到相关的宝贝"):
        print u"非常抱歉，没有找到相关的宝贝!---CasePass!!!"
        print (u"Case--AmezMallUI_018_SaleOfGoods搜索已下架商品--结果：Pass!")
        ws.write(275,7, 'Pass')    
        #如果成功，将错误日志覆盖
        ws.write(275,10,'')
    else:
        print u"结果错误！！！"
        ws.write(275,7, 'Failed',style2)
    time.sleep(2)
    
#回到商家窗口，回滚数据，上架商品
    driver.switch_to_window(driver.window_handles[0])
    driver.find_element_by_xpath("//*[@id='leftAside']/ul/li[4]/span").click()
    time.sleep(2)
    #查看所有仓库中的商品
    for i in range(0,100):
        GoodList = driver.find_elements_by_class_name("online-goods-detail")[i].text
        #选择需要下架的商品
        if("美的（Midea）" in GoodList):
            driver.find_elements_by_class_name("selectItem")[i].click()
            print u"出售中的商品存在:%s",GoodList
            break
    #上架选中商品    
    driver.find_element_by_xpath("//*[@id='main']/div[2]/div[6]/button[2]/span").click()
    time.sleep(4)
    #进入出售中商品中查看是否出现刚才上架商品
    driver.find_element_by_xpath("//*[@id='leftAside']/ul/li[2]/span").click()
    time.sleep(2)
    GoodList = driver.find_element_by_xpath("//*[@id='main']/div[2]").text
    print "商品下架后的出售中商品列表2：",GoodList
    #查看列表中是还存在下架商品
    if("美的（Midea）" in GoodList):
        print u"出售中商品存在刚才上架商品，上架成功！"
        print u"数据回滚成功，商品被重新上架！！！"
    else:
        print u"出售中商品不存在刚才上架商品，上架失败！"
        print u"数据回滚失败，商品没有被重新上架！！！"
    #将失败标志置为1，表示脚本执行完成           
    errorFlag = 1
    
except Exception as e:
    print(e)
    #抛出异常
    traceback.format_exc()
    #写入异常至用例文件中：
    errorInfo = str(traceback.format_exc())
    print "****errorInfo:",errorInfo
    ws.write(275,10,errorInfo,style2)
    #退出浏览器
    driver.quit()
    
finally :
    if(errorFlag == 0):
        print (u"Case--AmezMallUI_018_SaleOfGoods搜索已下架商品---结果：Failed!")
        ws.write(275,7, 'Failed',style2)
    ws.write(275,9, 'zhouchuqi')
    ws.write(275,8, datetime.now(), style1)
    #利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
    wb.save('E:\\gitworksqace\\mrbdome1\\test1\\amze_test\\UITestData.xls')
    #退出浏览器
    driver.quit()
    print u"****Case--AmezMallUI_018_SaleOfGoods.py--结束运行****"