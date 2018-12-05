# coding=utf-8
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


def open_homepage(browse, url):
    """
    open url and click "登录" btn
    :param browse:
    :param url:
    :return:
    """
    browse.get(url)
    browse.maximize_window()
    time.sleep(1)


def get_user_login(browse, name,pwd):
    """
    get element lable
    :param browse:
    :param element_id_dict:
    :return:
    """
    browse.find_element_by_xpath('//*[@id="app"]/div[1]/div/ul/li[1]').click()
    time.sleep(2)
    browse.find_element_by_xpath('//*[@id="am_content"]/div/div[2]/div/div[2]/div[2]/div[1]/input').send_keys(
        name)
    browse.find_element_by_xpath('//*[@id="am_content"]/div/div[2]/div/div[2]/div[2]/div[2]/input').send_keys(
        pwd)
    # browse.find_element_by_xpath('//*[@id="am_content"]/div/div[2]/div/div[2]/div[2]/div[1]/input').send_keys(userinfo_dict["name"])
    # browse.find_element_by_xpath('//*[@id="am_content"]/div/div[2]/div/div[2]/div[2]/div[2]/input').send_keys(userinfo_dict["pwd"])
    browse.find_element_by_xpath('//*[@id="loginBtn"]').click()
    time.sleep(1)
    browse.implicitly_wait(30)
    # 判断是否登录成功，如果左上角出现“欢迎来到艾美e族商城”，则判断用户登录成功
    text = browse.find_element_by_class_name("left").text
    print text
    if (text == u"欢迎来到艾美e族商城"):
        print u'登陆成功'
    else:
        print u'登陆失败'
    return
# def get_login_if(browse):
#     time.sleep(1)
#     browse.implicitly_wait(30)
#     # 判断是否登录成功，如果左上角出现“欢迎来到艾美e族商城”，则判断用户登录成功
#     text = browse.find_element_by_class_name("left").text
#     print text
#     if (text == u"欢迎来到艾美e族商城"):
#         print u'登陆成功'
#     else:
#         print u'登陆失败'
#     return


### 封装数据

# url = "http://www.amez999.com/"
# userinfo_dict={
#         "name" : "13713948825",
#          "pwd" : "123456"
# }

# 函数使用
# amez_pc_test = open_browse()
# open_homepage(amez_pc_test,"http://www.amez999.com/")
# lable_tuple = get_user_login(amez_pc_test,"13713948825","123456")

