"""
演示布尔类型的定义
以及比较运算符的应用
"""

# 定义变量存储布尔类型的数据
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是：{bool_1}，类型是{type(bool_1)}")
print(f"bool_1变量的内容是：{bool_2}，类型是{type(bool_2)}")
# 比较运算符的使用
# ==, !=, >, <, >=, <=
# 演示进行内容的相等比较
num_1 = 10
num_2 = 10
print(f"num_1 == num_2的结果是：{num_1 == num_2}")

num1 = 10
num2 = 15
print(f"num1 != num2的结果是{num1 != num2}")

name1 = "itcast"
name2 = "itheima"
print(f"name1 == name2的结果是：{name1 == name2}")

# 演示大于小于，大于等于，小于等于的比较运算
num1 = 10
num2 = 5
print(f"10 > 5结果是：{num1 > num2}")
print(f"10 < 5结果是：{num1 < num2}")

num1 = 10
num2 = 11
print(f"10 >= 10的结果是：{num1 >= num2}")
print(f"10 <= 10的结果是：{num1 <= num2}")