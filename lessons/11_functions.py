#coding=utf-8

import math

"""
函数
语句(statement)是程序的基本单位，一个复杂的程序可能由成千上万行语句构成。
而函数是将多条语句组合到一起，构成一个功能单元，以被重复调用
函数接受输入参数，然后执行运算，再将结果返回
"""

def circle_area(radius):
    """计算圆的面积"""
    return math.pi * radius * radius        # 用return语句返回函数的执行结果，如果补写return，那么函数返回为None

def cylinder_volume(radius, height):
    """计算圆柱的体积"""
    s = circle_area(radius)     # 计算底面积，这里直接调用函数
    return s * height

def power(x, n=2):                      # n=2表示不传n的时候，使用n=2，即返回x的平方
    """计算x的n次方"""
    result = 1
    while n > 0:
        n -= 1
        result *= x
    return result

def recursive_power(x, n=2):
    """使用递归计算x的n次方"""
    print("cal {0}^{1}".format(x, n))   # 这句话用于展示递归调用的逻辑
    if n == 0:                          # n=0时，终止
        return 1
    # 由于if语句中有return，当符合条件时函数直接返回了，因此这里可以不用写else语句
    return x * recursive_power(x, n-1)  # n > 1时，可以自身进行调用

# 半径为2的圆面积
r = 2 
print("radius={0}, area={1}".format(r, circle_area(r)))
# 半径为2，高度为3的圆柱体积
h = 3
print("radius={0}, height={1}, volume={2}".format(r, h, cylinder_volume(r, h)))
print("")

# 计算x的n次幂
x = 2
print("{0}的平方= {1}".format(2, power(x)))       # power函数使用默认参数，此时计算的是平方
print("{0}的立方= {1}".format(2, power(x, 3)))    # 手动传入n=3，计算立方
print("")

print(recursive_power(3, 4))
