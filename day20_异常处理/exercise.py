# 练习1：安全的计算器
"""
让用户输入两个数字和一个运算符（+、-、*、/），计算结果。
处理以下异常：
    。输入的不是数字（ValueError）
    。除法时除数为零（ZeroDivisionError）
    。使用 try-except-else-finally 结构。
"""

while True:
    try:
        num1 = float(input("请输入第一个数字："))
        num2 = float(input("请输入第二个数字："))
        op = input("请输入运算符（+ - * /）：")
        if op == "+":
            res = num1 + num2
        elif op == "-":
            res = num1 - num2
        elif op == "*":
            res = num1 * num2
        elif op == "/":
            res = num1 / num2
        else:
            print("未知运算符")
            continue

    except ValueError:
        print("输入的不是有效数字，请重新输入")
    except ZeroDivisionError:
        print("除法时除数不能为零")
    else:
        print(f"{num1} {op} {num2} = {res}")
        break
    finally:
        print("--- 本次尝试结束 ---")

# 练习2：安全文件读取
"""
让用户输入一个文件名，尝试打开并读取内容。
处理：文件不存在（FileNotFoundError），如果成功则打印内容，最后 finally 打印“操作结束”。
"""

filename = input("请输入要读取的文件名：")
try:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

except FileNotFoundError:
    print(f"文件 {filename} 不存在")

else:
    print("文件内容如下：")
    print(content)
finally:
    print("操作结束")

# 练习3：字典安全访问
"""
有一个字典 student = {"name": "小明", "age": 20}，尝试获取用户输入的键，使用 try-except 处理 KeyError，并给出提示
"""

student = {"name": "小明", "age": 20}
key = input("请输入要查询的键：")
try:
    value = student[key]
    print(f"{key}: {value}")

except KeyError:
    print(f"字典中没有 '{key}' 这个键")
