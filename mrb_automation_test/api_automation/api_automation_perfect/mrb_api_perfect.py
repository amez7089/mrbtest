# -*- coding:utf-8 -*-
# *********************************
# *****美容邦API接口测试报告*******
# *********************************
# 导入依赖模块
import xlrd, xlwt
from xlutils.copy import copy
import os
import unittest
import requests
from datetime import datetime
import json
import sys
import HTMLTestRunnerCN
import time

reload(sys)
sys.setdefaultencoding('utf-8')
# 打开用例文件，读取对应用例的用户名等数据
casefile = xlrd.open_workbook('E:\\gitworksqace\\mrbdome1\\test1\\mrb_automation_test\\api_automation\\api_automation_perfect\\mrb_api_perfect.xls', formatting_info=True)
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


class mrb_api_test(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def test_mrb_api(self):
        i = 1
        No=u'開始'
        while No != u'完':

            try:
                # errorFlag = 0
                way=table.cell(i, 5).value
                print way
                if way==u'post':
                    # 读取用例文件中的接口URL，用例文件中此用例在第2行第4列（行列都从0开始计数）
                    url = table.cell(i, 4).value
                    print url
                    # 给消息头赋值
                    headers = {"Content-Type": "application/json"}
                    # 传入参数从表格中读取出来不是字典类型，所以要转换类型为字典型
                    data = json.loads(table.cell(i, 6).value)
                    # print data
                    # 发送POST请求给接口：
                    r = requests.post(url=url, json=data,headers=headers)
                    result = r.json()
                    print result
                elif way==u'get':
                    # 读取用例文件中的接口URL，用例文件中此用例在第2行第4列（行列都从0开始计数）
                    url = table.cell(i, 4).value
                    print url
                    # 给消息头赋值
                    headers = {"Content-Type": "application/json"}
                    # 传入参数从表格中读取出来不是字典类型，所以要转换类型为字典型
                    data = json.loads(table.cell(i, 6).value)
                    print data
                    # 发送get请求给接口：
                    r = requests.get(url=url,json=data,headers=headers)
                    result = r.json()
                    print result
                elif way==u'delete':
                    # 读取用例文件中的接口URL，用例文件中此用例在第2行第4列（行列都从0开始计数）
                    url = table.cell(i, 4).value
                    print url
                    # 给消息头赋值
                    headers = {"Content-Type": "application/json"}
                    # 传入参数从表格中读取出来不是字典类型，所以要转换类型为字典型
                    data = json.loads(table.cell(i, 6).value)
                    print data
                    # 发送delete请求给接口：
                    r = requests.delete(url=url,json=data,headers=headers)
                    # return r.json
                    result = r.json()
                    print result
                elif way==u'put':
                    # 读取用例文件中的接口URL，用例文件中此用例在第2行第4列（行列都从0开始计数）
                    url = table.cell(i, 4).value
                    print url
                    # 给消息头赋值
                    headers = {"Content-Type": "application/json"}
                    # 传入参数从表格中读取出来不是字典类型，所以要转换类型为字典型
                    data = json.loads(table.cell(i, 6).value)
                    print data
                    # 发送put请求给接口：
                    r = requests.put(url=url,json=data,headers=headers)
                    # return r.json
                    result = r.json()
                    print result
                elif way == u'head':
                    # 读取用例文件中的接口URL，用例文件中此用例在第2行第4列（行列都从0开始计数）
                    url = table.cell(i, 4).value
                    print url
                    # 给消息头赋值
                    headers = {"Content-Type": "application/json"}
                    # 传入参数从表格中读取出来不是字典类型，所以要转换类型为字典型
                    data = json.loads(table.cell(i, 6).value)
                    print data
                    # 发送put请求给接口：
                    r = requests.head(url=url, json=data, headers=headers)
                    # return r.json
                    result = r.json()
                    print result
                elif way == u'options':
                    # 读取用例文件中的接口URL，用例文件中此用例在第2行第4列（行列都从0开始计数）
                    url = table.cell(i, 4).value
                    print url
                    # 给消息头赋值
                    headers = {"Content-Type": "application/json"}
                    # 传入参数从表格中读取出来不是字典类型，所以要转换类型为字典型
                    data = json.loads(table.cell(i, 6).value)
                    print data
                    # 发送put请求给接口：
                    r = requests.options(url=url, json=data, headers=headers)
                    # return r.json
                    result = r.json()
                    print result
                else:
                    ws.write(i, 9, u'请求方式错误', style2)
                    ws.write(i, 10, 'Failed', style2)
                    ws.write(i, 11, 'zhouchuqi')
                    ws.write(i, 12, datetime.now(), style1)
                    i = i + 1
                    No = table.cell(i, 2).value
                    print u'请求方式错误'
                    print i
                    continue
                # 判断响应消息中是否符合接口设计时的预期：
                codeno=int(table.cell(i, 7).value)
                if ( (result['code'] == codeno)):
                    print result['message']
                    print 'Case Pass!'
                    # 将响应数据中的CODE写入用例文件中
                    ws.write(i, 8, result['code'])
                    # 将执行成功结果写入用例文件中
                    ws.write(i, 10, 'Pass')
                    # 如果成功，则清空错误日志
                    ws.write(i, 9, "")
                else:
                    print 'Case Fail!'
                    # 将错误日志写入用例文件中
                    ws.write(i, 9, r.text, style2)
                    # 将响应CODE写入用例文件中
                    ws.write(i, 8, result['code'])
                    # 将执行失败结果写入用例文件中
                    ws.write(i, 10, 'Fail', style2)
                ws.write(i, 11, 'zhouchuqi')
                ws.write(i, 12, datetime.now(), style1)
                # errorFlag = 1
            # finally:
            #     # 判断脚本执行到此处时，errorFlag是否为0，为0则表示没有执行到上一条语句errorFlag = 1，表示脚本有错误处中断了执行
            #     if (errorFlag == 0):
            #         print "Case---Failed!"
            #         ws.write(i, 9, r.text, style2)
            #         ws.write(i, 10, 'Failed', style2)
            #     ws.write(i, 11, 'zhouchuqi')
            #     ws.write(i, 12, datetime.now(), style1)
            except Exception as e:
                print('请求出错,原因:%s' % e)
                ws.write(i, 9,u'脚本执行失败', style2)
                ws.write(i, 10, 'Failed', style2)
                ws.write(i, 11, 'zhouchuqi')
                ws.write(i, 12, datetime.now(), style1)
            i=i+1
            No = table.cell(i, 2).value
            print No



    def tearDown(self):
        #           self.driver.quit()
        # 利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
        wb.save('E:\\gitworksqace\\mrbdome1\\test1\\mrb_automation_test\\api_automation\\api_automation_perfect\\mrb_api_perfect.xls')
        print("tearDown")

if __name__ == '__main__':
    unittest.main()
    # suite=unittest.TestSuite()
    # suite.addTest(mrb_api_test('test_logonin_success'))
    # test_report = "E:\\gitworksqace\\mrbdome1\\test1\\mrb_automation_test\\api_automation\\api_automation_perfect"
    # #按照一定的格式获取当前的时间
    # now = time.strftime("%Y-%m-%d_%H-%M-%S")
    # #定义报告存放路径
    # filename = test_report+'\\'+'Reportresult_'+now+'.html'
    # fp = open(filename,'wb')
    # #定义测试报告
    # runner = HTMLTestRunnerCN.HTMLTestRunner(
    #     stream=fp,
    #     tester=u'周楚奇',
    #     title=u'美容邦API接口测试报告：',
    #     description=u'测试用例执行情况：'
    #     )
    # runner.run(suite)
    # #关闭报告文件
    # fp.close()

