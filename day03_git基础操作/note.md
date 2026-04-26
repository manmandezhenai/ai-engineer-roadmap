# Day 3 - Git 基础操作

## 学到的概念

- 工作区：你正在操作的文件夹，增删改文件都在这里
- 暂存区（stage）：可以理解为“购物车”，把准备提交的修改先放进去
- 仓库（repository）：正式保存提交历史的地方，一旦提交就永久记录
- 提交流程：修改 → git add → git commit

## 学会的命令

- `git status`：查看状态（红 = 未暂存，绿 = 已暂存）
- `git add .`：把所有修改加入暂存区
- `git commit -m "说明"`：提交并附上说明
- `git log`：查看历史记录
- `git log --oneline`：简洁版历史