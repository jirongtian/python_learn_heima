"""
演示tuple元组的定义和操作
"""

# 定义元组
t1 = (1,"hello",True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)},内容是：{t1}")
print(f"t2的类型是：{type(t2)},内容是：{t2}")
print(f"t3的类型是：{type(t3)},内容是：{t3}")

# 定义单个元素的元组
t4 = ("hello", )
print(f"t4的类型是：{type(t4)}，t4的内容是：{t4}")
# 元组的嵌套
t5 = ((1, 2, 3), (4, 5, 6))
print(f"t5的类型是：{type(t5)}，内容是：{t5}")
# 下标索引去取出元组
num = t5[1][2]
print(f"取出的元素是:{num}")
# 元组的操作：index查找方法
t6 = ("传智教育", "黑马程序员", "python")
index = t6.index("黑马程序员")
print(f"在元组t6中查找黑马程序员，的下标是：{index}")
# 元组的操作：count统计法
t7 = ("传智教育", "黑马程序员",  "黑马程序员",  "黑马程序员", "python")
num = t7.count("黑马程序员")
print(f"在元组t7中统计黑马程序员的数量是：{num}")
# 元组的操作：len函数统计元组元素数量
t8 = ("传智教育", "黑马程序员",  "黑马程序员",  "黑马程序员", "python")
num = len(t8)
print(f"t8元组中的元素有：{num}个")
# 元组的遍历：while
index = 0
while index < len(t8):
    print(f"元组中的元素：{t8[index]}")
    index += 1
# 元组的遍历：for
for element in t8:
    print(f"元组的元素：{element}")

# 修改元组内容
# t8[0] = "itcast"

# 定义一个元组
t9 = (1,2,["itheima", "itcast"])
print(f"t9的内容是：{t9}")
t9[2][0] = "黑马程序员"
t9[2][1] = "传智教育"
print(f"t9的内容是：{t9}")



"""
课后练习
"""
T1 = ('周杰伦', 11, ['football', 'music'])
# 1.查询其年龄所在下标位置
num = T1.index(11)
print(f"年龄所在下标位置是：{num}")

# 2.查询学生的姓名
print(f"学生姓名是：{T1[0]}")

# 3. 删除学生爱好中的football
del T1[2][1]
print(f"删除后的T1是：{T1}")
# 4.增加爱好：coding到爱好list
T1[2].append('coding')
print(f"修改后的T1是：{T1}")