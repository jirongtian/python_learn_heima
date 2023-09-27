"""
演示if else练习题：我要买票吗
"""

print("欢迎来到黑马动物园。")

# 定义键盘输入获取身高数据
height = int(input("请输入你的身高："))

# 通过if进行判断
if height > 120:
    print("您的身高超出120cm，游玩需要购票10元。")
else:
    print("您的身高未超出120cm，可以免费游玩。")
print("祝您游玩愉快。")