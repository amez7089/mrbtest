# -*- coding=utf-8 -*-
# @Time     :2018/12/27 17:12
# @Author   :ZhouChuqi
import MySQLdb
import jieba
from flask import Flask, request
import json
import time

from flask import jsonify


toy = Flask(__name__)


def cut(memberid):
    word_list = jieba.lcut(memberid)
    word_num = len(word_list)
    word_str = ",".join(word_list)
    return word_str, word_num


@toy.route("/")
def hello_world():
    return "Hello World!"


@toy.route("/cut/para/<string:memberid>")
def paraCut(memberid):
    # word_str, word_num = cut(memberid)
    result = member_sex(memberid)
    print result
    if result == 201:
        data = {"code": result, "message": "将会员{}性别修改成男性".format(memberid)}
        return json.dumps(data, ensure_ascii=False)  # 将data序列化为json类型的str
    elif result == 202:
        data = {"code": result, "message": "将会员{}性别修改成女性".format(memberid)}
        return json.dumps(data, ensure_ascii=False)  # 将data序列化为json类型的str
    else:
        data = {"state": result, "body": '修改会员性别失败'}
        return json.dumps(data, ensure_ascii=False)
        # 将结果格式化为dict


@toy.route('/member/queryById/<string:memberid>')
def queryById(memberid):
    result, code = member_name(memberid)
    print result, code
    if code == 200:
        data = {"code": code, "message": "接口调用成功", "name": result}
        return json.dumps(data, ensure_ascii=False)
    else:
        data = {"code": code, "message": "会员不存在"}
        return json.dumps(data, ensure_ascii=False)


@toy.route('/member/information/<int:memberid>')
def information(memberid):
    result, code = Membership_information(memberid)
    print result
    print code
    # re = {'memberid': result[0], 'name': result[1], 'member_mobile': result[2], 'address': result[3], 'sex': result[4],
    #       'is_marry': result[5]}
    # print re  timeStamp = int(time.mktime(timeArray))
    if code == 200:
        re = {'memberid': result[0], 'name': result[1], 'member_mobile': result[2], 'address': result[3],
              'sex': result[4], 'is_marry': result[5]}
        print re
        t = {}
        for num in range(1, 5):
            t[str(num)] = re
        data = {}
        data['success'] = 'success'
        data['data'] = t
        return jsonify(data)
        """
        a=str(result[7])
        # timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
        # timeStamp = int(time.mktime(timeArray))
        # print a,timeStamp
        data = {'memberid': result[0], 'name': result[1], 'member_mobile': result[2], 'address': result[3],
              'sex': result[4], 'is_marry': result[5],'uptime':a}
        data = {"code": code, "message": "接口调用成功", "data": data}
        return json.dumps(data, ensure_ascii=False)
        """
    else:
        data = {"code": code, "message": "会员不存在"}
        return json.dumps(data, ensure_ascii=False)


@toy.route("/cut/json/", methods=["POST"])  # methods可以是多个
def jsonCut():
    if request.method == "POST":
        # 从request请求中提取json内容
        json_dict = request.get_json()
        memberid = json_dict["memberid"]
        # 运行业务逻辑
        result = member_sex(memberid)
        # print result
        if result == 201:
            data = {"code": result, "message": "将会员{}性别修改成男性".format(memberid)}
            return json.dumps(data, ensure_ascii=False)  # 将data序列化为json类型的str
        elif result == 202:
            data = {"code": result, "message": "将会员{}性别修改成女性".format(memberid)}
            return json.dumps(data, ensure_ascii=False)  # 将data序列化为json类型的str
        else:
            data = {"state": result, "body": '修改会员性别失败'}
            return json.dumps(data, ensure_ascii=False)
            # 将结果格式化为dict

    else:
        return """<html><body>
        Something went horribly wrong
        </body></html>"""


def member_sex(member_id):
    # 打开数据库连接
    db = MySQLdb.connect("172.16.20.115", "root", "123456", 'myfirstdata', charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 更新语句
    sql = "UPDATE member SET sex = 1 WHERE sex = 0 and member_id= %s" % member_id
    sql2 = "UPDATE member SET sex = 0 WHERE sex = 1 and member_id=%s" % member_id
    sql3 = "SELECT * FROM member where member_id=%s" % member_id
    try:
        # 执行SQL语句
        cursor.execute(sql3)
        # 提交到数据库执行
        db.commit()
        results = cursor.fetchall()
        print results
        if results:
            for results in results:
                sex = results[4]
                # 打印结果
                print sex
                if sex == 1:
                    cursor.execute(sql2)
                    return 201
                else:
                    cursor.execute(sql)
                    return 202
        else:
            return 404


    except:
        # 发生错误时回滚
        db.rollback()
        return 500

    # 关闭数据库连接
    db.close()


def member_name(member_id):
    # 打开数据库连接
    db = MySQLdb.connect("172.16.20.115", "root", "123456", 'myfirstdata', charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 更新语句
    sql = "SELECT * FROM member where member_id=%s" % member_id
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        results = cursor.fetchall()
        if results:
            for results in results:
                name = results[1]
                code = 200
            return name, code
        else:
            code = 404
            name = "会员不存在"
            return name, code


    except:
        # 发生错误时回滚
        db.rollback()
        code = 500
        return code

    # 关闭数据库连接
    db.close()


def Membership_information(member_id):
    # 打开数据库连接
    db = MySQLdb.connect("172.16.20.115", "root", "123456", 'myfirstdata', charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 更新语句
    sql = "SELECT * FROM member_card where member_id=%s" % member_id
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        results = cursor.fetchall()
        if results:
            for results in results:
                code = 200
                return results, code
        else:
            code = 404
            name = "会员不存在"
            return name, code


    except:
        # 发生错误时回滚
        db.rollback()
        code = 500
        return code

    # 关闭数据库连接
    db.close()


if __name__ == "__main__":
    toy.run(port=5000, debug=True)
