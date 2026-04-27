# Day 16 示例代码：模块与 pip

# 1. 导入内置模块
import math
import random
from datetime import datetime

print(f"圆周率：{math.pi}")
print(f"1-100 随机数：{random.randint(1, 100)}")
print(f"当前时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# 2. 使用 as 别名
import math as m

print(f"平方根：{m.sqrt(81)}")

# 3. 使用 requests 库（需先 pip install requests）
import requests

response = requests.get("https://api.github.com")
print(f"状态码：{response.status_code}")
print(f"响应内容：{response.text}")
