# 通过占位完成拼接
name = "张三"
message = "%s的花园" % name
print(message)

# 通过占位完成数字和字符串的拼接
class_num = 57
avg_salary = 17775
message = "北京%s期,平局工资%s" % (class_num, avg_salary)
print(message)

num1 = 11
num2 = 11.234
print("数字11宽度限制为5,结果：%5d" % num1)
print("数字11限制宽度1,结果：%1d" % num1)
print("数字11.234宽度限制为7,结果：%7.2f" % num2)
print("数字11.234限制宽度不限制,结果：%.2f" % num2)

# 字符串格式化--快速写法
name = "张三"
set_up = 89
print(f"我是{name}，我有{set_up}个")

#  对表达式进行字符串格式化
print("1*1的结果是:%d" % (1 * 1))

#
