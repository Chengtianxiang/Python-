#coding=utf-8

"""
列表类型是python中使用最广泛的集合类型
"""

l = ["hello", "world", "!"]
# 输出列表值和类型
print(l, type(l))
# 列表长度
print(len(l))
# 使用下标来访问列表元素
print("first: {0} {1}".format(l[0], l[-len(l)]))    # 第一个元素，下标为0, 也可以直接使用-列表长度来索引
print("last: {0} {1}".format(l[len(l)-1], l[-1]))   # 最后一个元素，下标为列表长度-1，也可以直接使用-1来索引
# 在末尾添加元素
l.append("Welcome")
print(l)
# 在头部添加元素
l.insert(0, "python")       # 在下标为0的位置插入一个新元素
print(l)
# 从末尾移除元素
l.pop()
print(l)
# 从头部移除元素
l.pop(0)
print(l)
# 元素是否在列表中
print("!" in l)

# 列表相加
l2 = ["Welcome"]
l2.append("!")
l3 = l + l2
print(l3)
# 列表拼接
print(" ".join(l3))
# 列表反转
l.reverse()
print(l)
# 复合列表
cl = [0, 1.0, "aa", True]       # python中的列表，不要求元素有相同的数据类型，这是多数编程语言不具备的
print(cl, type(cl))
ll = [["a", "b"], [0, 1], [True, False]]    # 列表的列表
print(ll, type(ll))
