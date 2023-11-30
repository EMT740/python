age = 26
year = 3
level = 1
if age >= 18:
    print("你已经成年")
    if age < 30:
        print("你的年龄达标")
        if year > 2:
            print("恭喜，你的条件达标，可以领取礼物")
        elif level > 3:
            print("恭喜你的条件达标，可以领取礼物")
        else:
            print("你的条件不够，不能领取礼物")
    else:
        print("你的年龄不符合要求，不能领取礼物")
else:
    print("你的年龄不符合要求，不能领取礼物")
