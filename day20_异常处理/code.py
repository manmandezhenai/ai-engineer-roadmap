# Day 20 示例代码：异常处理

# 1. 基本异常处理
try:
    num1 = int(input("请输入被除数："))
    num2 = int(input("请输入除数："))
    result = num1 / num2
except ZeroDivisionError:
    print("除数不能为零")
except ValueError:
    print("输入的不是有效整数")
else:
    print(f"{num1} / {num2} = {result}")
finally:
    print("计算结束")

# 2. 捕获多种异常 + 获取信息
try:
    number = int("abc")
except (ValueError, TypeError) as e:
    print(f"错误信息：{e}")

# 3. 文件读取异常
filename = "不存在的文件.txt"
try:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

except FileNotFoundError:
    print(f"文件{filename}不存在，将创建新文件")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("这是自动创建的内容\n")

    print("已创建文件并写入默认内容")
