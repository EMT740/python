# 获取随机数
import random

num = random.randint(0, 100)
count = 0
guss_num = int(input("输入你猜的数字"))
while guss_num != num:
    if guss_num > num:
        print("你猜大了")
    if guss_num < num:
        print("你猜小了")
    count += 1
    guss_num = int(input("输入你猜的数字"))
print(f"你猜对了,你一共猜了{count}次")
