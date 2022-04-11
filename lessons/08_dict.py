#coding=utf-8

"""
字典(又称映射，Map)。字典可能是python中最有用的数据结构了
字典中的元素由键(Key)和值(Value)构成
字典和集合一样，也是无序的
"""

d = {"a": 1, "b": 2}
print(d, type(d))
# 取值
print("a={0}".format(d["a"]))
# 添加元素
d["c"] = 3
print(d)
# 覆盖元素
d["c"] = 4
print(d)
# 元素是否在字典中
print("a" in d)
# 删除元素
d.pop("c")
print(d)
# 获取字典所有的键
print(d.keys())
# 获取字典所有的值
print(d.values())

# 字典合并
d1 = {"a": 1, "b": 2}
d2 = {"x": 10, "y": 11, "a": 5}
print("d1={0}".format(d1))
print("d2={0}".format(d2))
d1.update(d2)
print(d1)
