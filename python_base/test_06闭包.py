"""

闭包三个条件：
1.函数中嵌套函数 2.内函数引用外函数的自由变量（非全局变量） 3.外函数返回内函数的引用。
"""


def login(num1):  # 外函数
    # 非全局变量
    num2 = 2

    def demo():  # 内函数
        print(num1)

        print(num2)
        # login.num2变量被封闭在了demo函数里面，形成了闭包
        # 作用：实现数据的锁定，提高程序的稳定性，一般搭配装饰器使用。

    return demo


# 在这里获得一个闭包
res = login(10)
# 执行内函数
res()
print(res.__closure__)


def line_conf(a, b):
    def line(x):
        return a * x + b

    return line


# 定义两条直线
line_a = line_conf(2, 1)  # line() = 2 * x + 1
line_b = line_conf(3, 2)  # line() = 3 * x + 2

# 执行打印x对应的y值
print(line_a(3))
print(line_b(5))
print("==" * 20)

# 问题代码：
ls1 = []
for i in range(3):
    def func(a):
        return i + a
    ls1.append(func)  # [0+a,1+a,2+a]

for j in ls1:
    print(j(1))
    """
    Output: 3
    Output: 3
    Output: 3
    """

# 闭包解决问题
ls1 = []
for i in range(3):
    def func(j):
        def demo(a):
            return j + a
        return demo
    ls1.append(func(i))

for j in ls1:
    print(j(1))
    """
    Output: 1
    Output: 2
    Output: 3
    """
