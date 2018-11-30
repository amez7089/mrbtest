#! /usr/bin/env python
# -*- coding:utf-8 -*-

# from appium import webdriver
#
# desired_caps = {"platformName": "Android",
#                 "deviceName": "127.0.0.1:62001",
#                 "platformVersion": "6.0",
#                 "appPackage": "com.aimeimrb:",
#                 "appActivity": "com.aimeimrb.activity.BootActivity",
#                 }
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# capabilities.setCapability("appWaitActivity", "com.taiyouxi.a3k.MainActivity")"appWaitActivity":"com.tencent.mm.ui.LauncherUI"
from selenium import webdriver
import time

#初始化信息
desired_caps={
                "platformName": "Android",
                "deviceName": "127.0.0.1:62001",
                "platformVersion": "6.0",
                "appPackage": "com.taobao.taobao",
                "appActivity": "com.taobao.tao.homepage.MainActivity3",
                "appWaitActivity": "com.taobao.tao.homepage.MainActivity3"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
#在搜索框输入关键词
driver.find_element_by_id("com.taobao.taobao:id/home_searchedit").click()
# 等待时间
time.sleep(3)
driver.find_element_by_id("com.taobao.taobao:id/searchEdit").send_keys("adidas")
time.sleep(3)
driver.find_element_by_id("com.taobao.taobao:id/searchbtn").click()
#截图
driver.quit()