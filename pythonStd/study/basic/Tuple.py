# coding=utf-8
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
gender = ('male','female')
emtpy = ()
one = ('one',)      # 括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算
# gender[0] = 1 #这样会报错
print(gender)
print(emtpy)
print(one)