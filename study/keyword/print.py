# 定义一个变量
money = 50
# 输出
print("钱包余额有:", money)

# 使用print直接输出类型信息
print(type("你好"))
print(type(666))
print(type(11.324))

# 使用变量存储type()语句的结果
string_type = type("你好")
int_type = type(123)
float_type = type(11.234)
print(string_type)
print(int_type)
print(float_type)

# 将数字类型转换成字符串
num_str = str(111)
print(type(num_str), num_str)

# 将字符串类型转成数字
num1 = int("11")
print(type(num1), num1)

num2 = float("11.456")
print(type(num2), num2)

# 整数转浮点型
float_num = float(11)
print(type(float_num), float_num)

# 浮点转整数
int_num = int(11.432)
print(type(int_num), int_num)

""" 
变量命名规范
1、明了
2、简洁
3、下划线命名法 
4、英文字母全小写
"""

# 算数（数学）运算符
print("1+1=", 1 + 1)
print("5-2=", 5 - 2)
print("3*6=", 3 * 6)
print("8/2=", 8 / 2)
print("5//3=", 5 // 3)
print("9%2=", 9 % 2)
print("4**6=", 4**6)

# 赋值运算符 （=、+=、-=、*=、/=、%=、**=、//=）
a = 1 + 2 + 4
a += 1
print("a += 1: ", a)
a -= 1
print("a -= 1: ", a)
a *= 4
print("a *= 1: ", a)
a /= 2
print("a /= 1: ", a)

# 几种引号定义法
name1 = """ 医院 """
name2 = " 医院 "
name3 = " 医院 "
print(type(name1), name1)
print(type(name2), name2)
print(type(name3), name3)

# 使用转义字符\解除引号效用
name = '"医院"'
print(type(name), name)
