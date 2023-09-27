"""
演示for嵌套循环
"""

# 坚持表白100天，每天都送10朵花
# range

i = 0
for i in range(1,101):
    print(f"今天是向小美表白的第{i}天，坚持。。。")

    # 内层控制循环
    for j in range(1,11):
        print(f"送给小美的第{j}朵花。")
    print(f"小美，我喜欢你(第{i}天表白结束)")
    
print(f"第{i}天，表白成功")
