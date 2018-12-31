#coding=utf-8
# from selenium import webdriver
# import time
# from selenium.webdriver.support.ui import WebDriverWait
import amez_pc_login_def
import amez_orderNumber_def
driver = amez_pc_login_def.open_browse()
amez_pc_login_def.open_homepage(driver, "http://web.test.amyun.cn/")
amez_pc_login_def.get_user_login(driver, "13713948825", "123456")
ordernumber = amez_orderNumber_def.get_ordernumber(driver)
print ordernumber
driver.quit()
