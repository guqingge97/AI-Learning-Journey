# CLI Tool

一个文本文件处理工具，支持文件统计、关键词查找、批量替换等功能。

## 环境要求

- Python >= 3.13
- uv（包管理工具）

## 快速开始

1. 安装 uv（如果没有）
```bash
   pip install uv
```

2. 安装依赖
```bash
   uv sync
```

3. 验证安装
```bash
   uv run cli-tool --help
```
   应该看到 4 个命令：greet, count, find, replace

## 命令用法

| 命令 | 作用 | 示例 |
|------|------|------|
| `cli-tool greet` | 打招呼 | `uv run cli-tool greet 十香` |
| `cli-tool count` | 统计文件字符数/行数 | `uv run cli-tool count a.txt b.txt --count-lines` |
| `cli-tool find` | 查找关键词 | `uv run cli-tool find TODO ./test.txt` |
| `cli-tool replace` | 批量替换文本 | `uv run cli-tool replace foo bar ./test.txt` |