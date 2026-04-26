# Day 8 示例代码：条件判断

# 1. 基础 if-elif-else
temperature = float(input("请输入当前气温（摄氏度）："))

if temperature > 35:
    print("天气炎热，注意防暑")
elif temperature > 25:
    print("天气温暖，很舒适")
elif temperature > 10:
    print("天气凉爽，记得带外套")
else:
    print("天气寒冷，要注意保暖")

# 2. 嵌套条件
has_umbrella = input("带伞了吗？(y/n)：")
if temperature < 10:
    if has_umbrella == "y":
        print("外面很冷，带伞是对的")
    else:
        print("小心冻着，最好带把伞")