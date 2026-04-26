# Day 9 示例代码：列表操作

# 1. 创建一个待办事项列表
todos = ["写作业", "跑步", "看书"]
print(f"今日的待办事项：{todos}")

# 2. 索引与切片
print(f"第一件事：{todos[0]}")
print(f"前两件事：{todos[:2]}")

# 3. 添加事项
todos.append("学Python")
todos.insert(1, "吃早餐")
print(f"添加后：{todos}")

# 4. 完成事项（删除）
done = todos.pop()
print(f"被删除的事项：{done}")
print(f"删除后：{todos}")

# 5. 统计
print(f"还剩{len(todos)}件事")
