# Day 15 - 文件读写

## 学到的概念

### 1.为什么要读写文件?

到目前为止，所有数据都存储在变量里，程序一关就没了。**文件能把数据持久化到硬盘上**，比如：

- 保存用户设置
- 记录日志
- 读取原始文档（txt、md）供后续处理

### 2.打开文件的基本方式

```python
file = open('example.txt', 'r', encoding='utf-8')  # 打开文件
content = file.read()  # 读取内容
file.close()  # 关闭文件（必须！）
```

- **模式**：`r` 只读，`w` 写入（会清空原文件！），`a`追加到末尾
- **编码**：推荐始终指定 `encoding = 'utf-8'`，避免中文乱码

### 3.使用 `with` 自动关闭文件（推荐）

`with` 语句会在代码块执行完毕后自动关闭文件，即使中途遇到错误也会关闭

```python
with open('example.txt', 'r', encoding='utf-8') as f:
    content = f.read()
print(content)  # 文件已自动关闭，但 content 还在
```

### 4.读取方式

- `f.read()`：一次性读取整个文件为字符串
- `f.readline()`：每次读取一行（包括行尾的 \n）
- `f.readlines()`：读取所有行，返回列表

### 5.写入文件

- `w` 模式：覆盖写入（文件不存在则创建）
- `a` 模式：追加到文件末尾
- `f.write(字符串)`：写入字符串