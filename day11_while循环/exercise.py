# 练习1：猜数字游戏
"""
程序随机生成一个 1~100 的整数
用户输入猜测，给出“大了”、“小了”或“猜对了”的提示
猜对后显示猜的次数
允许用户输入 quit 放弃游戏
"""

import random

num = random.randint(1, 100)
guess_count = 0
print("猜数字游戏（1~100），输入 quit 可退出")

while True:
    user_input = input("请输入你的猜测：")
    if user_input == "quit":
        print("你选择了放弃，游戏结束")
        break

    guess = int(user_input)
    guess_count += 1
    if guess < num:
        print("小了")
    elif guess > num:
        print("大了")
    else:
        print(f"猜对了！你一共猜了{guess_count}次")
        break

# 练习2：密码验证（3次机会）
"""
预设一个密码字符串，用户有最多 3 次输入机会
如果输入正确，显示“登录成功”并结束
如果 3 次都错误，显示“账户已锁定”
"""

pwd = "123456"
max_count = 3
count = 0
while count < max_count:
    user_input = input("请输入密码：")
    if user_input == pwd:
        print("登录成功")
        break
    else:
        count += 1
        remaining = max_count - count
        if remaining > 0:
            print(f"密码错误，还剩{max_count - count}次机会")
        else:
            print("账户已锁定")

# 练习3：累加器
"""
让用户连续输入数字，输入 0 时停止
计算所有输入数字的总和与平均值
"""

total = 0
count = 0
print("输入数字累加，输入 0 结束：")
while True:
    num = int(input("请输入一个数字："))
    if num == 0:
        break
    total += num
    count += 1

if count > 0:
    print(f"总和：{total}，平均值：{total / count}")
else:
    print("没有输入任何数字")
