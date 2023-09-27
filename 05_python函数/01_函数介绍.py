"""
演示：快速体验函数的开发和应用
"""
# 需求，统计字符串的长度，不使用内置函数了len()
str1 = "itheima"
str2 = "itcast"
str3 = "python"

# 定义一个计数变量
count = 0
for i in str1:
    count += 1
print(f"字符串的长度是：{count}")

count = 0
for i in str2:
    count += 1
print(f"字符串的长度是：{count}")

count = 0
for i in str3:
    count += 1
print(f"字符串的长度是：{count}")

# 可以使用函数，来优化这个过程

def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是{count}")


my_len(str1)
my_len(str2)
my_len(str3)