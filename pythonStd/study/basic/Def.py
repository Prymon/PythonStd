# coding=utf-8
from _collections_abc import Iterable
def test(id,passwd,**hobby):
    print(hobby)

def test2(name,*,a,b,c=2):
    print(a,b,c)
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

dictx = {'gender':'22','age':'2'}
test('addd','111',**dictx)
test2('addd',**{'a':2,'b':3})
print(fact(700))

list = [];
for n in range(5,9):
    list.append(n)
print(list)
d = {'a': 1, 'b': 2, 'c': 3}
for key,values in d.items():
    print(key,values)
    
print(isinstance(d, Iterable))