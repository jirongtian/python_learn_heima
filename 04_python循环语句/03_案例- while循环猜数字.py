import random
num = random.randint(1,100)
count = 1
guess_num = int(input("猜个数(1-100):"))

while guess_num != num:
    count += 1
    if guess_num > num:
        guess_num = int(input("大了，重新猜："))
    else:
        guess_num = int(input("小了，重新猜："))
print(f"猜对了，总共猜了{count}次")