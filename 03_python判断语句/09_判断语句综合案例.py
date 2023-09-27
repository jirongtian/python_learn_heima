import random
num = random.randint(1,10)

guess_num = int(input("猜一个数字（1-10）："))

if guess_num == num:
    print("恭喜你第一次就猜对了")
else:
    if guess_num > num:
        guess_num = int(input("大了，再猜一次："))
        if guess_num == num:
            print("猜对了")
        elif guess_num > num:
            guess_num = int(input("大了，再猜一次："))
            if guess_num == num:
                print("最后一次机会猜对了")
            else:
                print(f"三次都错了，答案是{num}")
        else:
            guess_num = int(input("猜小了，再猜一次："))
            if guess_num == num:
                print("最后一次机会猜对了")
            else:
                print(f"三次都错了，答案是{num}")
    else:
        guess_num = int(input("猜小了，再猜一次："))
        if guess_num == num:
            print("猜对了")
        elif guess_num > num:
            guess_num = int(input("大了，再猜一次："))
            if guess_num == num:
                print("最后一次机会猜对了")
            else:
                print(f"三次都错了，答案是{num}")
        else:
            guess_num = int(input("猜小了，再猜一次："))
            if guess_num == num:
                print("最后一次机会猜对了")
            else:
                print(f"三次都错了，答案是{num}")
