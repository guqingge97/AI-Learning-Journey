# M1-W3 新项目启动 Checklist

## 项目结构
- [ ] 创建 src 布局（`src/包名/`）
- [ ] 创建 tests 目录

## 配置文件
- [ ] 配置 pyproject.toml（项目信息 + 依赖 + ruff 规则）
- [ ] 配置 pyrightconfig.json（类型检查）
- [ ] 创建 .gitignore（排除 .venv、缓存等）
- [ ] 创建 .python-version（锁定 Python 版本）

## CI/CD
- [ ] 创建 .github/workflows/ci.yml

## 文档
- [ ] 写 README.md（环境要求 + 快速开始 + 开发命令）

## 验证
- [ ] uv sync 能成功
- [ ] uv run pytest 能通过
- [ ] uv run ruff check src 无报错
- [ ] uv run pyright 无报错
- [ ] GitHub Actions 跑通