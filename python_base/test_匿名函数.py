"""
【匿名函数】
lambda (纳莫达)
一种特殊函数，不需要def来定义，也不要函数名。用lambda表达式来定义。
格式：lambda 参数：表达式（返回值）
使用场景：简单的函数定义，只有一个表达式。
"""


def demo(num):
    num += 1
    return num


conf = lambda num: num + 1
print(conf(3))
