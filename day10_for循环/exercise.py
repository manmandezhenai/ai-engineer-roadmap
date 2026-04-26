# 练习1：待办清单编号
"""
创建一个待办事项列表 ["写作业", "跑步", "学Python", "看书"]
用 for 循环打印出带编号的清单，格式：第1项：写作业
"""

todos = ["写作业", "跑步", "学Python", "看书"]

for i in range(len(todos)):
    print(f"第{i + 1}项：{todos[i]}")

# 练习2：九九乘法表
"""
使用嵌套 for 循环打印完整的 9x9 乘法表，要求对齐（个位十位对齐）
输出示例：1 x 1 = 1
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} x {i} = {i * j}", end="\t")

    print()

# 练习3：1~100 求和
"""
用 for 循环计算 1+2+3+...+100 的结果并打印
用 sum() 和 range() 验证结果
"""

total = 0
for i in range(1, 101):
    total += i

print(f"1-100的和：{total}")
print(f"用 sum 验证：{sum(range(1, 101))}")