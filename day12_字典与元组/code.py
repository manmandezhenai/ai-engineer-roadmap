# Day 12 示例代码：字典与元组

# 1. 字典的基本操作
user = {
    "name": "小李",
    "age": 28,
    "skills": ["Python", "Git"]
}

print(user["name"])
user["email"] = "1758994523@qq.com"  # 添加
user["age"] = 29  # 修改
print(user)

# 2. 安全访问
print(user.get("phone", "未知"))

# 3. 遍历字典
for key, value in user.items():
    print(f"{key}: {value}")

# 4. 元组的使用
point = (10, 20)  # 坐标
print(point[0], point[1])

# 元组不可变，但元组中有可变元素可以修改
t = (1, 2, [3, 4])
t[-1].append(5)
print(t)
