# 需求：计算长度
str1 = "abcdef"
str2 = "eve"
str3 = "donot"

# 定义一个计数变量
count = 0
for i in str1:
    count += 1
print(f"字符串{str1}的长度是{count}")

count = 0
for i in str2:
    count += 1
print(f"字符串{str2}的长度是{count}")

count = 0
for i in str3:
    count += 1
print(f"字符串{str3}的长度是{count}")


# 定义一个函数
def my_len(date):
    count = 0
    for i in date:
        count += 1
    print(f"字符串{date}的长度是{count}")


my_len(str1)
my_len(str2)
my_len(str3)
