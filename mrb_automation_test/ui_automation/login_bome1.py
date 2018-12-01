#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait

def open_browse():
    """
    open browser obj
    :return:
    """
    browse_obj = webdriver.Chrome()
    return browse_obj

def click_url_and_clicl_loginbtn(browse,url):

    """
    open url and click "登录" btn
    :param browse:
    :param url:
    :return:
    """
    browse.get(url)
    browse.maximize_window()
    loginbtn_lable=browse.find_element_by_link_text("登录")
    loginbtn_lable.click()
    time.sleep(1)

def get_element_label(browse,element_id_dict):
    """
    get element lable
    :param browse:
    :param element_id_dict:
    :return:
    """
    user_label = browse.find_element_by_id(element_id_dict["name"])
    pwd_label = browse.find_element_by_id(element_id_dict.get("pwd"))
    login_label = browse.find_element_by_id(element_id_dict.get("login"))
    return (user_label,pwd_label,login_label)

def send_key_s(lable_tuple,userinfo_dict,userinfo_list):
    """
    send userinfo and logian
    :param lable_tuple:
    :param userinfo_dict:
    :param userinfo_list:
    :return:
    """

    i=0
    if i<=1:
        for key in userinfo_list:
            # lable_tuple[i].send_keys(" ")
            # lable_tuple[i].click()
            lable_tuple[i].send_keys(userinfo_dict.get(key))
            i+=1
            time.sleep(1)

    lable_tuple[2].click()


### 封装数据

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

chrome = open_browse()
click_url_and_clicl_loginbtn(chrome,url)

lable_tuple = get_element_label(chrome,id_dict)

send_key_s(lable_tuple,userinfo_dict,userinfo_list)
