# Day 15 示例代码：文件读写

# 1. 写入文件（w 模式）
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write('你好，世界！\n')
    f.write('这是第二行。\n')

# 2. 追加和内容（a 模式）
with open("hello.txt", "a", encoding="utf-8") as f:
    f.write("追加的第三行。\n")

# 3. 读取整个文件
with open("hello.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("文件全部内容：")
    print(content)

# 4. 按行读取并处理
with open("hello.txt", "r", encoding="utf-8") as f:
    print("按行输出：")
    for line in f:
        line = line.strip()
        print(f"->{line}")

# 5. 检查当前工作目录
import os

print("当前工作目录：", os.getcwd())
