#!/usr/bin/python
# -*- coding: utf-8 -*-

import jieba
from flask import Flask, request, jsonify
import requests, json

# business logic part

def cut(content):
    word_list = jieba.lcut(content)
    word_num = len(word_list)
    word_str = ",".join(word_list)
    return word_str, word_num

# flask part

toy = Flask(__name__) # create a Flask instance

@toy.route("/")
def index():
    return "Hello, World!"

# <string:content>定义输入的内容的类型及变量名，注意":"左右不能有空格，
@toy.route("/cut/para/<string:content>")
def paraCut(content):
    word_str, word_num = cut(content)
    return "words: {}; number of words: {}".format(word_str, word_num)

@toy.route("/cut/json/", methods=["POST"]) # methods可以是多个
def jsonCut():
    if request.method == "POST":
        # 从request请求中提取json内容
        json_dict = request.get_json()
        content = json_dict["content"]
        # 运行业务逻辑
        word_str, word_num = cut(content)
        # 将结果格式化为dict
        data = {"word_str": word_str, "word_num": word_num}
        return json.dumps(data,ensure_ascii = False) # 将data序列化为json类型的str
    else:
        return """<html><body>
        Something went horribly wrong
        </body></html>"""

@toy.route("/test/post/")
def postTest():
    # 生成一个request请求，其中包含了请求对象、要处理的数据、数据类型
    url = "http://localhost:5000/cut/json/"
    data = {"content": "我们中出了一个叛徒"}
    headers = {"Content-Type" : "application/json"}
    # 使用python自带的requests post方法发送请求
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.text

if __name__ == "__main__":
    toy.run(debug=True)
