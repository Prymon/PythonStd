# coding=utf-8
# map 把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
from _functools import reduce
def normalize(name):
    name = name[:1].upper() + name[1:].lower()
    return name
L = list(map(normalize, ['adam', 'LISA', 'barT']))
print(L)

# reduce Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(a,b):
    return a*b

L1 = [3, 5, 7, 9]
L2 = reduce(prod,L1)
print(L2)

