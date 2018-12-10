#-*-coding:utf-8 -*-
from flask import Flask, render_template,request
import jieba
import requests, json

app = Flask(__name__)

def cut(content):
    word_list = jieba.lcut(content)
    word_num = len(word_list)
    word_str = ",".join(word_list)
    return word_str, word_num

@app.route("/")
def index():
    return "Hello, World!111"

@app.route("/amez999/user")
def amezuser():
    return"艾小美,艾小帅"

@app.route("/amez/<int:id>")
def amezmemberidfind(id):
    Usertable={1:"xiaoming",2:"baiyun",3:"heitu"}
    return Usertable[id]
@app.route("/amez/member",methods=["POST"])
def member_id():
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
        return u'请求方式错误'




@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(port=5001,debug=True)