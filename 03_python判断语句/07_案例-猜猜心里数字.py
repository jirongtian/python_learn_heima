"""
演示if elif else练习题：猜猜心里数字
"""
"""
if (int(input("请输入第一次猜想的数字："))) != 10:
    if (int(input("不对，再猜一次："))) != 10:
        if(int(input("不对，再猜最后一次："))) != 10:
            print("Sorry，全部猜错啦，我想的是：10")
        else:
            print("对啦！")
    else:
        print("对啦！")
else:
    print("对啦！")
"""

num = 10
if int(input("请猜一个数字：")) == num:
    print("恭喜第一次就猜对了呢")
elif int(input("猜错了，再猜一次：")) == num:
    print("猜对了")
elif int(input("猜错了，再猜一次：")) == num:
    print("恭喜，最后一次机会猜对了")
else:
    print(f"sorry，全部猜错啦，我想的是{num}")