"""
演示for循环的练习题：数一数有几个a
"""

#统计如下字符串中，有多少个a
name = "itheima is a brand of itcast"
count = 0
for x in name:
    if x =="a":
        count += 1
print(f"总共有{count}个a")