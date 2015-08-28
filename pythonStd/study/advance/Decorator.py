# 1.无参数的Decorator
import functools
def log1(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
@log1
def now():
    print('method 1')
now()
print(now.__name__)
print()

# 带参数的Decorator,被装饰过的原方法的__name__会改变，这样可能导致依赖函数签名的代码执行出错
def log2(str):
    def decorator(method):
        def warpper(*args, **kw):
            print('calls %s(),message:%s' % (method.__name__ , str))
            return method(*args, **kw)
        return warpper
    return decorator

@log2('decorator with param')
def execute():
    print('method 2')
execute()
print(execute.__name__) 
print()

# 最终的装饰方法，使用 @functools.wraps(func)
def log3(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        result = func(*args, **kw)
        print('call over')
        return result
    return wrapper

@log3
def run():
    print('method 1')
run()
print(run.__name__)
print()

# 再思考一下能否写出一个@log的decorator，使它既支持：
def log4(*msg):
    def decorator(func):
        @functools.wraps(func)
        def warpper(*args, **kw):
            for str in msg:
                print('msg : %s' % str)
            print('call method %s'%func.__name__)
            return func(*args,**kw)
        return warpper
    return decorator

@log4('xixi')
def start():
    print('method 2')

start()
print(start.__name__)


