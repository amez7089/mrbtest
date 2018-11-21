#coding=utf-8
import requests
import json


class RunMain:

    def send_post(self, url, data):
        # 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        # result = requests.post(url=url, data=data).json()
        # # 因为这里要封装post方法，所以这里的url和data值不能写死
        # res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
        # return res
        # # print res
        r = requests.post(url=url, json=data)
        result = r.json()
        return result


    def send_get(self, url, data):
        result = requests.get(url=url, data=data)
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def run_main(self, method, url=None, data=None):
        result = None
        if method == 'post':
            result = self.send_post(url, data)
        elif method == 'get':
            result = self.send_get(url, data)
        else:
            print "错误"
        return result


if __name__ == '__main__':
    url = 'http://api.52mrb.com/app/member/queryById'
    data ={
'1145'
}
    # 实例化RunMain类
    run = RunMain()
    res = run.run_main("post",url,data)
    print res
