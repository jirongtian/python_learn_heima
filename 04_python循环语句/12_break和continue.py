"""
演示循环语句的中断控制:break和continue
"""

# 演示循环终端语句continue
for i in range(1,6):
    print("语句1")
    continue
    print("语句2")
print()

# 演示continue的嵌套应用

for i in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        continue
        print("语句3")

    print("语句4")
print()

# 演示循环终端语句break
for i in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        break
        print("语句3")

    print("语句4")
# 演示break的嵌套应用
