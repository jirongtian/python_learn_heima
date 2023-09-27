"""
import random
money = 10000
for i in range(1,21):
    score = random.randint(1, 10)
    if money == 0:
        print("公司帐户余额为0，结束")
        break
    elif score >= 5:
        money -= 1000
        print(f"向员工{i}发放工资1000元，账户余额剩余{money}")
    else:
        print(f"员工{i}，绩效分为{score}，低于5，不发工资，下一位")
"""

import random
money = 10000

for i in range(1,21):
    score = random.randint(1,10)
    if score < 5:
        print(f"员工{i}，绩效分为{score}，低于5，不发工资，下一位")
        continue
    if money >= 1000:
        money -= 1000
        print(f"向员工{i}发放工资1000元，账户余额剩余{money}")
    else:
        print(f"余额不足，当前余额{money}，不发了，下月再来")
        break
