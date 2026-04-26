# 练习1：灵活问候
"""
定义一个函数 greet_user(name, greeting="你好", repeat=1)，可以指定问候语和重复次数，默认问候“你好”且只说一次。调用三次展示不同组合。
"""


def greet_user(name, greeting="你好", repeat=1):
    for i in range(repeat):
        print(f"{greeting} {name}!")


greet_user("小明")
greet_user("小红", greeting="Hi", repeat=2)
greet_user("小刚", repeat=3)

# 练习2：平均值函数
"""
用 *args 定义一个 average(*numbers) 函数，计算任意个数的平均值。
    如果是空参数怎么处理？可返回 0 或给出提示。
    调用验证 average(80, 90, 85, 95)。
"""


def average(*numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


print(average(80, 90, 85, 95))
print(average())

# 练习3：构造名片
"""
用 **kwargs 定义一个 create_card(**data) 函数，能接收任意信息并用字典返回一张“名片”。
调用示例：create_card(name="小张", department="研发", phone="123456")。
"""


def create_card(**kwargs):
    card = {}
    for key, value in kwargs.items():
        card[key] = value

    return card


print(create_card(name="小张", department="研发", phone="123456"))
