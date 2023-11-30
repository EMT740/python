my_list = ["xiaohong", "xiaolan", "xiaolv"]

# 查找元素在列表内的下标索引
index = my_list.index("xiaohong")
print(f"xiaohong在列表中的下标索引值是:{index}")

# 修改下标索引位置的元素值
my_list[0] = "xiaoqiong"
print(f"列表被修改元素值后：{my_list}")

# 在指定下标位置插入元素
my_list.insert(1, "1")
print(f"列表插入元素后结果是:{my_list}")

# 追加元素
my_list.append("xiaocheng")
print(f"追加后的元素为:{my_list}")

# 追加一批元素
my_list.extend(my_list)
print(f"追加一批元素后的结果:{my_list}")

# 删除指定下标的元素
my_list = ["xiaohong", "xiaolan", "xiaolv"]
del my_list[2]
print(f"删除元素列表后的:{my_list}")
my_list = ["xiaohong", "xiaolan", "xiaolv"]
element = my_list.pop(1)
print(f"通过pop移除后的结果:{my_list},取出的元素是:{element}")

# 删除某个元素的第一个匹配项
my_list = ["xiaohong", "xiaolan", "xiaohong", "xiaolv"]
my_list.remove("xiaohong")
print(f"通过remove方法移除元素后的结果:{my_list}")

# 清空列表
my_list.clear()
print(f"列表被清空:{my_list}")

# 统计某类表中某元素的数量
my_list = ["xiaohong", "xiaolan", "xiaolv"]
count = my_list.count("xiaohong")
print(f"列表中该元素的数量为{count}")
