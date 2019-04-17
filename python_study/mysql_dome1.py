# -*- coding=utf-8 -*-
# @Time     :2018/12/27 10:49
# @Author   :ZhouChuqi
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("172.16.20.115", "root", "123456", 'myfirstdata', charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM member_card WHERE member_id= 12"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    print results
    if results:
        for row in results:
            card_no = row[1]
            card_pwd = row[2]
            # 打印结果
            print "card_no=%s,card_pwd=%s" % (card_no, card_pwd)
    else:
        print "查询结果为空"
except Exception, e:
    # 发生错误时回滚
    print "Error to update:", e
    db.rollback()

# 关闭数据库连接
db.close()
