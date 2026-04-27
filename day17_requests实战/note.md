# Day 17 - requests 实战

## 学到的概念

### 1.什么是 API？

API（应用程序接口）就像一个**数据自助餐厅**：你按菜单（文档）点菜（发请求），后厨（服务器）把菜（数据）端给你

```text
你的程序  →  HTTP请求  →  远程服务器
你的程序  ←  JSON响应  ←  远程服务器
```

### 2.`requests.get()` 核心模式

```python
import requests

# 带参数的请求
params = {
    'q': 'python',
    'limit': 5
}
response = requests.get('https://api.example.com/search', params=params)

# 检查状态码：200 表示成功
print(response.status_code)

# 如果响应是 JSON 格式，直接转为 Python 字典/列表
data = response.json()
```

- **GET 请求**：向服务器索要数据
- **JSON 格式**：API 返回主流数据格式
- **response.json()**：把 JSON 转成 Python 字典 / 列表
- **params 参数**：传递查询条件
- **状态码**：200（成功）、404（未找到）、500（服务器错误）等

### 3.错误处理

网络请求可能会失败，要养成判断状态码习惯：

```python
import requests

try:
    response = requests.get('https://api.example.com/data', timeout=5)
    response.raise_for_status()  # 如果不是 2xx，自动抛出异常
    data = response.json()
except requests.exceptions.Timeout:
    print("请求超时，请稍后重试")
except requests.exceptions.ConnectionError:
    print("网络连接失败，请检查网络")
except requests.exceptions.HTTPError as e:
    print(f"HTTP 错误：{e}")
```