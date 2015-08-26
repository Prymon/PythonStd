# coding=utf-8
from email._header_value_parser import Group
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