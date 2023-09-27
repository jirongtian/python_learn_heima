my_str = "万过薪月, 员序程马黑来, nohtyP学"
new_my_str = my_str[10:5:-1]
print(f"{new_my_str}")
new_my_str = my_str.split(",")[1].replace("来", " ")[::-1]
print(f"{new_my_str}")