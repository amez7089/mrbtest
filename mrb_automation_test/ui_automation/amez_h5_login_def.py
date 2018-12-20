# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys


def open_browse(loginadress, model):
    # 定义H5机型
    mobile_emulation = {'deviceName': model}
    # 打开谷歌浏览器
    options = webdriver.ChromeOptions()
    time.sleep(2)
    options.add_experimental_option('mobileEmulation', mobile_emulation)
    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    # 打开商城登录地址
    time.sleep(2)
    driver.get(loginadress)
    return driver


def login_member(driver, username, password):
    driver.get('http://mobile.test.amyun.cn/accountLogin')
    # 跳转至登录页面输入用户名密码,登录
    driver.find_element_by_xpath("//*[@id='accountLogin']/div[2]/div[1]/input").send_keys(username)
    driver.find_element_by_xpath("//*[@id='accountLogin']/div[2]/div[2]/input").send_keys(password, Keys.ENTER)
    time.sleep(2)
