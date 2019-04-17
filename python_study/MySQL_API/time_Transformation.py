# -*- coding=utf-8 -*-
# @Time     :2019/1/5 14:16
# @Author   :ZhouChuqi
# import time
# a = "2018-04-27 17:49:00"
# timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
# timeStamp = int(time.mktime(timeArray))#1524822540
# print timeStamp
# print a
# print  timeArray
from turtle import *


def nose(x, y):  # 鼻子
    penup()  # 提起笔
    goto(x, y)  # 定位
    pendown()  # 落笔，开始画
    setheading(-30)  # 将乌龟的方向设置为to_angle/为数字（0-东、90-北、180-西、270-南）
    begin_fill()  # 准备开始填充图形
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            left(3)  # 向左转3度
            forward(a)  # 向前走a的步长
        else:
            a = a - 0.08
            left(3)
            forward(a)
    end_fill()  # 填充完成

    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()
    pencolor(255, 155, 192)  # 画笔颜色
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)  # 返回或设置pencolor和fillcolor
    end_fill()

    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()


def head(x, y):  # 头
    color((255, 155, 192), "pink")
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    begin_fill()
    setheading(180)
    circle(300, -30)
    circle(100, -60)
    circle(80, -100)
    circle(150, -20)
    circle(60, -95)
    setheading(161)
    circle(-300, 15)
    penup()
    goto(-100, 100)
    pendown()
    setheading(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            lt(3)  # 向左转3度
            fd(a)  # 向前走a的步长
        else:
            a = a - 0.08
            lt(3)
            fd(a)
    end_fill()


def cheek(x, y):  # 腮
    color((255, 155, 192))
    penup()
    goto(x, y)
    pendown()
    setheading(0)
    begin_fill()
    circle(30)
    end_fill()


def mouth(x, y):  # 嘴
    color(239, 69, 19)
    penup()
    goto(x, y)
    pendown()
    setheading(-80)
    circle(30, 40)
    circle(40, 80)


def setting():  # 参数设置
    pensize(4)
    hideturtle()  # 使乌龟无形（隐藏）
    colormode(255)  # 将其设置为1.0或255.随后 颜色三元组的r，g，b值必须在0 .. cmode范围内
    color((255, 155, 192), "pink")
    setup(840, 500)
    speed(10)


def main():
    setting()  # 画布、画笔设置
    nose(-100, 100)  # 鼻子
    head(-69, 167)  # 头
    # ears(0, 160)  # 耳朵
    # eyes(0, 140)  # 眼睛
    cheek(80, 10)  # 腮
    mouth(-20, 30)  # 嘴
    done()


if __name__ == '__main__':
    main()
