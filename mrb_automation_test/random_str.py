#-*- coding:utf-8 -*-
import  random
import  string
def generate_random_str(randomlength=16):
    """
    生成指定长度的随机字符串

    """
    random_str=''
    base_str='ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length=len(base_str)-1
    for i in range(randomlength):
        random_str +=base_str[random.randint(0,length)]
    return random_str
def generata_random_title():
    """
    生成指定长度的随机字符串

    """
    random_str=''
    base_str='ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length=len(base_str)-1
    for i in range(4):
        random_str +=base_str[random.randint(0,length)]
    title="自动化课程%s"%random_str
    return title