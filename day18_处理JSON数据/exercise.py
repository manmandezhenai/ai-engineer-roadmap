import requests
import json

# 练习1：解析随机用户
print("=== 随机用户信息 ===")
"""
调用 https://randomuser.me/api/
提取以下信息并打印：
    。用户姓名（first + last）
    。性别
    。所在国家
    。邮箱地址
"""

url = "https://randomuser.me/api/"

response = requests.get(url)

data = response.json()
user = data["results"][0]

# 用户姓名（first + last）
name = f"{user['name']['first']} {user['name']['last']}"
# 性别
gender = user["gender"]
# 所在国家
country = user['location']['country']
# 邮箱地址
email = user['email']

print(f"姓名：{name}")
print(f"性别：{gender}")
print(f"国家：{country}")
print(f"邮箱：{email}")

# 练习2：天气数据（广州）
print("\n=== 广州天气 ===")
"""
获取广州的天气信息。
    。将完整响应以缩进 2 格的格式打印
    。提取当前温度和风速，显示“广州当前温度：XX°C，风速：XX km/h”
"""

url_weather = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 23.13,
    "longitude": 113.26,
    "current_weather": "true"
}

resp = requests.get(url_weather, params=params)
weather = resp.json()

# 美化输出
print("完整响应（美化后）：")
print(json.dumps(weather, indent=2, ensure_ascii=False))

# 提取信息
current = weather['current_weather']
print(f"\n广州当前温度：{current['temperature']}°C，风速：{current['windspeed']} km/h")

# 练习3：文章列表（前3篇）
print("\n=== 示例文章（前3篇） ===")
"""
调用 https://jsonplaceholder.typicode.com/posts 获取 3 篇示例文章。
    。打印前 3 篇文章的 ID 和标题
    。提示：返回结果是列表，用循环切片取出前三个元素
"""

url_posts = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url_posts)

data = response.json()

for post in data[:3]:
    print(f"ID：{post['id']} - 标题：{post['title']}")