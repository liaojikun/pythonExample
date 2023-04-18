"""
【生成器】 yield（耶的）
Python生成器是一种特殊的Python函数，它允许你逐步地生成结果，而不是一次性生成所有结果。
生成器使用yield语句而不是return语句来返回结果，可以在使用时生成一系列的值，
而不是一次性生成所有结果。生成器在以下情况非常有用。

总结：延迟计算，一次返回一个结果，不会一次生成所有结果。对于大数据量逐行处理非常有用。
"""
# 生成器有两种方式：在函数使用yield和表达式
# 生成器表达式：
tu = (i for i in range(1, 11))
print(type(tu))  # 不是 tuple
# next 执行一次取一个，执行一次生成一个，不会一次生成所有
print(next(tu))
print(next(tu))


# 生成器在函数中使用yield：
def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()
# print(next(gen))  # Output: 1
# print(next(gen))  # Output: 2
# print(next(gen))  # Output: 3

"""
先了解【可迭代对象】 
如果一个对象有__iter__() (衣特)方法，那这个对象就是可以迭代对象。

【迭代器】 for语句之所以可以遍历，就是以为背后迭代器的支持。
一个对象有__iter__()和__next__()，就是一个迭代器。（迭代器协议）
它可以遍历一个序列中的所有元素。迭代器可以用来遍历任何可迭代对象，如列表、元组、字典等。

具体来说，__iter__()返回迭代器对象本身，并准备开始迭代。__next__()返回序列中下一个元素的值，
如果没有更多元素则抛出StopIteration异常。（for语句会自动捕捉这个异常，并把它当作结束遍历的标志）。
总结：用很少的内存就可以存放和处理很超大量数据。用多少 取多少。（惰性加载/延迟加载）
"""


class MyIterator:
    def __init__(self, lst):
        self.index = 0
        self.lst = lst

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.lst):
            value = self.lst[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


lst = [1, 2, 3, 4, 5]
my_iterator = MyIterator(lst)
for item in my_iterator:
    print(item)

