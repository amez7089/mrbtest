#coding=utf-8
import unittest
import requests
import json
try:
    url = "http://api.52mrb.com/app/mrbMember/login"
    data = {
        "ip": "192.168.1.170",
        "loginCustomer": 0,
        "loginType": 1,
        "mobile": "13713948825",
        "password": "e52397ecdf276f786d19442c90c4684d",
        "source": "0",
        "userName": "13713948825"
    }
    #测试美容邦登陆post接口
    r = requests.post(url=url, json=data)
    json_response=r.json()
    # json_response = json.loads(r.text)
    print json_response
    print json_response['message'],json_response['code']

    # r = requests.post(url=url, json=data)
    # result = r.json()
    # print result
except Exception as e:
    print('post请求出错,原因:%s' % e)

try:
    url = "http://api.52mrb.com/app/member/queryById/1154"
    # 测试美容邦前端根据ID查询会员信息get接口
    headers = {"Content-Type": "application/json"}
    r = requests.get(url=url, headers=headers)
    json_response=r.json()
    # json_response = json.loads(r.text)
    print json_response

    # r = requests.post(url=url, json=data)
    # result = r.json()
    # print result
except Exception as e:
    print('post请求出错,原因:%s' % e)

try:
    url = "http://test.52mrb.com/pc/activity/1.1.0/deleteById/139"
    # 测试根据活动id删除活动delete接口
    headers = {"Content-Type": "application/json"}
    r = requests.delete(url=url,headers=headers)
    json_response=r.json()
    # json_response = json.loads(r.text)
    print json_response
    print json_response['message'], json_response['code']


    # r = requests.post(url=url, json=data)
    # result = r.json()
    # print result
except Exception as e:
    print('post请求出错,原因:%s' % e)

try:
    url = "http://test.52mrb.com/app/storeBeautician/isOrder/1537/false"
    # 邦女郎修改接单状态的put接口
    headers = {"Content-Type": "application/json"}
    r = requests.put(url=url, headers=headers)
    json_response = r.json()
    # json_response = json.loads(r.text)
    print json_response
    print json_response['message'], json_response['code']

    # r = requests.post(url=url, json=data)
    # result = r.json()
    # print result
except Exception as e:
    print('post请求出错,原因:%s' % e)