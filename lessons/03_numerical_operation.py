#coding=utf-8

"""
数值运算
"""

import math

# 整型的运算
a = 2
b = 3
print("----- 整型 -----")
print("a={0} b={1}".format(a, b))
print("")
print("a+b = {0}".format(a + b))        # 加法
print("")
print("a-b = {0}".format(a - b))        # 减法
print("")
print("a x b = {0}".format(a * b))      # 乘法
print("")
print("a / b = {0}".format(a / b))      # 除法，python2中整型/整型是整型，python3中是浮点型
print("a / b = {0}".format(a * 1.0 / b))# 除法，乘以1.0这个浮点数，可以转成浮点类型
print("")
print("a % b = {0}".format(a % b))      # 模
print("")
print("a ^ b = {0}".format(a ** b))         # 幂运算
print("a ^ b = {0}".format(math.pow(a, b))) # 幂运算
print("")
print("sqrt(a) = {0}".format(math.sqrt(a)))     # 开根号
print("sqrt(a) = {0}".format(math.pow(a, 0.5))) # 开根号
print("")

# 浮点类型的运算
c = math.pi         # 圆周率
print("----- 浮点型 -----")
print("c={0}".format(c))
print("向上取整 = {0}".format(math.ceil(c)))
print("向下取整 = {0}".format(math.floor(c)))
print("向下取整 = {0}".format(c // 1.0))        # 两个乘号是幂运算，两个除号是地板除，即先执行除法，然后向下取整
