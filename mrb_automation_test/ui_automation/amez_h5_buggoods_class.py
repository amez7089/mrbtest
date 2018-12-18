# coding=utf-8
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re


def amez_h5_buygoods(driver, ReadGoods):
    driver.get('http://mobile.test.amyun.cn/')
    time.sleep(1)
    # 点击搜索栏进入搜索页面
    driver.find_element_by_xpath("//*[@id='app']/div/div[1]/input").click()
    time.sleep(1)
    # 输入要搜索的商品
    driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[1]/form/input").send_keys(ReadGoods, Keys.ENTER)
    time.sleep(3)
    # 查看被搜索出来的商品第一条
    SearchGoods = driver.find_element_by_xpath("//*[@id='app']/div/section[2]/ul/li[1]/div[2]/div[1]").text
    print "SearchGoods:", SearchGoods
    if ReadGoods in SearchGoods:
        print u"搜索商品成功，搜索出的第一条商品为：", SearchGoods
        # 点击商品进入商品详情
        driver.find_element_by_xpath("//*[@id='app']/div/section[2]/ul/li[1]/div[2]/div[1]").click()
        time.sleep(2)
        # 点击立即购买
        # JS点击立即购买按钮
        js = 'document.getElementsByClassName("ljgm")[0].click();'
        driver.execute_script(js)
        time.sleep(2)
        # 选择商品规格
        el = driver.find_element_by_xpath("//*[@id='app']/div/section[8]/section/div[2]/div[1]/div/span[1]")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(1)
        # 75英寸
        el = driver.find_element_by_xpath("//*[@id='app']/div/section[8]/section/div[2]/div[2]/div/span[1]")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(1)
        # 点击确定
        js = 'document.getElementsByClassName("but_full_square_outer")[0].click();'
        driver.execute_script(js)
        time.sleep(3)
        # 确认订单页面点击提交订单
        el = driver.find_element_by_xpath("//*[@id='app']/div/section[6]/button")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(3)
        # 收银台页面选择余额支付
        el = driver.find_element_by_xpath("//*[@id='app']/div/div[1]/section/ul/li[4]/label/span[1]/i[1]")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(1)
        # 确定
        el = driver.find_element_by_xpath("//*[@id='app']/div/div[1]/section/a")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(2)
        # 输入支付密码
        el = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[3]/ul/li[1]")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(0.5)
        el = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[3]/ul/li[2]")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(0.5)
        el = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[3]/ul/li[3]")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(0.5)
        el = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[3]/ul/li[4]")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(0.5)
        el = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[3]/ul/li[5]")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(0.5)
        el = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[3]/ul/li[6]")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(5)
        # 待支付成功后，关掉弹框，查看订单
        el = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div/span")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(1)
        # 获取支付成功元素
        successIcon = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/p').text
        if (successIcon == u"您已支付成功"):
            print u"订单支付成功！！！"
        # 返回首页
        el = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[3]/div[2]')
        driver.execute_script("arguments[0].click();", el)
        time.sleep(2)


def amez_h5_get_ordernumber(driver, ReadGoods):
    # 点击查看订单
    driver.get('http://mobile.test.amyun.cn/mine')
    time.sleep(2)
    el = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/ul/li[2]/div/img')
    driver.execute_script("arguments[0].click();", el)
    time.sleep(3)
    # 在待发货页面，查看订单
    OrderGoods = driver.find_element_by_xpath("//*[@id='app']/div/div/section[1]/div[2]/ul/li/div[2]/p[1]").text
    OrderStatus = driver.find_element_by_xpath("//*[@id='app']/div/div/section[1]/div[1]/span").text
    print "OrderGoods:", OrderGoods
    print "OrderStatus", OrderStatus
    if (ReadGoods in OrderGoods and OrderStatus == u"待发货"):
        el = driver.find_element_by_xpath("//*[@id='app']/div/div/section[1]/div[2]/ul/li/div[2]/p[1]")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(2)
        # 保存订单编号
        OrderNumber = str(
            driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section[3]/div[3]/p/span[1]").text)
        print "OrderNumber:", OrderNumber
        # 提取出订单编号
        OrderNumber = re.findall(r"订单编号：(.*)", OrderNumber)
        # 将提取出的List类型转化为str类型
        OrderNumber = ''.join(OrderNumber)
        print "提取后的OrderNumber:", OrderNumber
        return OrderNumber
