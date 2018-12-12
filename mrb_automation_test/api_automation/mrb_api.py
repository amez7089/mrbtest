#coding=utf-8
import requests
import json
import unittest
class reques():
    def get(self, url):  # get消息
        try:
            r = requests.get(url, headers=self.headers)
            r.encoding = 'UTF-8'
            json_response = json.loads(r.text)
            return json_response
        except Exception as e:
            print('get请求出错,出错原因:%s' % e)
            return {}

    def post(self, url, data):  # post消息
        data = json.dumps(data)
        try:
            r = requests.post(url, data=data, headers=self.headers)
            json_response = json.loads(r.text)
            return json_response
        except Exception as e:
            print('post请求出错,原因:%s' % e)

    def delfile(self, url, data):  # 删除的请求
        try:
            del_word = requests.delete(url, data, headers=self.headers)
            json_response = json.loads(del_word.text)
            return json_response
        except Exception as e:
            print('del请求出错,原因:%s' % e)
            return {}

    def putfile(self, url, data):  # put请求
        try:
            data = json.dumps(data)
            me = requests.put(url, data)
            json_response = json.loads(me.text)
            return json_response
        except Exception as e:
            print('put请求出错,原因:%s' % e)
            return json_response


if __name__ == '__main__':
    unittest.main()
