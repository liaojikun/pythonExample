"""
【递归函数】
函数内部调用自己。
"""


# 示例：
def demo(test_num: int):
    if test_num <= 1:
        return test_num
    else:
        demo_num = demo(test_num - 1)
        return test_num * demo_num


n = demo(4)
print(n)
