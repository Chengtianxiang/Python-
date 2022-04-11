#coding=utf-8

"""
集合
1. 集合中的元素不能重复
2. 集合中的元素是无序的
"""

s = set(["a", "b", "c"])
print(s, len(s))
# 添加元素
s.add("d")      # 添加不同的元素
print(s)
s.add("a")      # 添加相同的元素
print(s)
# 元素是否在集合中
print("b" in s)
# 删除元素
s.remove("a")
print(s)

# 集合的运算
s1 = set(["a", "b", "c"])
s2 = set(["a", "d"])
print()
print("s1={0}, s2={1}".format(s1, s2))
print("s1 交 s2 = {0}".format(s1 & s2))              # 交集
print("s1 并 s2 = {0}".format(s1 | s2))              # 并集
print("s1 差 s2 = {0}".format(s1 - s2))              # 差集
print("s2 差 s1 = {0}".format(s2 - s1))              # 差集
