#-*-coding:utf-8-*-
import requests

# with open('2.jpg','wb')as f:
#     url="https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike92%2C5%2C5%2C92%2C30/sign=c2075516ae0f4bfb98dd960662261395/5ab5c9ea15ce36d3953cb9b930f33a87e950b17a.jpg"
#     r=requests.get(url)
#     f.write(r.content)
import re
url="https://lol.qq.com/biz/hero/champion.js"
r=requests.get(url)
ret=r.content.decode()
print (ret)
