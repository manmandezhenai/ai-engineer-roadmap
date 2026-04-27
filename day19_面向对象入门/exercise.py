# 练习1：Book 类
"""
定义一个 Book 类
    。属性：title、author、pages
    。方法：info()，打印“《书名》由作者 著，共页数页”
    。创建两本书的对象，分别调用 info() 方法
"""


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        print(f"《{self.title}》由{self.author} 著，共{self.pages}页数")


book1 = Book("Python编程从入门到实践", "Eric Matthes", 460)
book2 = Book("活着", "余华", 191)

book1.info()
book2.info()

# 练习2：BankAccount 类
"""
定义一个 BankAccount 类
    。属性：owner（账户名）、balance（余额，默认为 0）
    。方法：
        - deposit(amount)：存入金额，打印“存入 X 元，当前余额 Y 元”
        - withdraw(amount)：取款，如果余额不足提示“余额不足”，否则扣款并打印“取款 X 元，当前余额 Y 元”
    。创建一个账户，模拟存钱和取钱操作
"""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"存入{amount}元，当前余额{self.balance}元")

    def withdraw(self, amount):
        if amount > self.balance:
            print("余额不足")
        else:
            self.balance -= amount
            print(f"取款{amount}，当前余额{self.balance}元")


account = BankAccount("小明")
account.deposit(1000)
account.withdraw(200)
account.withdraw(900)  # 余额不足

# 练习3（选做）：扩展 Dog 类
"""
增加一个 breed 品种属性
方法 bark()，不同品种叫不同声音（如金毛“汪汪”，哈士奇“嗷呜”）
"""


class Dog:
    """模拟小狗的简单尝试"""

    def __init__(self, name, age, breed):
        """初始化属性 name 和 age"""
        self.name = name
        self.age = age
        self.breed = breed

    def sit(self):
        """模拟小狗收到指令后坐下"""
        print(f"{self.name} 坐下了。")

    def describe(self):
        """打印小狗信息"""
        print(f"{self.name}，今年{self.age}岁")

    def bark(self):
        """模拟小狗叫"""
        if self.breed == "金毛":
            print(f"{self.name}: 汪汪！")
        elif self.breed == "哈士奇":
            print(f"{self.name}: 嗷呜～")
        else:
            print(f"{self.name}: 汪！")


dog1 = Dog("豆豆", 3, "金毛")
dog2 = Dog("二哈", 1, "哈士奇")
dog1.bark()
dog2.bark()
