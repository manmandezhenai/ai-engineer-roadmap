# Day 19 示例代码：面向对象入门

class Dog:
    """模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性 name 和 age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到指令后坐下"""
        print(f"{self.name} 坐下了。")

    def describe(self):
        """打印小狗信息"""
        print(f"{self.name}，今年{self.age}岁")

# 创建实例
my_dog = Dog('旺财', 3)
your_dog = Dog('小白', 1)

# 访问属性
print(f"我的狗叫：{my_dog.name}")
print(f"你的狗叫：{your_dog.name}")

# 调用方法
my_dog.sit()
my_dog.describe()
your_dog.sit()
your_dog.describe()

