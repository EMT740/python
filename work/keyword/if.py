print("欢迎来到方特，儿童免费，成人收费")
age = int(input("请输入你的年龄："))

if age >= 18:
    print("你已成年, 游玩需补票10元")
else:
    print("你还未成年，不需要付款")

print("祝你游玩愉快")
