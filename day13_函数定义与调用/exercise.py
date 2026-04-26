# 练习1：温度转换函数
"""
定义一个函数 celsius_to_fahrenheit(celsius)，将摄氏温度转为华氏温度。
公式：华氏度 = 摄氏度 × 9/5 + 32
调用该函数转换 0°C、25°C、100°C 并打印结果。
"""


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


print(f"0°C = {celsius_to_fahrenheit(0)}°F")
print(f"25°C = {celsius_to_fahrenheit(25)}°F")
print(f"100°C = {celsius_to_fahrenheit(100)}°F")

# 练习2：列表统计函数
"""
定义一个函数 analyze_list(numbers)，接收一个数字列表，返回最高值、最低值和平均值。
调用该函数处理 [78, 92, 85, 65, 88]，并打印结果。
"""


def analyze_list(numbers):
    return max(numbers), min(numbers), sum(numbers) / len(numbers)


max_val, min_val, avg_val = analyze_list([78, 92, 85, 65, 88])
print(f"最高分：{max_val}，最低分：{min_val}，平均值：{avg_val}")

# 练习3：封装年龄判断（示例）
"""
把你 Day 8 的“年龄判断器”或 Day 11 的“猜数字游戏”用函数封装起来。
至少封装一个核心逻辑函数。
"""


def judge_age(age):
    if age <= 3:
        return "婴幼儿"
    elif age <= 12:
        return "儿童"
    elif age <= 17:
        return "青少年"
    elif age <= 64:
        return "成年人"
    else:
        return "老年人"


print(f"25岁是：{judge_age(25)}")
print(f"70岁是：{judge_age(70)}")
