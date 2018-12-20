# -*- coding:utf-8 -*-
import random
import string
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def generate_random_str(randomlength):
    """
    生成指定长度的随机字符串

    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str


def generata_random_title():
    """
    生成指定长度的随机字符串

    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789a'u'美'u'容'u'养'u'颜'u'阿'u'卡'u'手'u'机'u'号'u'卡'u'扣'u'式'u'爱'u'啥'
    length = len(base_str) - 1
    for i in range(4):
        random_str += base_str[random.randint(0, length)]
    title = "自动化课程%s" % random_str
    print title
    return title

ti=str(generata_random_title())
t2=generate_random_str(12)
print ti
print t2