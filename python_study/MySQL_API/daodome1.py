# -*- coding=utf-8 -*-
# @Time     :2019/1/4 16:32
# @Author   :ZhouChuqi
import MySQLdb
import json
import jsonify
import numpy as np

def member_sms(member_id):
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
            t={}
            for results in results:
                i=0
                t[i] = results
                i=i+1
            code = 200
            return t,code
        else:
            return 404
    except:
        # 发生错误时回滚
        db.rollback()
        return 500

        # 关闭数据库连接
    db.close()
print member_sms(12)
deta,code = member_sms(12)
print deta
# y=json.dumps(deta, ensure_ascii=False)
print code
print deta
# print y
re={'memberid':deta[0],'name':deta[1],'member_mobile':deta[2],'address':deta[3],'sex':deta[4],'is_marry':deta[5]}
print re
t={}
for num in range(1,5):
    t[str(num)]= re
data={}
data['success']='success'
data['data']=t
# return jsonify(data)
# print json.dumps(re, ensure_ascii=False)

# db = MySQLdb.connect("172.16.20.115", "root", "123456", 'myfirstdata', charset='utf8')
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # SQL 更新语句
# sql = "SELECT * FROM member_card where member_id=12"
# try:
#     # 执行SQL语句
#     cursor.execute(sql)
#     # 提交到数据库执行
#     db.commit()
#     results = cursor.fetchall()
#     if results:
#         # print results
#         t = np.zeros(shape=(2, 5))
#         for results in results:
#             t[0,:]=results
#             # print results
#     else:
#         print 404
#     print t
#
#
# except:
#     # 发生错误时回滚
#     db.rollback()
#     print 500
#
#     # 关闭数据库连接
# db.close()

