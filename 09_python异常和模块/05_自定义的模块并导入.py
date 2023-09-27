"""
演示自定义模块
"""

# 导入自定义模块的使用
# import my_module1
# from my_module1 import test
# test(1, 2)

# 导入不同模块的同名功能
from my_module1 import test_a
# from my_module2 import test
# test(1, 2)

# __main__变量
from my_module1 import test_a

# __all__变量
from my_module1 import *
test_a(1, 2)
test_b(2, 1)