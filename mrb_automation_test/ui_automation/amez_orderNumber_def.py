# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import re
import amez_pc_login_def


def get_ordernumber(driver):
    # amez_login_def.open_homepage(driver,"http://web.test.amyun.cn/")
    # amez_login_def.get_user_login(driver,"13713948825","123456")
    driver.find_element_by_xpath("//*[@id='app']/div[1]/div/ul/li[2]/div[1]").click()
    time.sleep(1)
    # 因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(2)
    # 待收货页面查看是否有待发货订单
    driver.find_element_by_xpath("//*[@id='am_content']/div/div[2]/div[2]/div/div[3]/div[1]/ul/li[2]/p/span[1]").click()
    # 查看待发货页面第一条数据是否为我们需要的订单
    # 因为窗口变化，所以要定位当前的句柄，不然无法找到元素
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(2)
    # 获取订单号：
    ordernumber = str(driver.find_element_by_xpath(
        "//*[@id='am_content']/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/ul/li/dl/dd[1]").text)
    print "ordernumber:", ordernumber
    # 提取出订单编号
    ordernumber = re.findall(r"订单号：(.*)", ordernumber)
    #     print "ordernumber1:",ordernumber
    #     print type(ordernumber)
    # 将提取出的List类型转化为str类型
    ordernumber = ''.join(ordernumber)
    #     print type(ordernumber)
    print "ordernumber:", ordernumber
    # 保存订单编号
    # ws.write(j, i, ordernumber)
    return ordernumber
