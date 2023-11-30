""" # 演示
name_list = ["xiaoming", "xiaohong", "xiaolain"]
print(name_list)
print(type(name_list)) """

# 定义一个嵌套列表
my_list = ["xiaohong", "666", "like"]
print(my_list)
print(type(my_list))

my_list = ["xiaohong", 666, True]
print(my_list)
print(type(my_list))

# 定义一个嵌套的列表
my_list = [[1, 2, 3], [2, 3, 4]]
print(my_list)
print(type(my_list))

# 通过小标索引取出对应位置的数据
my_list = ["xiaohong", "xiaolan", "xiaolv"]
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

# 取嵌套列表元素
my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list[1][1])
