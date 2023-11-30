print("欢迎来到游乐园")
if int(input("你的身高是多少：")) > 120:
    print("身高超出限制，请问你是高级VIP用户吗")
    if int(input("你的VIP等级是多少")) > 3:
        print("可以免费游玩")
    else:
        print("你需要补票10元")
else:
    print("欢迎小朋友，可以免费游玩")
