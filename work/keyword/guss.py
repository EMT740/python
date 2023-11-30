print("猜数字，猜猜心里想的数字")

num = 5

if int(input("请输入")) == num:
    print("恭喜，第一次就猜对了")
elif int(input("猜错了，请再猜一次")) == num:
    print("猜对了")
elif int(input("猜错了，还有一次机会")) == num:
    print("猜对了")
else:
    print("你没有猜对")
