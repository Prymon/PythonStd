# coding=utf-8
#dict
from _collections_abc import Iterable
dict = {'name':'admin','passwd':'123456','age':11}
print(dict['name'],dict['age'])

group = {'root':['male',18,'coder'],'Tom':['female','22','doc']}
if 't' in group:
    print('t in group')
if group.get('Tom'):
    print(group['Tom'])
else:
    print('wrong name')
    
    
# set set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
set = set([3,2,1])
set.add(4)
set.add(('a','b'))
print(set)

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
# 1
for key,values in d.items():
    print(key,':',values,end=' | ')
print()
# 2
for key in d:
    print(key,':',d[key],end=' | ')
print()
# 3
if isinstance(d, Iterable):
    for k,v in enumerate(d):
        print(k,':',v,end=' | ')
    print()
else:
    pass

        
        
        
        
        
        
        
        
        
        
        
        
        