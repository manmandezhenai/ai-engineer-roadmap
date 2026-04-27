# Day 16 - 模块与 pip

## 学到的概念

### 1.什么是模块与库?

- **模块**：一个 `.py` 文件，里面包含可复用的函数、类、变量
- **库**：一堆相关的模块打包在一起

### 2.导入模块的方式

- `import 模块名`：导入整个模块
- `import 模块名 as 别名`：导入并起别名
- `from 模块名 import 变量/函数/类`：从模块中导入特定变量/函数/类
- `from 模块名 import *`：导入全部内容（不推荐，可能污染命名空间）

### 3.常用内置模块

- `datetime`：时间处理（获取时间、格式化、时间计算）
- `os`：操作文件系统、目录、系统环境
- `random`：生成随机数、随机选择

```python
import datetime

print(datetime.datetime.now())  # 当前时间

import os

print(os.getcwd())  # 当前工作目录
print(os.listdir('.'))  # 列出当前目录下的文件

import random

print(random.choice(['苹果', '香蕉', '橘子']))  # 随机选一个
```

### 4.`pip` 与第三方库

- `pip` 是Python的包管理工具
- 常用命令：

```bash
pip install 库名
pip list
pip uninstall 库名
```

## 操作记录

- 安装 `requests`：pip install requests
- 创建虚拟环境命令：`python -m venv venv`
- 激活虚拟环境：`venv\Scripts\activate`