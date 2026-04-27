# Day 18 - 处理 JSON 数据

## 学到的概念

### 1.JSON是什么?

- JSON 是一种**纯文本的数据交换格式**（几乎所有 API 作为标准响应格式）
- 核心规则：
    - 键名必须用**双引号**包裹
    - 值可以是：字符串、数字、布尔值、数组（列表）、嵌套对象（字典）、null
    - 不能有 Python 独有的 `None`、单引号、元组等

### 2.`json.loads()` 与 `json.dumps()`

- `json.loads()`：JSON 字符串 → Python 字典
- `json.dumps()`：Python 字典 → JSON 字符串
- 美化输出：`json.dumps(data, indent=2, ensure_ascii=False)`