# 练习1：购物清单
"""
创建一个空列表 shopping_list
让用户连续输入 3 件要买的东西，用 append 加入列表
打印最终清单，并显示“共有X件商品”
"""

shopping_list = []
for i in range(3):
    item = input(f"请输入第{i + 1}件商品：")
    shopping_list.append(item)

print(f"你的购物清单：{shopping_list}")
print(f"共有{len(shopping_list)}件商品")

# 练习2：成绩统计
"""
给你一个成绩列表：[78, 92, 85, 55, 88]
    。输出最高分、最低分、平均分（用 sum 和 len）
    。把不及格的成绩（< 60）替换成 0（此时没有，但可以练习一下条件判断 + 列表修改）
"""

scores = [78, 92, 85, 55, 88]

print(f"最高分：{max(scores)}")
print(f"最低分：{min(scores)}")
avg_score = sum(scores) / len(scores)
print(f"平均分：{avg_score}")

for i in range(len(scores)):
    if scores[i] < 60:
        scores[i] = 0

print(f"修改后的成绩：{scores}")

# 练习3：元素交换
"""
创建一个列表 data = [1, 2, 3, 4, 5]
将第一个元素与最后一个元素交换位置（不允许直接赋值 [5,2,3,4,1]）
打印交换后的列表
"""

data = [1, 2, 3, 4, 5]

temp = data[0]
data[0] = data[-1]
data[-1] = temp
print(f"交换后：{data}")