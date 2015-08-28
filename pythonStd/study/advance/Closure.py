# coding=utf-8
# 相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
# 1 返回一个加法的闭包，可以等用的时候再调
from _ast import Num
def count(*nums):
    def sum():
        sum = 0
        for i in nums:
            sum += i
        return sum
    return sum
total = count(*[1, 2, 3, 4])
print(total())

# 理想结果是1,4,9 实际却是9,9,9
def count1():
    fs = []
    for i in range(1, 4):
        def f():
             return i * i
        fs.append(f)
    return fs
for f in count1():
    print(f(), end=',')
print()

# 需要一个机制保证在闭包运行时用的参数没有变
def count2():
    fs = []
    list = []
    for i in range(1, 4):
        list.append(i)
        def f():
             i1 = list.pop(0)
             return i1 * i1
        fs.append(f)
    return fs
for f in count2():
    print(f(), end=',')
print()
# 或者用函数参数保存
def count3():
    def param(num):
        def f():
            return num*num
        return f
    fs = []
    for i in range(1,4):
        fs.append(param(i))
    return fs
for f in count3():
    print(f(),end=',')
    
    