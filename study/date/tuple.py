# 演示tuple元组的定义与操作

# 定义元组
t1 = (1, "hello", True)
t2 = ()
t3 = tuple()
print(f"t1的类型是:{type(t1)},内容是:{t1}")
print(f"t2的类型是:{type(t2)},内容是:{t2}")
print(f"t3的类型是:{type(t3)},内容是:{t3}")

# 定义单个元素,需加，（逗号）
t4 = "hello"
t44 = ("hello",)
print(f"t4的类型是:{type(t4)},内容是:{t4}")
print(f"t44的类型是:{type(t44)},内容是:{t44}")

# 元组嵌套
t5 = ((1, 2, 3), (4, 5, 6))
print(f"t5的类型是:{type(t5)},内容是:{t5}")

# 下标索引取出元素
num = t5[1][2]
print(f"从嵌套元组中取出的数据是:{num}")

# 元组的操作：index查找方法
t6 = ("zhangfei", "liubei", "guanyu")
index = t6.index("zhangfei")
print(f"在元组t6中查找zhangfei的下标是:{index}")
# 元组的操作：count统计方法

# 元组的操作：len函数统计元组数量
