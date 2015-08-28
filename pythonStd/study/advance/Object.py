# coding=utf-8
import types

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score
        
stu = Student('toy', '88')
stu.print_score()
print(stu.get_name())


# oop
class animal(object):
    def __init__(self):
        print('animal init')
        pass
    
    def run(self):
        print('animal run')
    pass

class dog(animal):
    def __init__(self):
        print('dog wang')
        pass
    
    def run(self):
        print('dog run')
    pass

a = dog()
a.run()


# duck typing 
# “当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。”
# 在这种风格中，一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由当前方法和属性的集合决定。
class Refrigerator(object):
    __prinum = 0
    pubnum = 0
    def run(self):
        print('joke')
        pass
    pass

a = Refrigerator()
a.run()
print(isinstance(a, Refrigerator))
print(isinstance(a.run, types.FunctionType))
print(type(abs))
print(type(a))

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir(Refrigerator))

# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
print(hasattr(Refrigerator, 'run'))
print(hasattr(Refrigerator, '__prinum'))
print(hasattr(Refrigerator, 'pubnum'))

# 为对象增加属性
test = Refrigerator()
setattr(test, 'name', 'ArefriG')
str = getattr(test, 'name')
print(test.name)
# 如果试图获取不存在的属性，会抛出AttributeError的错误
# try:
#     getattr(str, 'gender')
