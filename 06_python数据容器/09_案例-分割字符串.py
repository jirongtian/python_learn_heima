
my_str = "itheima itcast boxuegu"
num = my_str.count("it")
print(f"在字符串中it出现了{num}次")
new_my_str = my_str.replace(" ", "|")
print(f"改变后的字符串是{new_my_str}")
new_my_str2 = new_my_str.split("|")
print(f"分割后的列表是：{new_my_str2}")