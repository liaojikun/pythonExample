"""
列表推导式
# 需求：要求列表输出 name1-name10
# 总结：列表推导式的好处 节省代码量，使代码看上去更美观。
"""
# 普通写法：
data = []
for i in range(1, 11):
    data.append("name%s" % i)
print(data)

# 列表推导式：
res = ["name%s" % i for i in range(1, 11)]
print(res)

"""
字典推导式
需求：生成{1:1,2:2,3:3,4:4}这样的列表
"""
# 普通循环生成:
dic1 = {}
for i in range(1, 5):
    dic1[i] = i
print(dic1)

# 字典推导式：
res = {i: i for i in range(1, 5)}
print(res)

# 将一下字符串转换为字典
test_str = "ABC=abc; ABD=abd; ABE=abe"
dic2 = {}
for i in test_str.split('; '):
    dic2[i.split('=')[0]] = i.split('=')[1]
print(dic2)

# 字典推导式
res = {i.split('=')[0]: i.split('=')[1] for i in test_str.split('; ')}
print(res)



