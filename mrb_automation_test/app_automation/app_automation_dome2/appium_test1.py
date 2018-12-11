# coding=utf-8

from appium import webdriver

import time

desired_caps = {

                'platformName': 'Android',

                'deviceName': '30d4e606',

                'platformVersion': '5.0',

                'appPackage': 'com.taobao.taobao',

                'appActivity': 'com.taobao.tao.ContainerActivity',

                }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 休眠五秒等待页面加载完成

time.sleep(2)
driver.find_element_by_id("com.taobao.taobao:id/uik_mdButtonDefaultPositive").click()
time.sleep(5)
driver.find_element_by_id("com.taobao.taobao:id/home_searchedit").click()
time.sleep(5)
driver.find_element_by_id("com.taobao.taobao:id/searchEdit").send_keys('121212wss')
time.sleep(2)
driver.find_element_by_id("com.taobao.taobao:id/searchbtn").click()
time.sleep(2)