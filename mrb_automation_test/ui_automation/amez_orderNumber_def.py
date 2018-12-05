# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import amez_login_def
def get_ordernumber():
    browse_obj = webdriver.Chrome()
    return browse_obj