# 定义变量
money = 5000000
name = None
# 要求输入姓名
name = input("请输入你的名字")


# 定义查询函数
def query(show_header):
    print("------查询余额-------")
    print(f"{name}你好，你的余额剩余{money}元")


# 定义取款函数
def saving(num):
    global money  # money在函数内部定义为全局变量
    money += num
    print("-------存款------")
    print(f"{name}，你好，你取款{money}元成功")
    # 调用quary函数查询余额
    query(False)


# 定义取款函数
def get_money(num):
    global money  # money在函数内部定义为全局变量
    money -= num
    print("-------取款------")
    print(f"{name}，你好，你取款{money}元成功")
    # 调用quary函数查询余额
    query(False)


# 主菜单
def display():
    print("momo你好欢迎来到ATM，请选择")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入你的选择")


while True:
    keyboard_input = display()
    if keyboard_input == "1":
        query()
        continue
    elif keyboard_input == "2":
        num = int(input("你想要存多少钱？请输入"))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("你想要取多少钱？请输入"))
        get_money(num)
        continue
    else:
        print("程序退出")
        break  # 退出程序
