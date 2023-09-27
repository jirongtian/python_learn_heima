"""
演示if elif else 多条件判断语句的使用
"""

height = int(input("请输入你的身高(cm)："))
vip_level = int(input("请输入你的vip等级(1-5)："))
day = int(input("请告诉我今天几号："))
# 通过if判断，可以使用多条件判断的语法
# 第一个条件是if
if height < 120:
    print("身高小于120cm，可以免费游玩。")
elif vip_level > 3:
    print(("vip级别大于3，可以免费游玩"))
elif day == 1:
    print("今天是1号免费日，可以免费游玩")
else:
    print("不好意思条件都不满足，需要买票10元")
