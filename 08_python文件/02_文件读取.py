"""
演示对文件的读取
"""
import time

# 打开文件
f = open("test.txt", "r", encoding="UTF-8")

print(type(f))
# 读取文件 - read()
# print(f"读取十个字节的结果：{f.read(10)}")
# print(f"读取全部字节的结果：{f.read()}")  # 下一个read在上一个的结尾开始

# 读取文件 - readLines()
# lines = f.readlines()
# print(f"lines对象的类型是：{type(lines)}")
# print(f"lines对象的内容是：{lines}")

# 读取文件 - readline()
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行数据是：{line1}")
# print(f"第二行数据是：{line2}")
# print(f"第三行数据是：{line3}")

# for循环读取文件行
# for line in f:
#     print(f"每一行数据是：{line}")

# 文件的关闭
# f.close()
# time.sleep(500000)

# with open 语法的操作(运行后自动关闭)
with open("test.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据是：{line}")
time.sleep(500000)