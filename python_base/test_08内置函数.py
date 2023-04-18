"""
Python内置函数有很多，包括但不限于以下功能类别：
1. 数学函数
2. 字符串函数
3. 列表操作函数
4. 文件处理函数
5. 网络编程函数
6. 输入输出函数
7. 时间日期函数
一些常见的有：
map、filter、zip
"""

# map
"""
【map】 (慢不)
map函数是一个内置函数，它对可迭代对象进行迭代，并将其元素传递给指定的函数进行处理，返回处理后的结果组成的列表。
"""
# map(function, iterable)
# 其中，function是用于处理元素的函数，iterable是可迭代对象，如列表或元组。
lst = [1, 2, 3, 4, 5]


def square(num):
    return num*num


squared_lst = map(square, lst)
print(list(squared_lst))

"""
【filter】 （翻的）

"""
# 需求：去掉list中不属于str的元素
test_list = ['a', 'b', 'c', 1, 4, False]


test_filter = filter(lambda x: isinstance(x, str), test_list)
print(list(test_filter))