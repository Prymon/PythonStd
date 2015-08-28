# coding=utf-8
def add(*num):
    sum = 0
    for i in num:
        sum+=i
        pass
    print(sum)
    return sum

def Fab(a,b,f):
    return f(a,b)
    
Fab(1, 2, add)


