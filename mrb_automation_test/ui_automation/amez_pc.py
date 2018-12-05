#coding=utf-8
# from selenium import webdriver
# import time
# from selenium.webdriver.support.ui import WebDriverWait
import amez_login_def
driver = amez_login_def.open_browse()
amez_login_def.open_homepage(driver,"http://www.amez999.com/")
amez_login_def.get_user_login(driver,"13713948825","123456")
# amez_login_def.get_login_if(driver)

