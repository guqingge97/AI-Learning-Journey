# Python App Template

一个 Python 项目的工程化模板，包含代码检查、类型检查、测试配置。

## 环境要求

- Python >= 3.10
- uv（包管理工具）

## 快速开始

1. 克隆项目后进入目录
2. 安装依赖：`uv sync`
3. 运行测试验证环境：`uv run pytest`

## 开发命令

| 命令 | 作用 |
|------|------|
| `uv run ruff check src` | 检查代码 |
| `uv run ruff format src` | 格式化代码 |
| `uv run pyright` | 类型检查 |
| `uv run pytest` | 运行测试 |