# 定义列表
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
now_list = []
list_len = len(list)


# 用while实现
def list_while():
    # 定义一个变量计数
    count = 0
    while count < list_len:
        if list[count] % 2 == 0:
            now_list.append(list[count])
        count += 1
    print(f"通过while循环,从列表：{list}中取出偶数组成新列表：{now_list}")


# 用for实现
def list_for():
    for count in list:
        if count % 2 == 0:
            now_list.append(count)
    print(f"通过for循环,从列表：{list}中取出偶数组成新列表：{now_list}")


list_while()
list_for()
