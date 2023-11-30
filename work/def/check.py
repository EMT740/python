def check(num):
    print("欢迎来到游乐园\n请出示你的72小时核酸证明\n并配合测量体温")
    if num <= 37.5:
        print(f"体温测量中，你的体温是：{num}度，体温正常,请进")
    else:
        print(f"体温测量中，你的体温是：{num}度，体温异常,需要隔离")


check(36.8)
