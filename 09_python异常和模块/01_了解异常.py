"""
主动写一段代码，演示异常的出现
"""

# 通过open，读取一个不存在的文件
open("abc.txt", "r", encoding="UTF-8")