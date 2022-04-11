#coding=utf-8

"""
字符串
"""

a = "hello"
b = "world!"
print("a={0} b={1}".format(a, b))

# 字符串相加
c = a + " " + b
print(c)
# 字符串长度
print(len(a))
# 字符串下标寻址
print(a[0], a[1], a[2], a[3], a[4]) # python中下标都是从0开始的
# 字符串转大写
print(a.upper())
# 字符串转小写
print(a.lower())
# 字符串包含
print("l" in a)
# 字符串查找
print(a.find("l"))  # 返回l在a中出现的第一个位置
print(a.index("l")) # 返回l在a中出现的第一个位置
print(a.rindex("l"))# 返回l在a的逆序中出现的第一个位置
# 字符串分割
print(a.split("l"))
