# 练习1：随机猫咪事实
"""
调用 API：https://catfact.ninja/fact
解析返回的 JSON，打印出关于猫的冷知识
"""

import requests

url = 'https://catfact.ninja/fact'
resp = requests.get(url)
if resp.status_code == 200:
    data = resp.json()
    print("猫咪冷知识：", data['fact'])
    print(f"这句话有 {data['length']} 个字符")

# 练习2：GitHub 用户信息查询
"""
让用户输入一个 GitHub 用户名
调用 https://api.github.com/users/{用户名} 获取该用户信息
打印用户名、粉丝数、公开仓库数
如果用户不存在（404），给出友好提示
"""

username = input("请输入 GitHub 用户名：")
url = f'https://api.github.com/users/{username}'
resp = requests.get(url)

if resp.status_code == 200:
    user = resp.json()
    print(f"用户名：{user['login']}")
    print(f"粉丝数：{user['followers']}")
    print(f"公开仓库数：{user['public_repos']}")
elif resp.status_code == 404:
    print(f"用户 {username} 不存在")
else:
    print(f"请求失败，状态码：{resp.status_code}")
