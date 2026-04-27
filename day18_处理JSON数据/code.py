# Day 18 示例代码：处理 JSON 数据

import json
import requests

# 1. json.loads 与 json.dumps
json_str = '{"city": "广州", "weather": "晴", "temperature": 28}'
data = json.loads(json_str)
print(f"转换后的字典：{data}")
print(f"城市：{data['city']}")

info = {"language": "Python", "level": 2}
json_out = json.dumps(info)
print(f"转换后的 JSON 字符串：{json_out}")

# 2. 从嵌套结构中提取数据

response = {
    "status": "success",
    "data": {
        "user": {
            "name": "Alice",
            "repos": [
                {"name": "project1", "stars": 42},
                {"name": "project2", "stars": 18}
            ]
        }
    }
}

# 获取用户名
print(response["data"]["user"]["name"])

# 3. 美化输出测试
sample = {"name": "测试", "scores": [90, 85, 92], "passed": True}
print("\n美化输出：")
print(json.dumps(sample, indent=4, ensure_ascii=False))