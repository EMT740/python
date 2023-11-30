# 构建一个随机变量
import random

num = random.randint(1, 10)

guss_num = int(input("请输入你认为的数字："))
if guss_num == num:
    print("恭喜你猜对了")
else:
    if guss_num > num:
        print("你猜的数字大了")
    if guss_num < num:
        print("你猜的数字小了")
    guss_num = int(input("请输入你认为的数字："))
    if guss_num == num:
        print("恭喜你第二次猜对了")
    else:
        if guss_num > num:
            print("你猜的数字大了")
        if guss_num < num:
            print("你猜的数字小了")
        guss_num = int(input("请输入你认为的数字："))
        if guss_num == num:
            print("恭喜你猜对了")
        else:
            if guss_num > num:
                print("三次机会用完了你没有猜中")
            if guss_num < num:
                print("三次机会用完了你没有猜中")
