"""
面向对象原则的核心：开发和封闭原则。对扩展开发，对修改封闭。
作用：在不改变原函数（或对象）内部代码和方法的情况下，为原函数添加新功能。
引用场景：登录校验，函数运行时间统计，函数执行前准备和执行后数据清理工作。
"""


# 普通装饰器
import time


def longin(func):
    def demo():
        name = str(input("name:"))
        pwd = str(input("pwd:"))
        # 这里引用了外部变量，就不属于闭包
        if name == "ikun" and pwd == "123":
            print('执行func函数')
            func()
        else:
            print('不会执行 func函数')

    return demo


@longin
def index():
    print('继续执行 index()')


# index()


# 带参数的装饰器又有返回值
def add(func):
    def add_num(a: str, b: str):
        print('执行add_num')
        c = func()
        return a + b + str(c)

    return add_num


@add
def demo():
    return 'c'


n = demo('a', 'b')
print(n)


# Output: abc


# 标准化有得到了通用装饰器：
def add2(func):
    def add_num(*args, **kwargs):
        print(args, kwargs)
        text = func(*args, **kwargs)
        return text + 'add_num_%s_%s \n' % (args, kwargs)

    return add_num


@add2
def demo2(*args, **kwargs):
    text = 'demo2_%s_%s \n' % (args, kwargs)
    return text


n = demo2('a', 'b')
print(n)


# ('a', 'b') {}
# demo2_('a', 'b')_{}
# add_num_('a', 'b')_{}


# 类装饰器 将类当作参数传入装饰器中：
def add_cls(cls):
    def add_cls_num(*args, **kwargs):
        print('装饰器：add_cls.add_cls_num: %s_%s' % (args, kwargs))
        cls.info = '装饰器添加的属性'
        return cls(*args, **kwargs)

    return add_cls_num


@add_cls
class Test:
    def __init__(self, a):
        print('类的__init__', a)


test = Test('a')
print(test.info)
"""
# Output: 装饰器：add_cls.add_cls_num: ('a',)_{}
# Output: 类的__init__ a
# Output: 装饰器添加的属性
"""


# 函数运行时间统计:
def timer(func):
    def timer_demo(*args, **kwargs):
        t1 = time.time()
        text = func(*args, **kwargs)
        t2 = time.time()
        print('运行时长：', t2-t1)
        return text + 'timer_%s_%s \n' % (args, kwargs)
    return timer_demo


@add2
@timer
def test_timer(*args, **kwargs):
    time.sleep(1)
    text = 'demo2_%s_%s \n' % (args, kwargs)
    return text


test_text = test_timer()
print(test_text)
"""
() {}
运行时长： 1.009666919708252
demo2_()_{} 
timer_()_{} 
add_num_()_{} 
"""


# 使用类实现装饰器
class Decorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Decorator.__call__')
        self.func()


@Decorator
def test_decorator():
    print('test_decorator')


test_decorator()