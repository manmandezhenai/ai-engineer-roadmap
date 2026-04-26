# Day 7 示例代码：运算符与输入

# 1. 算术运算
a = 10
b = 3
print("加法:", a + b)
print("整除:", a // b)
print("取余:", a % b)
print("幂:", a ** b)

# 2. 比较运算
print("10 > 3 吗？", a > b)
print("10 == 3 吗？", a == b)

# 3. 赋值运算符简写
c = 5
c += 2
print("c += 2 后:", c)

# 4. 输入并计算
num1 = float(input("请输入第一个数字: "))
num2 = float(input("请输入第二个数字: "))
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} * {num2} = {num1 * num2}")
