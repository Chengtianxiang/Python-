#coding=utf-8

"""
程序的常见结构有三种，顺序结构、分支结构、循环结构
* 顺序结构：代码从前往后依次执行，每一条语句都会被执行到
* 分支结构：代码被分成多个部分，程序会根据特定的条件来判断到底执行哪一部分
* 循环结构：程序会重复执行同一段代码，直至条件不再满足，或者遇到强行跳出语句(break)
python中的分支结构中只有if语句，没有switch-case这种开关语句
"""

# 多条件匹配
age = "1995"
if age < "1970":
    print("70前")
elif age < "1980":
    print("70后")
elif age < "1990":
    print("80后")
elif age < "2000":
    print("90后")
else:
    print("00后")

# 使用条件语句来赋值，写出好看的代码
country = "china"
my_country = "中国" if country == "china" else "外国"
print(my_country)
country = "us"
my_country = "中国" if country == "china" else "外国"
print(my_country)
