#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait

import login_bome1

url = "http://www.amez999.com/"
# id_dict = {0
#     "name":"id_account_l",
#     "pwd" : "id_password_l",
#     "login":"login_btn",
# }
#
login_bome1.userinfo_dict={
    "name" : "13713948825",
    "pwd" : "123456",
    "url" : "http://www.amez999.com/",
}

# # 函数使用

login_bome1.userinfo_list =["name","pwd"]

chrome = login_bome1.open_browse()
login_bome1.click_url_and_clicl_loginbtn(chrome,url)

lable_tuple = get_element_label(chrome,id_dict)

send_key_s(lable_tuple,userinfo_dict,userinfo_list)
