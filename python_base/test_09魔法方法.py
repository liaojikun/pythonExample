
"""

"""


# __new__
# 实例化的时候先调用这个方法，创建并返回对象，再调用__init__()

class TestCase(object):

    def __new__(cls, *args, **kwargs):
        print('__new__')
        return object.__new__(cls)

    def __init__(self):
        print('__init__')


TestCase()


# 单例模式
class TestCaseOne(object):
    # 标记类是否被实例化过，默认没有
    instance = None

    def __new__(cls, *args, **kwargs):
        # 如果被实例化过了,就直接返回上次实例化的对象
        if cls.instance is not None:
            return cls.instance
        else:
            cls.instance = object.__new__(cls)
            return cls.instance

    def __init__(self):
        print(self.instance)


TestCaseOne()
TestCaseOne()
TestCaseOne()


def is_instance_cls(cls):
    cls.__instance = None

    def is_instance(*args, **kwargs):
        if cls.__instance is not None:
            return cls.__instance
        else:
            cls.__instance = object.__new__(cls)
            return cls.__instance
    return is_instance


@is_instance_cls
class TestOne(object):

    def __init__(self):
        self.name = 'TestOne'
        print('TestOne.__init__')


a = TestOne()
print(a.name)

