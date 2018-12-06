#-*- coding:utf-8 -*-
#*********************************
#*******艾美商城登录接口************
#*********************************
#导入依赖模块
import xlrd,xlwt
from xlutils.copy import copy
import os
import unittest
import requests
from datetime import datetime
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#打开用例文件，读取对应用例的用户名等数据
casefile = xlrd.open_workbook('D:\\Python27\\TestData\\InterfaceData.xls', formatting_info=True)
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

class MyTest(unittest.TestCase):
        def setUp(self):
            print("setUp")
        def test_logonin_success(self):
            try:
                errorFlag = 0
                #读取用例文件中的接口URL，用例文件中此用例在第2行第4列（行列都从0开始计数）
                url = table.cell(2,4).value
                print url
                #给消息头赋值
                headers = {"Content-Type":"application/json"}  
                #传入参数从表格中读取出来不是字典类型，所以要转换类型为字典型
                data = json.loads(table.cell(2,6).value)
                print type(data)
                #发送POST请求给接口：
                r = requests.post(url = url,json = data,headers = headers)  
                #return r.json  
                result = r.json()
#                 print (r.text)     
#                 print (r.status_code)
#                 print "the code is:",result['code']
                #判断响应消息中是否符合接口设计时的预期：
                if((result['status'] == 'SUCCESS') and (result['msg']== u'成功') and (result['code']=='0')):
                    print 'Case Pass!'
                    #将响应数据中的CODE写入用例文件中
                    ws.write(2,8,result['code'])
                    #将执行成功结果写入用例文件中
                    ws.write(2,10, 'Pass')
                    #如果成功，则清空错误日志
                    ws.write(2,9,"")
                else:
                    print 'Case Fail!'
                    #将错误日志写入用例文件中
                    ws.write(2,9,r.text,style2)
                    #将响应CODE写入用例文件中
                    ws.write(2,8,result['code'])
                    #将执行失败结果写入用例文件中
                    ws.write(2,10, 'Fail',style2)
                errorFlag = 1
            finally :
                #判断脚本执行到此处时，errorFlag是否为0，为0则表示没有执行到上一条语句errorFlag = 1，表示脚本有错误处中断了执行
                if(errorFlag == 0):
                    print "Case---Failed!"
                    ws.write(2,9,r.text,style2)
                    ws.write(2,10, 'Failed',style2)
                ws.write(2,11, 'lilei')
                ws.write(2,12, datetime.now(), style1)    

        def test_logonin_1007(self):
            #密码输入错误返回：用户名或密码错误
            try:
                errorFlag = 0
                #读取用例文件中的接口URL，用例文件中此用例在第3行第4列（行列都从0开始计数）
                url = table.cell(3,4).value
                print url
                #给消息头赋值
                headers = {"Content-Type":"application/json"}  
                #传入参数从表格中读取出来不是字典类型，所以要转换类型为字典型
                data = json.loads(table.cell(3,6).value)
