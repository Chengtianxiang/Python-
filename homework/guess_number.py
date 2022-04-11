#!/usr/bin/python
#coding=utf-8

import random

"""
猜数游戏
1. 预设一个0~9之间的整数
2. 用户通过键盘输入所猜的数
（1）如果大于预设的数，输出"遗憾，太大了"
（2）如果小于预设的数，输出"遗憾，太小了"
3. 循环上述过程，直至猜中，输出"预测N次，你猜中了！"，其中N是用户输入数字的次数
"""

NUMBER = random.randint(0, 9)       # 生成[0, 9]区间内的一个整数
guess_times = 0                     # 猜的次数
while 1:
    num = int(input())
    guess_times += 1
    if num > NUMBER:
        print("遗憾，太大了")
    elif num < NUMBER: 
        print("遗憾，太小了")
    else:
        print("预测{0}次，你猜中了！".format(guess_times))
        break
