# Day 10 示例代码：for 循环

# 1. 遍历列表
todos = ["写作业", "跑步", "学Python", "看书"]
print("今日待办：")
for task in todos:
    print(task)

# 2. 使用 range 计数
print("\n倒计时开始：")
for i in range(5, 0, -1):
    print(i)

print("出发！")

# 3. 循环与索引
print("\n带编号的清单：")
for i in range(len(todos)):
    print(f"{i + 1}. {todos[i]}")

# 4. 嵌套循环打印简版乘法表
print("\n5x5 乘法表：")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {i * j}", end="\t")

    print()
