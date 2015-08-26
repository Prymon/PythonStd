# coding=utf-8
from email._header_value_parser import Group
from _ast import Tuple
from _collections_abc import Iterable
user1 = ['admin','admin','male',18]
user2 = ['root','root','female']

user2.append(18)
user2[1] = '123456'
user2.pop()
user2.insert(3,22)
print(user1,'\n',user2)
print(user1[0],user1[1],user1[2],user1[3])
print(user1[-1],user1[-2],user1[-3],user1[-4])
print(user1+user2)



# Two dimensional array
group = [user1,user2]
print(group,group[0][3])

# 列表生成式
# 1
list1 = [];
for n in range(5,9):
    list1.append(n)
print(list1)

# 2
list2 = list(range(5,10))
print(list2)

# 3
list3 = list(x for x in range(10) if x%3!=0)
print(list3)

# 4
list4 = list(x+"-"+y for x in 'ABC' for y in 'EF')
list4 = [x+"-"+y for x in 'ABC' for y in 'EF']
print(4,list4)
    
# 5
list5 = list(x.lower() for x in list4)
print(list5)

# 6
list6 = list(list5)
list6.insert(0, '===')
print(list6,list5)

# 7
list7 = list6[:]
print(list7)

# 8
list8 = list7[1:3]
list8.append('123');
print(list8,list7) 

