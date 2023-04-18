import logging
import requests
"""
钩子函数（hook function），可以理解是一个挂钩，作用是有需要的时候挂一个东西上去。
具体的解释是：钩子函数是把我们自己实现的hook函数在某一时刻挂接到目标挂载点上

应用场景: 相信你对钩子函数并不陌生。我在 requests 和 mitmproxy 都有看到类似的设计。

"""
# requests 使用hook
r = requests.get("https://httpbin.org/get")
print(r.status_code)
# print(r.content)
# print(r.text)


# 打印状态码，这个动作，我们可以封装到一个函数里，然后作为钩子函数传给requests 使用。
def status_code(response, *args, **kwargs):
    # 作为一个函数，可以做的事情很多，比如，进一步判断状态码，打印响应的数据，甚至对相应的数据做加解密等处理。
    print(response.status_code)


# 把打印状态码封装到一个status_code() 函数中，在requests.get() 方法中通过hooks 参数接收钩子函数status_code()。
r = requests.get("https://httpbin.org/get", hooks={"response": status_code})
# print(r.text)


def decrypt_response(response, *args, **kwargs):
    # print(response.text) 原始数据

    class NewResponse:
        text = '{"code": 0, "data": {"token": "yo yo"}}'  # response.text解密
        history = response.history
        raw = response.raw
        is_redirect = response.is_redirect
        content = b'{"code": 0, "data": {"token": "yo aa"}}'  # response.text解密
        elapsed = response.elapsed

        @staticmethod
        def json():
            # 拿到原始的response.json() 后解码
            return {"code": 0, "data": {"token": "yo yo"}}

        @property
        def info_test(self):
            return 'info'

    return NewResponse


url = "https://www.cnblogs.com/yoyoketang/"
res = requests.get(url, hooks={"response": decrypt_response})
print(res.elapsed)
print(res.text)
print(res.content)
print(res.json())


"""
mitmproxy 中的hook
mitmproxy是一个代理工具，我们这之前的文章也有做过介绍。在抓包的过程中，同样需要用到 
hooks 去对request请求或response响应做一些额外的处理。
"""
"""
一个代理插件的基本骨架。
"""


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        self.num = self.num + 1
        print("We've seen %d flows" % self.num)


addons = [Counter()]



