"""
演示数据容器之：list列表
语法：[元素，元素，。。。]
"""

# 通过下标索引取出对应位置的数据
my_list = ["Tom", "Rose", "Lily"]
# 列表[下标索引]，从前往后从0开始，每次+1，从后向前从-1开始，每次-1
print(my_list[0])
print(my_list[1])
print(my_list[2])
# 错误示范：通过下标索引一定不要超出范围
# print(my_list[3])
print()

# 通过下标索引取出数据(倒序)
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])
# 取出嵌套列表的元素
my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list[0][0])
print(my_list[0][1])
print(my_list[0][2])
print(my_list[1][0])
print(my_list[1][1])
print(my_list[1][2])
