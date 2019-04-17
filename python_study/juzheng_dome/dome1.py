# -*- coding=utf-8 -*-
# @Time     :2019/1/5 17:29
# @Author   :ZhouChuqi
# import numpy as np
# # a=np.arange(9).reshape(3,3)
# a = np.zeros(shape=(2,5))
# print a[0]
# b=[2,4,6,2,12]
# c=(1,2,34,3,2)
# a[0,:]=b
# a[1,:]=c
# print a
# def __init__(self, cells):
#     self.cells, self.comments = self._parse(cells)
#
#
def parse():
    data = []
    comments = []
    i=1
    for i in range(1,10):
        if i>5:
            comments.append(i)
        else:
            data.append(i)
    return data,comments
a,b=parse()
print a,b
def csahj():
    data = []
    comments = []
    i=1
    for i in range(1,10):
        if i>5:
            comments.append(i)
        else:
            data.append(i)
    return data,comments
a,b=csahj()
print a,b