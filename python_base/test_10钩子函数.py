"""
python hook 机制

钩子函数（hook function）是一种在特定事件发生时被调用的函数。
在Python中，钩子函数通常被用来在程序运行过程中修改现有的程序行为。
例如，Python中的Tkinter库（用于GUI编程）中有许多钩子函数。
当用户单击按钮、关闭窗口或者输入文本时，这些钩子函数可以被自定义来实现特定的行为。
另一个常见的用途是在Python中创建自定义模块时使用钩子函数。在导入模块时，
可以使用特殊的钩子函数来控制模块的加载过程。这样可以实现很多高级的功能，比如动态的模块加载、模块缓存等。
总之，钩子函数是Python中非常重要的一种编程工具，可以为程序添加灵活性和可扩展性。

钩子函数:就是把我们自己实现的hook函数在某一时刻挂接到目标挂载点上。

hook函数：就是我们自己实现的函数，函数类型与挂载点匹配（返回值，参数列表）
挂接：也就是hook或者叫注册（register）,使得hook函数对目标可用
目标挂载点：也就是挂我们hook函数的地方
"""
import time


class LazyPerson(object):
    def __init__(self, name):
        self.name = name
        self.watch_tv_func = None  # 目标挂载点
        self.have_dinner_func = None  # 目标挂载点

    def get_up(self):
        """起床"""
        print("%s 起床在:%s" % (self.name, time.time()))

    def go_to_sleep(self):
        """睡觉"""
        print("%s 去睡觉:%s" % (self.name, time.time()))

    def register_tv_hook(self, watch_tv_func):  # 挂接
        """注册看电视的钩子函数"""
        self.watch_tv_func = watch_tv_func

    def register_dinner_hook(self, have_dinner_func):
        """注册吃晚餐的钩子函数"""
        self.have_dinner_func = have_dinner_func

    def enjoy_a_lazy_day(self):
        """一天的生活"""
        self.get_up()
        time.sleep(2)
        # 如果注册了钩子函数
        if self.watch_tv_func is not None:
            self.watch_tv_func(self.name)
        else:  # 没有注册钩子函数
            print("没有电视可看")

        time.sleep(2)
        # have dinner --> check the have_dinner_func(hooked or unhooked) --> hooked
        if self.have_dinner_func is not None:
            self.have_dinner_func(self.name)
        else:  # 脱钩
            print("晚餐没什么可吃的")

        time.sleep(2)
        self.go_to_sleep()


def watch_daydayup(name):  # hook函数
    print("%s : 他编程---天向上---很有趣!!!" % name)


def watch_happyfamily(name):
    print("%s : 节目---幸福家庭---很无聊!!!" % name)


def eat_meat(name):
    print("%s : 肉很好吃!!!" % name)


def eat_hamburger(name):
    print("%s : 汉堡包还不错!!!" % name)


def test():
    lazy_tom = LazyPerson("Tom")
    lazy_jerry = LazyPerson("Jerry")

    # register hook 寄存器挂钩
    lazy_tom.register_tv_hook(watch_daydayup)
    lazy_tom.register_dinner_hook(eat_meat)

    lazy_jerry.register_tv_hook(watch_happyfamily)
    lazy_jerry.register_dinner_hook(eat_hamburger)

    # enjoy a day 享受一天
    lazy_tom.enjoy_a_lazy_day()
    lazy_jerry.enjoy_a_lazy_day()


test()
