# Day 14 示例代码：函数进阶

# 1. 默认参数
def power(base, exp=2):
    return base ** exp


print(f"3的平方：{power(3)}")
print(f"3的立方：{power(3, 3)}")


# 2. 关键字参数
def order(item, quantity=1, price=0):
    return f"购买了{quantity}份，{item}，总价{price}元"


print(order("薯片", price=6, quantity=3))


# 3. *args
def multiply(*args):
    result = 1
    for arg in args:
        result *= arg

    return result


print(f"1*2*3*4 = {multiply(1, 2, 3, 4)}")


# 4. **kwargs
def print_config(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")


print_config(language="Python", version=3.11, mode="script")
