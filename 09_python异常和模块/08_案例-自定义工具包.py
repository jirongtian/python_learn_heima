"""
演示异常、模块、包的综合案例联系
"""

# 创建my_utils包，在包内创建：str_util.py 和 file_util.py 2个模块，并提供相应的函数

from my_utils import str_util
from my_utils import file_util

print(str_util.str_reverse("黑马程序员"))
print(str_util.substr("itheima", 0, 4))

# file_util.print_file_info("test_append.txt")
file_util.append_to_file("test_append.txt", "\nitheima")
file_util.print_file_info("test_append.txt")