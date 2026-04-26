# Day 2 - PyCharm 与 Git 安装

## 学到的概念

- IDE 是集成开发环境，PyCharm 是 Python 专用 IDE
- Git 是版本控制系统，GitHub 是代码托管平台

## 学会的操作

### 1.安装 PyCharm 社区版

- **下载地址**：https://www.jetbrains.com/pycharm/download/

### 2.安装 Git

- **下载地址**：https://git-scm.com/downloads
- **验证安装**：在终端输入 `git --version`，如果出现 `git version 2.xx.x` 即为成功。

### 3.配置 Git 身份

每个 Git 提交都需要一个用户名和邮箱，这是写在历史记录里的身份标识。

```bash
git config --global user.name "你的姓名拼音"
git config --global user.email "你的邮箱@example.com"
```

检查配置：
```bash
git config --global --list
```