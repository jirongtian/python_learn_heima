"""
演示读取文件，课后练习题
"""

# 打开文件，以读取模式打开
f = open("word.txt", "r", encoding="UTF-8")
# 方式1:读取全部内容，通过字符串count方法统计itheima单词数量
# content = f.read()
# count = content.count("itheima")
# print(f"itheima出现了{count}次")

# 方式2:读取内容，一行一行读取
count = 0
for line in f:
    line = line.strip()
    words = line.split(" ")
# 判断单词出现次数并累计
    for word in words:
        if word == "itheima":
            count += 1
print(f"itheima出现了{count}次")
# 关闭文件
f.close()