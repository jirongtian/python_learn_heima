"""
演示函数综合案例开发
"""

# 定义全局变量money name
money = 5000000
name = None
# 要求客户输入名字
name = input("请输入您的姓名：")
# 定义查询函数
def query(show_header):
    if show_header:
        print("----------------查询余额----------------")
    print(f"{name}，您好，您的余额剩余：{money}元")

# 定义存款函数
def saving(num):
    global money
    money += num
    print(f"{name}，您好，您存款{num}元成功。")
    query(False)
# 定义取款函数
def get_money(num):
    global money
    money -= num
    print(f"{name}，您好，您取款{num}元成功。")
    query(False)
# 定义主菜单函数
def main():
    print("----------------主菜单----------------")
    print(f"{name}，您好，欢迎来到黑马银行ATM。请选择操作：")
    print("查询余额\t[输入1]")
    print("存钱\t\t[输入2]")
    print("取钱\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")
# 设置无限循环，确保程序不退出
while True:
    keyboard_input = main()
    if keyboard_input =="1":
        query(True)
        continue
    elif keyboard_input == "2":
        num = int(input("您想要存多少钱？请输入："))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("您想要取多少钱？请输入："))
        get_money(num)
        continue
    else:
        print("退出程序")
        break