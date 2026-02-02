## 【速查表】M1-W3-D3：ruff 格式化与静态检查



```
┌─────────────────────────────────────────────────────────────┐
│                    ruff 核心命令                             │
├─────────────────────────────────────────────────────────────┤
│  安装                                                        │
│  uv add --dev ruff                                          │
├─────────────────────────────────────────────────────────────┤
│  检查代码问题（不修改）                                        │
│  uv run ruff check src                                      │
├─────────────────────────────────────────────────────────────┤
│  检查并自动修复                                               │
│  uv run ruff check src --fix                                │
├─────────────────────────────────────────────────────────────┤
│  格式化代码风格                                               │
│  uv run ruff format src                                     │
├─────────────────────────────────────────────────────────────┤
│  只检查格式，不修改                                           │
│  uv run ruff format src --check                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    pyproject.toml 配置                       │
├─────────────────────────────────────────────────────────────┤
│  [tool.ruff]                                                │
│  line-length = 88        # 每行最大字符数                     │
│  src = ["src"]           # 源码目录                          │
│                                                             │
│  [tool.ruff.lint]                                           │
│  select = ["E", "F", "I"]  # 启用的检查规则                   │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    常见错误码                                 │
├─────────────────────────────────────────────────────────────┤
│  E = 代码风格错误（如 E501 行太长）                            │
│  F = 逻辑错误（如 F401 未使用的 import）                       │
│  I = import 排序问题（如 I001 排序不对）                       │
├─────────────────────────────────────────────────────────────┤
│  [*] 标记 = 可自动修复                                        │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    check vs format                          │
├─────────────────────────────────────────────────────────────┤
│  ruff check   → 检查代码问题（未使用变量、错误逻辑）            │
│  ruff format  → 统一代码风格（空格、缩进、引号）               │
└─────────────────────────────────────────────────────────────┘
```

---

## M1-W3-D4 速查表

### 类型检查

uv run pyright src

### 可选类型（允许 None）

email: str | None = None
email: Optional[str] = None  # 旧写法

### Optional vs 默认值

Optional[str]        → 控制"允许什么值"（str 或 None）
= None               → 控制"是否必须传"
这两个是独立的！

### pyright 配置文件

pyrightconfig.json

---

## M1-W3-D5【速查表-GitHub Actions CI】



```
┌─────────────────────────────────────────────────────────────┐
│                    配置文件位置                              │
├─────────────────────────────────────────────────────────────┤
│  仓库根目录/.github/workflows/ci.yml                         │
│  （不是项目子目录！）                                         │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    最小 CI 配置                              │
├─────────────────────────────────────────────────────────────┤
│  name: CI                                                   │
│  on: [push]                                                 │
│  jobs:                                                      │
│    test:                                                    │
│      runs-on: ubuntu-latest                                 │
│      defaults:                                              │
│        run:                                                 │
│          working-directory: projects/xxx  # 子目录时需要     │
│      steps:                                                 │
│        - uses: actions/checkout@v4       # 拉代码           │
│        - uses: astral-sh/setup-uv@v4     # 装 uv            │
│        - run: uv sync                    # 装依赖           │
│        - run: uv run ruff check src      # 检查             │
│        - run: uv run pytest tests        # 测试             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    关键语法                                  │
├─────────────────────────────────────────────────────────────┤
│  on: [push]              → 什么时候触发（push 时）           │
│  runs-on: ubuntu-latest  → 在什么机器上跑                    │
│  uses: xxx               → 使用别人写好的动作                │
│  run: xxx                → 执行 shell 命令                  │
│  working-directory       → 指定命令运行目录                  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    常见踩坑                                  │
├─────────────────────────────────────────────────────────────┤
│  ❌ CI 报错找不到 pyproject.toml                             │
│  → 检查 working-directory 是否指向项目目录                    │
│                                                             │
│  ❌ Actions 页面看不到运行记录                                │
│  → 检查 .github/workflows/ci.yml 是否在仓库根目录            │
│  → 检查是否 git push 成功                                    │
└─────────────────────────────────────────────────────────────┘
```

---

## M1-W3-WE1【速查表-README 标准结构】

### README 标准结构



markdown

```markdown
# 项目名称
一句话说明

## 环境要求
- Python >= x.x
- 依赖工具

## 快速开始
1. 克隆项目
2. 安装依赖：`uv sync`
3. 验证环境：`uv run pytest`

## 开发命令
| 命令 | 作用 |
|------|------|
| uv run ruff check src | 检查代码 |
| uv run ruff format src | 格式化代码 |
| uv run pyright | 类型检查 |
| uv run pytest | 运行测试 |
```

### 提交 Git vs 不提交

| 提交               | 不提交         |
| ------------------ | -------------- |
| src/、tests/       | .venv/         |
| pyproject.toml     | __pycache__/   |
| uv.lock            | .pytest_cache/ |
| pyrightconfig.json | .ruff_cache/   |
| .gitignore         | .idea/         |
| .python-version    |                |
| README.md          |                |
| .github/workflows/ |                |

