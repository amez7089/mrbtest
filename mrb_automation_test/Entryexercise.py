#coding=utf-8
import xlrd,xlwt
import time
import os
from selenium import webdriver
from xlutils.copy import copy
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
import sys
from lib2to3.tests.support import driver
from cgitb import text
reload(sys)
sys.setdefaultencoding('utf-8')
#打开用例文件，读取对应用例的用户名等数据
# casefile = xlrd.open_workbook('D:\\test\\mrbtest1.xls', formatting_info=True)
casefile = xlrd.open_workbook('E:\\gitworksqace\\mrbdome1\\test1\\mrb_automation_test\\mrbtest1.xls', formatting_info=True)
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
print(u"****Case-rmbtest1_001_Login管理员登录--开始运行****")
try:
    #失败标志
    errorFlag = 0
    #读取用户名
    userName = table.cell(1,1).value
    print userName
    #读取密码
    passWord = table.cell(1,2).value
    print passWord
    #打开谷歌浏览器
    driver=webdriver.Chrome()
    #最大化浏览器
    driver.maximize_window()
    #打开商城登录地址
    loginadress = table.cell(1,3).value
    driver.get(loginadress)
    time.sleep(5)
    driver.implicitly_wait(30)
    #输入用户名
    driver.find_element_by_class_name("ivu-input").send_keys(userName)
    #输入密码
    driver.find_element_by_xpath('//*[@id="main"]/div/div/div/div[2]/div[5]/input').send_keys(passWord)
    #点击登录
    driver.find_element_by_class_name("btn").click()
    text = driver.find_element_by_class_name("ivu-breadcrumb-item-link").text
    print text
    if (text == u"首页"):
        print u"登录成功！！"
        ws.write(1, 9, 'Pass')
    else:
        print u"登录失败！！"
        ws.write(1, 9, 'Failed', style2)
    driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/ul/li[6]/div/span').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/ul/li[6]/ul/a[5]/li/span').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/div[3]/div/div/div/form/div[3]/div/button[2]/span').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/div[3]/div/div/div/form/div[1]/div/div[1]/input').send_keys(u"自动化课程")
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div/div/div/div').click()
    os.system("d:\\upfile.exe")
    time.sleep(3)
    driver.get_screenshot_as_file("E:\\tupian1.png")
    time.sleep(3)
    print("截图成功")
    driver.find_element_by_xpath(
        '//*[@id="main"]/div/div/div[2]/div[3]/div/div/div/form/div[12]/div/div/div/button/span').click()
    time.sleep(1)
    #i ,j 用来xpath中循环定位
    j = 1
    #n,m 用来定位获取表格中位置
    m=2
    y=16
    Tunll=str(u'第一题')
    while Tunll != None:
        n = 1
        i = 1
        print i
        while i < 6:
            i = str(i)
            j = str(j)
            xp = '/html/body/div[17]/div[2]/div/div/div[2]/div['+ j +  ']/form/div[' + i + ']/div/div[1]/input'
            print(xp)
            i = int(i)
            j = int(j)
            t=table.cell(m,n).value
            print t
            driver.find_element_by_xpath(xp).send_keys(t)
            i = i + 1
            n=n+1
        j=str(j)
        xp1='/html/body/div[17]/div[2]/div/div/div[2]/div['+j+']/form/div[6]/div/div/div/span[1]'
        driver.find_element_by_xpath(xp1).click()
        time.sleep(1)
        key = table.cell(m, n).value
        print key
        if y==16:
            if key == 'A':
                driver.find_element_by_xpath('/html/body/div[16]/ul[2]/li[1]').click()
            elif key == 'B':
                driver.find_element_by_xpath('/html/body/div[16]/ul[2]/li[2]').click()
            elif key == 'C':
                driver.find_element_by_xpath('/html/body/div[16]/ul[2]/li[3]').click()
            else:
                driver.find_element_by_xpath('/html/body/div[16]/ul[2]/li[4]').click()
            y=y+2
        else:
            y=str(y)
            xp2 = '/html/body/div[' + y + ' ]/ul[2]/li[1]'
            xp3 = '/html/body/div[' + y + ']/ul[2]/li[2]'
            xp4 = '/html/body/div[' + y + ']/ul[2]/li[3]'
            xp5 = '/html/body/div[' + y + ']/ul[2]/li[4]'
            if key == 'A':
                driver.find_element_by_xpath(xp2).click()
            elif key == 'B':
                driver.find_element_by_xpath(xp3).click()
            elif key == 'C':
                driver.find_element_by_xpath(xp4).click()
            else:
                driver.find_element_by_xpath(xp5).click()
            y=int(y)
            y=y+1
        time.sleep(1)
        j = int(j)
        j=j+1
        m=m+1
        Tunll=table.cell(m,n).value
        if Tunll!=None:
            # driver.find_element_by_class_name('ivu-btn ivu-btn-primary').click()
            driver.find_element_by_xpath('/html/body/div[17]/div[2]/div/div/div[2]/button/span').click()
        else:
            driver.find_element_by_xpath('/html/body/div[17]/div[2]/div/div/div[3]/div/button[1]/span').click()
    # driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/div[3]/div/div/div/form/div[15]/div/button[2]').click()#/html/body/div[18]/div[2]/div/div/div[3]/div/button[2]/html/body/div[18]/div[2]/div/div/div[3]/div/button[2]/span
    # driver.find_element_by_xpath('/html/body/div[17]/div[2]/div/div/div[2]/div/form/div[6]/div/div/div/span[1]').click()#/html/body/div[17]/div[2]/div/div/div[3]/div/button[2]
    # time.sleep(1)
    # key=table.cell(2,i).value
    # print key
    # if key=='A':
    #     driver.find_element_by_xpath('/html/body/div[16]/ul[2]/li[1]').click()
    # elif key=='B':
    #     driver.find_element_by_xpath('/html/body/div[16]/ul[2]/li[2]').click()
    # elif key=='C':
    #     driver.find_element_by_xpath('/html/body/div[16]/ul[2]/li[3]').click()
    # else:driver.find_element_by_xpath('/html/body/div[16]/ul[2]/li[4]').click()
    # driver.find_element_by_xpath('/html/body/div[17]/div[2]/div/div/div[2]/button/span').click()

    errorFlag = 1

except Exception as e:
    print(e)

finally :
    if(errorFlag == 0):
        print (u"Case--AmezMallUI_001_Login已注册会员用户登录--结果：Failed!")
        ws.write(1,9, 'Failed',style2)
    ws.write(1,10, u'周楚奇')
    ws.write(1,11, datetime.now(), style1)
    #利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
    wb.save('E:\\gitworksqace\\mrbdome1\\test1\\mrb_automation_test\\mrbtest1.xls')
    #退出浏览器
    driver.quit()
    print "Case--AmezMallUI_001_Login.py运行结束！！！)"