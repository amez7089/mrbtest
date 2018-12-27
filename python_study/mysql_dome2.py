# -*- coding=utf-8 -*-
# @Time     :2018/12/27 11:27
# @Author   :ZhouChuqi
import MySQLdb

# Script starts from here

# 连接数据库
# db_conn = MySQLdb.connect(host='192.168.18.128', user='root', passwd='123456')

# 如果已经创建了数据库，可以直接用如下方式连接数据库
db_conn = MySQLdb.connect(host = '192.168.18.128', user = 'root',passwd = '123456', db = 'dbtest')
# db_conn = MySQLdb.connect("192.168.18.128", "root", "123456",'myfirstdata', charset='utf8')

"""
connect方法常用参数:
 host: 数据库主机名.默认是用本地主机
 user: 数据库登陆名.默认是当前用户
 passwd: 数据库登陆的秘密.默认为空
 db: 要使用的数据库名.没有默认值
 port: MySQL服务使用的TCP端口.默认是3306
 charset: 数据库编码
"""

# 获取操作游标
cursor = db_conn.cursor()

# 使用 execute 方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone 方法获取一条数据库。
dbversion = cursor.fetchone()

print "Database version : %s " % dbversion

# 创建数据库
cursor.execute("create database if not exists dbtest")

# 选择要操作的数据库
db_conn.select_db('dbtest');

# 创建数据表SQL语句
sql = """CREATE TABLE if not exists employee(
   first_name CHAR(20) NOT NULL,
   last_name CHAR(20),
   age INT, 
   sex CHAR(1),
   income FLOAT )"""

try:
    cursor.execute(sql)
except Exception, e:
    # Exception 是所有异常的基类，这里表示捕获所有的异常
    print "Error to create table:", e

# 插入数据
sql = """INSERT INTO employee(first_name,
   last_name, age, sex, income)
   VALUES ('%s', '%s', %d, '%s', %d)"""

# Sex: Male男, Female女

employees = (
    {"first_name": "Mac", "last_name": "Mohan", "age": 20, "sex": "M", "income": 2000},
    {"first_name": "Wei", "last_name": "Zhu", "age": 24, "sex": "M", "income": 7500},
    {"first_name": "Huoty", "last_name": "Kong", "age": 24, "sex": "M", "income": 8000},
    {"first_name": "Esenich", "last_name": "Lu", "age": 22, "sex": "F", "income": 3500},
    {"first_name": "Xmin", "last_name": "Yun", "age": 31, "sex": "F", "income": 9500},
    {"first_name": "Yxia", "last_name": "Fun", "age": 23, "sex": "M", "income": 3500}
)

try:
    # 清空表中数据
    cursor.execute("delete from employee")
    # 执行 sql 插入语句
    for employee in employees:
        cursor.execute(sql % (employee["first_name"], \
                              employee["last_name"], \
                              employee["age"], \
                              employee["sex"], \
                              employee["income"]))
    # 提交到数据库执行
    db_conn.commit()
    # 对于支持事务的数据库， 在Python数据库编程中，
    # 当游标建立之时，就自动开始了一个隐形的数据库事务。
    # 用 commit 方法能够提交事物
except Exception, e:
    # Rollback in case there is any error
    print "Error to insert data:", e
    # b_conn.rollback()

print "Insert rowcount:", cursor.rowcount
# rowcount 是一个只读属性，并返回执行execute(方法后影响的行数。)

# 数据库查询操作:
# fetchone()  得到结果集的下一行
# fetchmany([size=cursor.arraysize]) 得到结果集的下几行
# fetchall()  返回结果集中剩下的所有行
try:
    # 执行 SQL
    cursor.execute("select * from employee")

    # 获取一行记录
    rs = cursor.fetchone()
    print rs

    # 获取余下记录中的 2 行记录
    rs = cursor.fetchmany(2)
    print rs

    # 获取剩下的所有记录
    ars = cursor.fetchall()
    for rs in ars:
        print rs
    # 可以用 fetchall 获得所有记录，然后再遍历
except Exception, e:
    print "Error to select:", e

# 数据库更新操作
sql = "UPDATE employee SET age = age + 1 WHERE sex = '%c'" % ('M')
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    db_conn.commit()
    cursor.execute("select * from employee")
    ars = cursor.fetchall()
    print "After update: ------"
    for rs in ars:
        print rs
except Exception, e:
    # 发生错误时回滚
    print "Error to update:", e
    db_conn.rollback()
# 关闭数据库连接
db_conn.close()
