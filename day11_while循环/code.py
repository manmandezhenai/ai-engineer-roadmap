# Day 11 示例代码：while 循环

# 1. 基础 while 循环
count = 5
while count > 0:
    print(count)
    count = count - 1

print("出发！")

# 2. while True + break：命令交互
print("\n命令交互（输入 'quit' 退出）：")
while True:
    cmd = input(">")
    if cmd == "quit":
        print("退出程序")
        break

    print(f"你输入了：{cmd}")

# 3. continue 示例：只打印偶数
print("\n打印 1~10 之间的偶数：")
num = 0
while num <= 10:
    num += 1
    if num % 2 != 0:
        continue

    print(num, end=" ")

print()