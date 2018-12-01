#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait

import login_bome1

url = "http://www.maiziedu.com/"
id_dict = {
    "name":"id_account_l",
    "pwd" : "id_password_l",
    "login":"login_btn",
}

userinfo_dict={
    "name" : "helloyiwantong@163.com",
    "pwd" : "helloyiwantong@1234",
    "url" : "http://www.maiziedu.com/",
}

# 函数使用

userinfo_list =["name","pwd"]

# chrome = open_browse()
# click_url_and_clicl_loginbtn(chrome,url)
#
# lable_tuple = get_element_label(chrome,id_dict)
#
# send_key_s(lable_tuple,userinfo_dict,userinfo_list)