### .gitignore 最小模板



```
.venv/
__pycache__/
*.pyc
.idea/
.DS_Store
.pytest_cache/
.ruff_cache/
```

---

## M1-W4-D1【速查表-命令行三种参数类型】

### 命令行三种参数类型

| 类型     | 命令行示例   | typer 写法           | 判断依据           |
| -------- | ------------ | -------------------- | ------------------ |
| 位置参数 | `./file.txt` | `file: str`          | 无默认值           |
| 带值选项 | `--times 3`  | `times: int = 1`     | 有默认值 + 非 bool |
| 开关选项 | `--loud`     | `loud: bool = False` | 有默认值 + bool    |

### typer 最小模板



python

```python
import typer

app = typer.Typer()

@app.command()
def greet(name: str, times: int = 1, loud: bool = False):
    """命令描述（会显示在 --help）"""
    pass

if __name__ == "__main__":
    app()
```

### 多子命令



python

```python
@app.command()
def count():
    """统计文件"""
    ...

@app.command()
def find():
    """查找关键词"""
    ...
```

### 常用命令



bash

```bash
uv add typer                           # 安装 typer
uv run python -m cli_tool.main --help  # 查看帮助
uv run python -m cli_tool.main count --help  # 查看子命令帮助
```

### 命名转换规则

| 函数参数名    | 命令行选项名    |
| ------------- | --------------- |
| `dry_run`     | `--dry-run`     |
| `output_file` | `--output-file` |

---

## M1-W4-D2【速查表-文件读写】

### 文件读写



python

```python
# 正确姿势（自动关闭）
with open("file.txt", "r") as f:
    content = f.read()

# 多文件同时打开
with open("in.txt", "r") as f1, open("out.txt", "w") as f2:
    f2.write(f1.read())
```

### typer 错误退出



python

```python
typer.echo("Error: 描述", err=True)  # 输出到 stderr
raise typer.Exit(code=1)              # 非零退出码
```

### 异常处理顺序（子类在前）



python

```python
except FileNotFoundError:   # 最具体
    ...
except PermissionError:     # 具体
    ...
except OSError as e:        # 兜底
    ...
```

### 可选参数



python

```python
from typing import Optional

def cmd(output: Optional[str] = None):
    if output:  # 检查是否指定
        ...
```

---

------

## M1-W4-D3【速查表-本节知识】

### ThreadPoolExecutor 最小用法



python

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(func, iterable)
```

### 多参数函数处理



python

~~~python
from functools import partial

# 固定部分参数
task = partial(count_one, count_lines=count_lines)
results = executor.map(task, files)
```

### 耗时计算（批次思维）
```
总时间 = ceil(任务数 / worker数) × 单任务耗时

例：10 个任务，4 个 worker，每个 1 秒
→ ceil(10/4) = 3 批 = 3 秒
~~~

### 批量处理错误处理原则



python

```python
# ✅ try-except 在循环内部，单个失败不影响其他
for file in files:
    try:
        process(file)
    except Exception:
        print(error)  # 不 raise，继续下一个

# ❌ try-except 在循环外部，一个失败全部停止
try:
    for file in files:
        process(file)
except Exception:
    ...
```

### 选型口诀

| 场景            | 工具               |
| --------------- | ------------------ |
| 文件 IO（阻塞） | ThreadPoolExecutor |
| 网络 IO（HTTP） | async / asyncio    |

---

## M1-W4-D4【速查表-本节知识】

### 测试场景分类

| 类型 | 含义                         | 典型例子                 |
| ---- | ---------------------------- | ------------------------ |
| 正常 | Happy path，预期使用方式     | 文件存在，返回正确结果   |
| 异常 | Error path，应优雅处理的错误 | 文件不存在，返回错误提示 |
| 边界 | Edge case，极端但合法的输入  | 空文件，返回 0           |

### CLI 测试基本结构



python

```python
from typer.testing import CliRunner
from cli_tool.main import app

runner = CliRunner()

def test_xxx(tmp_path):
    # 1. 准备测试文件
    f = tmp_path / "test.txt"
    f.write_text("content")
    
    # 2. 调用命令
    result = runner.invoke(app, ["命令", "参数", str(f)])
    
    # 3. 断言结果
    assert result.exit_code == 0
    assert "预期输出" in result.stdout
```

### 常用断言

| 断言                     | 用途             |
| ------------------------ | ---------------- |
| `result.exit_code == 0`  | 命令执行成功     |
| `result.exit_code == 1`  | 命令执行失败     |
| `"xxx" in result.stdout` | 输出包含预期内容 |

### 添加 pytest 依赖



bash

```bash
uv add pytest --dev
uv pip install -e .
uv run pytest -v
```

---

