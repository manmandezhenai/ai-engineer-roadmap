# 练习1：学习主题文件
"""
创建一个文本文件 days.txt，向其中写入过去十五天的学习主题，每天一行（格式如 Day 1: 命令行入门）。
然后读取这个文件，统计一共有多少行，并打印出所有以“Day 1”开头的行。
用 with 语句完成所有文件操作。
"""

subjects = [
    "Day 1: 命令行入门",
    "Day 2: PyCharm 与 Git",
    "Day 3: Git 基础操作",
    "Day 4: GitHub 远程仓库",
    "Day 5: Python 安装与第一行代码",
    "Day 6: 变量与数据类型",
    "Day 7: 运算符与输入",
    "Day 8: 条件判断",
    "Day 9: 列表入门",
    "Day 10: for 循环",
    "Day 11: while 循环与循环控制",
    "Day 12: 字典与元组",
    "Day 13: 函数定义与调用",
    "Day 14: 函数进阶",
    "Day 15: 文件读写"
]

with open("days.txt", "w", encoding="utf-8") as f:
    for subject in subjects:
        f.write(subject + "\n")

count = 0
with open("days.txt", "r", encoding="utf-8") as f:
    for line in f:
        count += 1
        if line.startswith("Day 1"):
            print(line.strip())

print(f"总共有 {count} 天的记录")

# 练习2：简单日记本
"""
让用户输入今天的日记内容，然后追加写入 diary.txt。
每次都附上写入时间（可以用 import datetime 获取当前时间）。
写入后再读取整个日记文件并打印出来。
"""

import datetime

entry = input("今天有什么想记录的？ ")
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open('diary.txt', 'a', encoding='utf-8') as f:
    f.write(f"[{timestamp}] {entry}\n")

print("\n--- 日记全文 ---")
with open('diary.txt', 'r', encoding='utf-8') as f:
    print(f.read())