#                 print type(data)
                #发送POST请求给接口：
                r = requests.post(url = url,json = data,headers = headers)  
                #return r.json  
                result = r.json()
                #                 print (r.text)     
                #                 print (r.status_code)
                #                 print "the code is:",result['code']
                #判断响应消息中是否符合接口设计时的预期：
                if((result['status'] == 'ERROR') and (result['msg']== u'用户名或密码错误') and (result['code']=='1007')):
                    print 'Case Pass!'
                    #将响应数据中的CODE写入用例文件中
                    ws.write(3,8,result['code'])
                    #将执行成功结果写入用例文件中
                    ws.write(3,10, 'Pass')
                    #如果成功，则清空错误日志
                    ws.write(3,9,"")
                else:
                    print 'Case Fail!'
                    #将错误日志写入用例文件中
                    ws.write(3,9,r.text,style2)
                    #将响应CODE写入用例文件中
                    ws.write(3,8,result['code'])
                    #将执行失败结果写入用例文件中
                    ws.write(3,10, 'Fail',style2)
                errorFlag = 1
            finally :
                #判断脚本执行到此处时，errorFlag是否为0，为0则表示没有执行到上一条语句errorFlag = 1，表示脚本有错误处中断了执行
                if(errorFlag == 0):
                    print "Case---Failed!"
                    ws.write(3,9,r.text,style2)
                    ws.write(3,10, 'Failed',style2)
                ws.write(3,11, 'lilei')
                ws.write(3,12, datetime.now(), style1)
          
        def test_logonin_1003(self):
            #用户未注册
            try:
                errorFlag = 0
                #读取用例文件中的接口URL，用例文件中此用例在第4行第4列（行列都从0开始计数）
                url = table.cell(4,4).value
                print url
                #给消息头赋值
                headers = {"Content-Type":"application/json"}  
                #传入参数从表格中读取出来不是字典类型，所以要转换类型为字典型
                data = json.loads(table.cell(4,6).value)
                #发送POST请求给接口：
                r = requests.post(url = url,json = data,headers = headers)  
                #return r.json  
                result = r.json()
                #                 print (r.text)     
                #                 print (r.status_code)
                #                 print "the code is:",result['code']
                #判断响应消息中是否符合接口设计时的预期：
                if((result['status'] == 'ERROR') and (result['msg']== u'用户未注册') and (result['code']=='1003')):
                    print 'Case Pass!'
                    #将响应数据中的CODE写入用例文件中
                    ws.write(4,8,result['code'])
                    #将执行成功结果写入用例文件中
                    ws.write(4,10, 'Pass')
                    #如果成功，则清空错误日志
                    ws.write(4,9,"")
                else:
                    print 'Case Fail!'
                    #将错误日志写入用例文件中
                    ws.write(4,9,r.text,style2)
                    #将响应CODE写入用例文件中
                    ws.write(4,8,result['code'])
                    #将执行失败结果写入用例文件中
                    ws.write(4,10, 'Fail',style2)
                errorFlag = 1
            finally :
                #判断脚本执行到此处时，errorFlag是否为0，为0则表示没有执行到上一条语句errorFlag = 1，表示脚本有错误处中断了执行
                if(errorFlag == 0):
                    print "Case---Failed!"
                    ws.write(4,9,r.text,style2)
                    ws.write(4,10, 'Failed',style2)
                ws.write(4,11, 'lilei')
                ws.write(4,12, datetime.now(), style1)      

        def test_logonin_1004(self):
            #用户名不能为空
            try:
                errorFlag = 0
                #读取用例文件中的接口URL，用例文件中此用例在第5行第4列（行列都从0开始计数）
                url = table.cell(5,4).value
                print url
                #给消息头赋值
                headers = {"Content-Type":"application/json"}  
                #传入参数从表格中读取出来不是字典类型，所以要转换类型为字典型
                data = json.loads(table.cell(5,6).value)
                #发送POST请求给接口：
                r = requests.post(url = url,json = data,headers = headers)  
                #return r.json  
                result = r.json()
                #                 print (r.text)     
                #                 print (r.status_code)
                #                 print "the code is:",result['code']
                #判断响应消息中是否符合接口设计时的预期：
                if((result['status'] == 'ERROR') and (result['msg']== u'账户不能为空') and (result['code']=='1004')):
                    print 'Case Pass!'
                    #将响应数据中的CODE写入用例文件中
                    ws.write(5,8,result['code'])
                    #将执行成功结果写入用例文件中
                    ws.write(5,10, 'Pass')
                    #如果成功，则清空错误日志
                    ws.write(5,9,"")
                else:
                    print 'Case Fail!'
                    #将错误日志写入用例文件中
                    ws.write(5,9,r.text,style2)
                    #将响应CODE写入用例文件中
                    ws.write(5,8,result['code'])
                    #将执行失败结果写入用例文件中
                    ws.write(5,10, 'Fail',style2)
                errorFlag = 1
            finally :
                #判断脚本执行到此处时，errorFlag是否为0，为0则表示没有执行到上一条语句errorFlag = 1，表示脚本有错误处中断了执行
                if(errorFlag == 0):
                    print "Case---Failed!"
                    ws.write(5,9,r.text,style2)
                    ws.write(5,10, 'Failed',style2)
                ws.write(5,11, 'lilei')
                ws.write(5,12, datetime.now(), style1)      

        def tearDown(self):        
#           self.driver.quit() 
            #利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
            wb.save('D:\\Python27\\TestData\\InterfaceData.xls')        
            print("tearDown")  
             
            
if __name__ == '__main__':    
        unittest.main()
        