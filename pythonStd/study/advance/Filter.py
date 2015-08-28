# coding=utf-8
# filter
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 10)))
print(L)


# sorted 假设我们用一组tuple表示学生名字和成绩：根据成绩排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[1]

# 升序
L2 = list(sorted(L, key=by_name))
print(L2)
# 降序
L3 = list(sorted(L, key=by_name, reverse=True))
print(L3)
    
