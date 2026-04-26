# 练习1：定义并打印自己信息
# 定义三个变量：你的姓名（字符串）、你的年龄（整数）、你的身高米数（浮点数），然后用 print 和 type 分别打印它们

name = "小满"
age = 23
height = 1.75

print(name, type(name))
print(age, type(age))
print(height, type(height))

# 练习2：交换两个变量的值
# 交换两个变量的值：让 a = 10，b = 20，用程序交换它们的内容，使得最终 a = 20, b = 10

a = 10
b = 20

a, b = b, a
print(f"a = {a}, b = {b}")

# 练习3：浮点数转整数
# （附加题）将一个浮点数转换成整数，打印转换前后的值和类型

float_num = 3.14
int_num = int(3.14)
print(f"转换前的值：{float_num}，类型：{type(float_num)}")
print(f"转换后的值：{int_num}，类型：{type(int_num)}")