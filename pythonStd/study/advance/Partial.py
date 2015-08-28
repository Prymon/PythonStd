#coding=utf-8
'a test module for partial'
__author__ = 'Deamon'

# 通过设定参数的默认值，可以降低函数调用的难度
import functools
str = int('100',base=16)
print(str)

int2 = functools.partial(int,base=16)
print(int2('100'))

# 也可以传递参数
n = max(1,2,3,4)
print(n)

max2 = functools.partial(max,10)
n = max2(1,2,3,4)
print(n)