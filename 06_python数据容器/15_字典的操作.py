"""
演示字典的常用操作
"""

my_dict = {"周杰伦": 99, "林俊杰": 88, "张学友": 77}
# 新增元素
my_dict["张信哲"] = 66
print(f"字典经过新增元素后：{my_dict}")
# 更新元素
my_dict["周杰伦"] = 33
print(f"字典经过更新后，结果：{my_dict}")
# 删除元素
my_dict.pop("周杰伦")
print(f"字典中被移除了一个元素，结果：{my_dict}")
# 清空元素
my_dict.clear()
print(f"清空字典之后，结果：{my_dict}")
# 获取全部的Key
my_dict = {"周杰伦": 99, "林俊杰": 88, "张学友": 77}
keys = my_dict.keys()
print(f"字典的全部key是：{keys}")
# 遍历字典
# 方式1: 通过获得到全部的key来完成遍历
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")

# 方式2: 直接对字典进行for循环，每一次循环都是直接得到的key
for key in my_dict:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")

# 统计字典内的元素数量
num = len(my_dict)
print(f"字典中的元素数量有：{num}个")