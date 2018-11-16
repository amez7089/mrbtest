#coding=utf-8
# i = 1
# while i<6:
#     str='/html/body/div[17]/div[2]/div/div/div[2]/div/form/div['
#     str1= ']/div/div[1]/input'
#     i=bytes(i)
#     print(i)
#     # xp = '/html/body/div[17]/div[2]/div/div/div[2]/div/form/div[' + i + ']/div/div[1]/input'
#     # i=bytes(i)
#     xp=str+i+str1
#     print(xp)
#     i=int('i')
#     i=i+1
# i=1
# a=i+1
# i=str(i)
# # b=i+2
# print(i,a)
# i=int(i)
# # print(i,a)
# i=1
# while i<6:
#     i=str(i)
#     xp = '/html/body/div[17]/div[2]/div/div/div[2]/div/form/div[' + i + ']/div/div[1]/input'
#     print(xp)
#     i=int(i)
# #     i=i+1
# #     print(i)
#
# tup = ('physics', 'chemistry', 1997, 2000)
#
# print tup
# del tup
# print "After deleting tup : "
# print tup
#
# s='ahskashk'
# print ("The 你好 length of %s" %s)
# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.sucaijiayuan.com/api/demo.php?url=/demo/20150325-1')
driver.maximize_window()

driver.switch_to.frame('iframe')

driver.find_element_by_id('message1').send_keys('Hello world!')  # 很简单，直接send_keys就行
sleep(2)

print driver.find_element_by_id('message1').get_attribute('value')

driver.quit()