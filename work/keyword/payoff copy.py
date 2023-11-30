# whlie循环
# import random

# money = 10000
# man = 0
# while money >= 0:
#     num = random.randint(1, 10)
#     man = man + 1
#     if num < 5:
#         print(f"员工{man},绩效{num}，绩效不合格,不发工资,账户还剩{money}，下一位")
#     else:
#         money = money - 200 * num
#         print(f"员工{man},绩效{num},发放工资1000,账户还剩{money}")
#     if man == 20:
#         break
# print("工资发完了，下个月再来吧")

# for 循环
money = 10000
for i in range(1, 21):
    import random

    score = random.randint(1, 10)
    if score < 5:
        print(f"员工{i}绩效分{score}，不满足，不发放工资，下一个")
    else:
        money = money - 1000
        print(f"员工{i}绩效分{score}，满足条件，发放工资1000,公司账户还剩{money}")
    if money <= 0:
        break
print("余额不足，下个月再来")
