"""
演示lambda匿名函数
"""

# 定义一个桉树，接受其他函数的输入
def test_func(compute):
    result = compute(1, 2)
    print(f"结果是：{result}")
# 通过lambda匿名函数的形式，将匿名函数作为参数传入


test_func(lambda x, y: x + y)