# coding=utf-8
# NORMAL
def add(a, b):
    return a + b
print(add(1, 2))
print(add(*(1, 2)))

# 默认参数
def power(x, n=2):
    sum = 1
    for i in range(n):
        sum *= x
    return sum
print(power(0), end=' | ')
print(power(2, 3), end=' | ')
print(power(2, n=4), end=' | ')

# 可变参数
def Ad_add(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum
L1 = Ad_add(1, 2, 3, 4)
L2 = Ad_add(*[1, 2, 3, 4])
print(L1, ' | ', L2)

# 关键字参数
def person(name, age, **msg):
    if 'gender' in msg:
        print(msg['gender'])
        pass
    pass
L = person('a', 'b', gender='male')
L = person('a', 'b', **{'gender':'male'})
L = person( *['a','b'],**{'gender':'female'})




