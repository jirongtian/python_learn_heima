"""
演示函数的嵌套调用
"""

# 定义函数func_b
def func_b():
    print("---2---")
# 定义函数func_a，并在内部调用func_b
def func_a():
    print("---1---")
    # 嵌套调用func_b
    func_b()
    print("---3---")
# 调用func_a
func_a()
