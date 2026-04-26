# 练习1：简易计算器
# 让用户输入两个数字，计算它们的 和、差、积、商（浮点）、整除结果、余数，并打印出来

num1 = float(input("请输入第一个数字: "))
num2 = float(input("请输入第二个数字: "))

print("和:", num1 + num2)
print("差:", num1 - num2)
print("积:", num1 * num2)
print("商:", num1 / num2)
print("整除:", num1 // num2)
print("余数:", num1 % num2)

# 练习2：奇偶判断
# 输入一个整数，判断它是奇数还是偶数（提示：用 % 2）

number = int(input("请输入一个整数: "))
if number % 2 == 0:
    print(number, "是偶数")
else:
    print(number, "是奇数")

# 练习3：圆的面积
# (选做) 输入一个圆的半径，计算圆的面积（面积 = 3.14159 * 半径的平方），结果保留两位小数

radius = float(input("请输入圆的半径: "))
area = 3.14159 * radius ** 2
print("圆的面积约为: ", round(area, 2))