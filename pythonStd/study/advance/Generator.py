# coding=utf-8
# 列表生成式
L = [x for x in 'ABC'];
print(L)

# 列表元素可以按照某种算法推算出来，那我们可以在循环的过程中不断推算出后续的元素,这种机制，称为生成器：generator
# 1
G = (x for x in range(1000) if x*x%86==0)
for t in G:
    print(t,end=' ')
print()
# 2
def Feibo(n):
    a = 0
    b = 1
    print(b)
    for i in range(1,n):
        a,b = b,a+b
        print(b)
Feibo(3)
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
# fib(5)