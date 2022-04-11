#coding=utf-8

"""
循环
计算机的优势在于可以执行成千上万次重复运算，这需要通过循环来实现。
python中的循环语句有两种：
（1）for...in循环
（2）while循环
"""

# 使用for循环可以遍历字符串
s = "hello"
print(s)
for char in s:
    print(char)

# 使用for循环遍历列表
print("")
l = ["a", "b", "c", "d"]
print(l)
for ele in l:
    print(ele)

# 使用for循环遍历集合
print("")
s = set(["a", "b", "c"])
print(s)
for ele in s:
    print(ele)

# 使用for循环遍历字典
print("")
d = {"a": 1, "b": 2, "x": 10, "y": 11, "a": 5}
print(d)
for key in d:           # 按照key来遍历
    print("{0}: {1}".format(key, d[key]))
print("")
for key, value in d.items():    # 按照key-value对来遍历
    print("{0}: {1}".format(key, value))



# 输出10以内的自然数列
print("")
print("使用for:")
for i in range(10):             # range(n)会生成[0, n)之间的整数数列
    print(i)
# 使用while循环输出10以内的自然数列
print("")
print("使用while:")
i = 0
while i < 10:
    print(i)
    i += 1                  # i = i + 1, python中可以写成+=，类似地，还有-=, *=, /=
