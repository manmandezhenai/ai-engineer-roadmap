# Day 13 示例代码：函数

# 1. 有参数、有返回值
def multiply(a, b):
    """返回两数乘积"""
    return a * b


result = multiply(10, 20)
print("10 * 20 =", result)


# 2. 有参数、无返回值
def say_hello(name):
    print(f"Hello {name}！")


say_hello("小满")

# 3. 无参数、有返回值
import datetime


def get_current_year():
    return datetime.datetime.now().year


print(f"今年是：{get_current_year()}")

# 4. 作用域演示
global_var = "我是全局变量"


def scope_demo():
    local_var = "我是局部变量"
    print(f"函数内访问全局：{global_var}")
    print(f"函数内访问局部：{local_var}")


scope_demo()
print(f"函数外访问全局：{global_var}")
# print(local_var)  # 会报错
