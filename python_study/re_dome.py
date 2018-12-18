#coding=utf-8
import re
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
strdome='匹配规则刷卡啥可BSAssaksl是匹配规则则飒飒很快就啥课kjhaKLAO则的SA212哈尽ASA12快哈ASAS454asj及匹配规则哈可是222匹配规则'
a = re.findall("匹配规则",strdome)
b=re.findall("^匹配规则",strdome)
print strdome
print "a:",a
print "b:",b
c=re.findall("a-z",strdome)
print "c:",c
d =re.findall("[a-z]",strdome)
print "d:",d
e=re.findall("0-9",strdome)
print "e:",e
pattern = re.compile(ur'0?(13|14|15|18|17|19)[0-9]{9}')
str = u'19212345678'
print(pattern.search(str))
