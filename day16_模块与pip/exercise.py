# 练习1：内置模块
"""
用 random 模块生成 5 个 1~100 之间的随机整数，存入列表，并打印。
用 datetime 模块输出今天的日期和星期几（如：2026-04-27 星期一）。
用 math 模块计算一个半径为 5 的圆的面积（π × r²）。
"""

import random
import math
from datetime import datetime

# 生成5个随机数
randoms = [random.randint(1, 100) for _ in range(5)]
print(f"随机数列表：{randoms}")

# 今天的日期与星期
today = datetime.now()
weekdays = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
print(f"今天是：{today.strftime('%Y-%m-%d')} {weekdays[today.weekday()]}")

# 圆面积
radius = 5
area = math.pi * radius ** 2
print(f"半径：{radius}，圆面积：{area:.2f}")

# 练习2：requests 获取 GitHub 仓库信息
"""
使用 requests.get() 访问 https://api.github.com/repos/microsoft/vscode
解析返回的 JSON 数据（.json()），打印出仓库的全名、星标数、描述。
"""

import requests

response = requests.get("https://api.github.com/repos/microsoft/vscode")
data = response.json()
print(f"仓库全名：{data['full_name']}")
print(f"星标数：{data['stargazers_count']}")
print(f"描述：{data['description']}")
