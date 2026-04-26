# 练习1：个人信息名片
"""
创建一个字典存放你自己的个人信息：姓名、年龄、城市、爱好（用列表）
用循环打印所有信息
添加一个新字段“职业”，然后更新年龄
"""

my_info = {
    "name": "小满",
    "age": 20,
    "city": "广州",
    "hobbies": ["编程", "跑步", "读书"]
}

for k, v in my_info.items():
    print(f"{k}: {v}")

my_info["major"] = "学生"
my_info["age"] = 21

print(f"更新后：{my_info}")

# 练习2：菜单翻译器
"""
创建一个中英菜单字典：{"鱼": "fish", "饭": "rice", "面": "noodles"}
让用户输入中文食物名，输出对应的英文
如果输入的词不在字典中，提示“暂时没有收录该食物”
"""

menu = {"鱼": "fish", "饭": "rice", "面": "noodles"}

word = input("请输入中文食物名：")
if word in menu:
    print(f"{word} 的英文是：{menu[word]}")
else:
    print("暂时没有收录该食物")

# 练习3：元组解包
"""
创建一个元组 dimensions = (1920, 1080)
用一行代码将两个值分别赋予变量 width 和 height
打印这两个变量验证
"""

dimensions = (1920, 1080)
width, height = dimensions
print(f"宽度：{width}，高度：{height}")