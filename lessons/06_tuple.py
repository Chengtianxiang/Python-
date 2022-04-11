#coding=utf-8

"""
元组类型，元组是不可变的列表类型，在python中也较为常见
"""

t = ("hello", "world", "!")
print(t, type(t))
# 元组类型一旦定义好了就不能做任何修改
print(t[0])
# 元素是否在元组中
print("!" in t)
