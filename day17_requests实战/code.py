# Day 17 示例代码：requests 实战
import requests

# 1. 随机狗狗图片
print("=== 随机狗狗图片 ===")
url_dog = 'https://dog.ceo/api/breeds/image/random'
resp = requests.get(url_dog)
if resp.status_code == 200:
    data = resp.json()
    print("状态：", data['status'])
    print("图片地址：", data['message'])
else:
    print("请求失败")

# 2. 随机名言
print("\n=== 随机名言 ===")
url_quote = 'http://api.quotable.io/random'
resp = requests.get(url_quote)
if resp.status_code == 200:
    data = resp.json()
    print(f"“{data['content']}”")
    print(f"—— {data['author']}")

# 3. 带错误处理的请求
print("\n=== 带错误处理的请求 ===")
try:
    resp = requests.get('https://api.github.com/users/python', timeout=5)
    resp.raise_for_status()
    user = resp.json()
    print(f"GitHub 用户 python：{user['name']}，仓库数：{user['public_repos']}")
except requests.exceptions.Timeout:
    print("请求超时")
except requests.exceptions.HTTPError as e:
    print(f"HTTP 错误：{e}")
except Exception as e:
    print(f"其他错误：{e}")
