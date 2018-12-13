# -*- coding:utf-8 -*-
# !/usr/bin/env python
# ****************************************
# *******已收货订单退款退货，商家同意********
# ****************************************
# 导入依赖模块
import xlrd, xlwt
import time
from selenium import webdriver
from xlutils.copy import copy
from datetime import datetime
from selenium.webdriver.support.ui import Select
import sys
import re
import amez_h5_login_def
import amez_h5_buggoods_class
from selenium.webdriver.common.action_chains import ActionChains

reload(sys)
sys.setdefaultencoding('utf-8')
import traceback
from selenium.webdriver.common.keys import Keys

# 打开用例文件，读取对应用例的用户名等数据
casefile = xlrd.open_workbook('E:\\gitworksqace\\mrbdome1\\test1\\amez_test\\H5TestData.xls', formatting_info=True)
# 设置日期格式
style1 = xlwt.XFStyle()
style1.num_format_str = 'YYYY-MM-DD HH:MM:SS'
# 设置单元格背景颜色
font0 = xlwt.Font()
font0.name = 'Times New Roman'  # 字体
font0.colour_index = 2  # 颜色
font0.bold = True  # 加粗
style2 = xlwt.XFStyle()
style2.font = font0
# 准备向用例文件中写入测试结果
wb = copy(casefile)
ws = wb.get_sheet(0)
# 打开第一张表
table = casefile.sheets()[0]
print u"****Case--AmezMallH5_008_ReceivedRefund已收货订单退款退货，商家同意--开始运行****"

try:
    # 失败标志
    errorFlag = 0
    print u"会员登录购买商品！"
    # 读取用户名
    userName = table.cell(9, 5).value
    print userName
    # 读取密码
    passWord = table.cell(10, 5).value
    print passWord
    loginadress = table.cell(3, 5).value
    print loginadress
    driver=amez_h5_login_def.open_browse(loginadress,'iPhone X')
    time.sleep(2)
    amez_h5_login_def.login_member(driver,userName,passWord)
    # 搜索框输入要搜索的商品
    ReadGoods = table.cell(27, 5).value
    # 点击搜索栏进入搜索页面
    amez_h5_buggoods_class.amez_h5_buygoods(driver,ReadGoods)
    OrderNumber=amez_h5_buggoods_class.amez_h5_get_ordernumber(driver,ReadGoods)
    print OrderNumber
    errorFlag=1


except Exception as e:
    print(e)
    # 抛出异常
    traceback.format_exc()
    # 写入异常至用例文件中：
    errorInfo = str(traceback.format_exc())
    print "****errorInfo:", errorInfo
    ws.write(144, 10, errorInfo, style2)

finally:
    if (errorFlag == 0):
        print u"Case--AmezMallH5_008_ReceivedRefund已收货订单退款退货，商家同意--结果：Failed!"
        ws.write(144, 7, 'Failed', style2)
    # 写入执行人员
    ws.write(144, 9, 'zhouchuqi')
    # 写入执行日期
    ws.write(144, 8, datetime.now(), style1)
    # 利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
    wb.save('E:\\gitworksqace\\mrbdome1\\test1\\amez_test\\H5TestData.xls')
    # 退出浏览器
    driver.quit()
    print u"Case--AmezMallH5_008_ReceivedRefund.py运行结束！！！"