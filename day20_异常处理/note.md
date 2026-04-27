# Day 20 - 异常处理

## 学到的概念

### 1.什么是异常?

- 异常（Exception）是程序运行时发生的**错误事件**。如果不处理，程序会直接中断并打印一堆红色的错误信息
- 用异常处理可以让程序**预期到错误并给出友好提示**，而不是直接崩溃

### 2.基本结构

```python
try:
    可能出错的代码
except 异常类型:
    捕获特定异常
else:
    没有发生异常时才执行
finally:
    无论是否异常都会执行
```

### 3.常见异常类型

- `ValueError`：类型正确但值不对（如字母转数字）
- `ZeroDivisionError`：除以 0
- `TypeError`：类型错误（如 "2" + 2）
- `FileNotFoundError`文件不存在
- `KeyError`：字典键不存在

### 4.获取异常信息

可以使用 `as` 把异常对象保存下来，获取详情信息：

```python
try:
    num = int("abc")
except ValueError as e:
    print(f"转换失败：{e}")
```