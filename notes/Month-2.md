# M2-W5-D1

## Phase: Month 2 - LLM API 工程化 | Week 5 - LLMClient 基础封装

**今日核心目标**：设计可替换的 LLM 调用层骨架（接口 + 数据结构 + Provider 抽象）

------

### Why：不学会导致的工程死穴

直接在业务代码里写 `openai.ChatCompletion.create(...)` 会怎样？

- 换模型供应商（OpenAI → DeepSeek → 本地 Ollama）要**改所有调用点**
- 测试时必须真实调 API，每跑一次测试就烧钱
- 输入输出格式散落各处，没有统一的数据结构，后续加日志/重试/缓存无处下手

Java 后端经验对照：你项目里封装了 HttpGetClient/HttpPostClient，Service 注入 Client 而不是直接 new——LLMClient + Provider 是完全相同的思路。

------

### What：第一性原理

**核心公式**：

> LLMClient（调用入口）= Provider 抽象（谁来做）+ 数据结构（输入输出长什么样）

三个角色的关系：

- **ChatRequest / ChatResponse**：定义"数据长什么样"
- **LLMProvider（Protocol）**：定义"能做什么"——有 chat 方法就行
- **LLMClient**：定义"怎么用"——持有 Provider 引用，调用 chat

类比：餐厅模型

- ChatRequest = 点菜单（菜名、口味要求）
- ChatResponse = 上的菜（菜本身 + 小票价格）
- LLMProvider = 厨师接口（能做菜就行，不管是中餐厨师还是西餐厨师）
- LLMClient = 服务员（接单 → 递给厨师 → 把菜端回来）

------

### How：最小可运行范式

**项目结构：**

```
llm-client/
  src/llm_client/
    models.py          ← 数据结构
    provider.py         ← 抽象接口
    mock_provider.py    ← 测试用实现
    client.py           ← 调用入口
  demo.py               ← 串联验证
```

**models.py — 数据结构：**

```python
@dataclass
class ChatRequest:
    messages: list[dict[str, str]]   # [{"role": "user", "content": "..."}]
    model: str = "gpt-3.5-turbo"

@dataclass
class ChatResponse:
    content: str
    input_tokens: int      # 输入 token（计费用）
    output_tokens: int     # 输出 token（单价不同，必须分开记）
```

**provider.py — 抽象接口：**

```python
class LLMProvider(Protocol):
    def chat(self, request: ChatRequest) -> ChatResponse: ...
```

**client.py — 调用入口（组合模式）：**

```python
class LLMClient:
    def __init__(self, provider: LLMProvider):
        self.provider = provider

    def chat(self, request: ChatRequest) -> ChatResponse:
        return self.provider.chat(request)
```

**使用方式：**

```python
client = LLMClient(MockProvider())       # 测试环境
client = LLMClient(DeepSeekProvider())   # 生产环境
# LLMClient 代码零修改
```

------

### Pitfall：真实踩坑

- **token 只记一个总数**：输入和输出单价不同（GPT-4 输出单价是输入的 3 倍），不分开记就算不清成本
- **messages 类型写 list 不加泛型**：别人看不出里面是什么结构，后续维护成本高
- **过早分目录**：3 个文件就分 models/ 和 client/ 两个子目录，导致 import 路径变深、容易出错。文件少于 10 个时保持扁平
- **demo.py 用相对导入**：项目根目录的脚本不在包内，不能用 `from .xxx`，要用包名直接导入

------

### Application：在 RAG/Agent/架构中的位置

本周（W5）全貌：D1 接口设计（今天，骨架）→ D2 超时+重试 → D3 结构化输出 → D4 Mock 测试 → D5 README+成本估算

后续复用：W6 Tools 调用 LLMClient → W8 FastAPI 包装 LLMClient → M3 RAG 检索结果注入 messages → M5 Agent 多轮调用+工具

------

### 视觉闭环

```
┌─────────────┐
│  业务代码     │  demo.py / Service / Agent
│  (调用方)     │
└──────┬──────┘
       │ 依赖
       ▼
┌─────────────┐
│  LLMClient   │  持有 Provider，转发 chat()
└──────┬──────┘
       │ 组合（不是继承）
       ▼
┌─────────────┐     ┌─────────────────┐
│ LLMProvider  │◄────│ Protocol 接口     │
│ (抽象)       │     │ chat(req) -> res │
└──────┬──────┘     └─────────────────┘
       │ 实现（鸭子类型）
       ▼
  ┌──────────┬──────────┬──────────┐
  │MockProv  │DeepSeek  │OpenAI    │  ← 新增不改 Client
  │(测试)    │Prov      │Prov      │
  └──────────┴──────────┴──────────┘

数据流：
ChatRequest ──→ Provider.chat() ──→ ChatResponse
(messages,      (各家API实现)        (content,
 model)                              input_tokens,
                                     output_tokens)
```

------

### 工程师记忆分层

- 🗑️ **垃圾区（查文档）**：dataclass 装饰器语法、Protocol 的 import 路径、PyCharm 的 Sources Root 配置
- 🔍 **索引区（记关键词）**：messages 结构是 role + content、token 分 input/output、src 布局包内相对导入 `from .xxx`
- 💎 **核心区（必须内化）**：Provider 抽象的目的是新增实现不改调用方、LLMClient 组合模式 `__init__` 接收接口、鸭子类型不需要继承只需方法签名一致、文件少时保持扁平别过早分目录

---

# M2-W5-D2

## Phase

Month 2 · LLM API 工程化 · Week 5 LLMClient 基础封装 · Day 2 超时控制 + 指数退避重试

## 今日核心目标

为 LLMClient 加上"防御层"——错误分类 + 指数退避重试，让 API 调用在网络抖动和服务端故障下不会一碰就死。

------

## Why：不学会导致的工程死穴

LLM API 调用本质是远程网络请求，100% 会遇到超时、限流、服务端故障。没有重试机制的 LLMClient：

- 一次网络抖动就整个功能不可用
- 429 限流后疯狂重试 → 重试风暴（Retry Storm） → 服务端更加过载
- 401/422 这种永久错误也在傻傻重试 → 浪费时间、浪费钱

生产环境没有重试 = 裸奔。

------

## What：第一性原理 + 类比

### 错误分类：Transient vs Permanent

核心判断标准：**这个错误是"暂时的"还是"永久的"？**

- **Transient（暂时性）**：超时、429、500 → 下次可能好 → 值得重试
- **Permanent（永久性）**：401、422 → 重试一万次也没用 → 直接抛出

类比：打电话没接（暂时的，过会儿再打），号码是空号（永久的，打多少次都没用）。

### 指数退避（Exponential Backoff）

问题：重试等多久？固定等 1 秒 → 所有客户端同时重试 → 重试风暴。

解法：每次重试，等待时间翻倍。

公式：`delay = min(base_delay × 2^attempt, max_delay)`

- attempt 0 → 1s
- attempt 1 → 2s
- attempt 2 → 4s
- attempt 3 → 8s

max_delay 是安全阀，防止等待时间指数爆炸。

进阶：Jitter（随机抖动）在等待时间上加随机偏移，进一步打散重试时机。

------

## How：最小可运行范式

### 核心组件：RetryHandler

```python
class RetryHandler:
    def __init__(self, max_retries=3, base_delay=1, max_delay=10, retryable_errors=()):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.retryable_errors = retryable_errors

    def is_retryable_error(self, error) -> bool:
        return isinstance(error, self.retryable_errors)

    def execute(self, operation, *args, **kwargs):
        retry_count = 0  # 局部变量，不是实例属性！
        while True:
            try:
                return operation(*args, **kwargs)
            except Exception as e:
                if not self.is_retryable_error(e):
                    raise
                if retry_count >= self.max_retries:
                    raise
                retry_count += 1
                delay = min(self.base_delay * 2 ** (retry_count - 1), self.max_delay)
                time.sleep(delay)
```

### 组合进 LLMClient

```python
class LLMClient:
    def __init__(self, provider: LLMProvider, retry_handler: RetryHandler):
        self.provider = provider
        self.retry_handler = retry_handler

    def chat(self, request: ChatRequest) -> ChatResponse:
        return self.retry_handler.execute(self.provider.chat, request)
```

### 异常体系

```python
class LLMError(Exception): pass          # 基类，必须继承 Exception
class LLMTimeoutError(LLMError): pass    # 可重试
class LLMRateLimitError(LLMError): pass  # 可重试
class LLMServerError(LLMError): pass     # 可重试
class LLMAuthError(LLMError): pass       # 不可重试
class LLMRequestError(LLMError): pass    # 不可重试
```

### 组装

```python
retry_handler = RetryHandler(
    retryable_errors=(LLMTimeoutError, LLMRateLimitError, LLMServerError)
)
client = LLMClient(provider=provider, retry_handler=retry_handler)
```

------

## Pitfall：真实踩坑

- **retry_count 放成实例属性**：第一次调用重试 2 次后，第二次调用只剩 1 次重试额度。必须是 execute() 内的局部变量，每次调用互相独立
- **LLMError 忘记继承 Exception**：Python 不允许 raise 一个非异常对象，`raise LLMTimeoutError()` 会直接报 TypeError
- **retryable_errors 默认空 tuple**：不传 = 什么都不重试。`isinstance(error, ())` 永远 False
- **ChatResponse 缺字段**：FailingMockProvider 成功返回时忘了传 input_tokens/output_tokens，dataclass 会报 missing arguments

------

## Application：在 RAG / Agent / 架构中的位置

- **RAG**：检索时调 Embedding API + 生成时调 LLM API，任何一步都需要重试
- **Agent**：工具调用失败、LLM 规划失败，都走 RetryHandler 的重试逻辑
- **生产服务**：Month 6 会加更完整的观测（重试次数指标、失败率告警），RetryHandler 是观测数据的来源

------

## 视觉闭环

```
chat(request)
    │
    ▼
RetryHandler.execute()
    │
    ├─ try: provider.chat(request) ──→ 成功 → 返回 ChatResponse
    │
    └─ except:
        │
        ├─ is_retryable? ──No──→ 直接 raise（401/422）
        │
        └─ Yes
            │
            ├─ 超过 max_retries? ──Yes──→ raise
            │
            └─ No → sleep(delay) → 回到 try
                     delay = min(base × 2^attempt, max)

组合关系：
┌────────────────────────────────┐
│ LLMClient                      │
│  ├── provider: LLMProvider     │  ← D1
│  └── retry_handler: RetryHandler│ ← D2
│       ├── retryable_errors     │
│       └── execute() 包裹调用    │
└────────────────────────────────┘
```

------

## 工程师记忆分层

- 🗑️ 垃圾区（查文档）：time.sleep() 的精确用法、isinstance 支持 tuple 的语法细节
- 🔍 索引区（记关键词）：Jitter 随机抖动、Retry Storm 重试风暴、min() 封顶
- 💎 核心区（必须内化）：Transient vs Permanent 错误分类决定重试策略；指数退避公式 `min(base × 2^attempt, max)`；RetryHandler 独立于 LLMClient，通过组合注入；retry_count 必须是局部变量不是实例属性

---

# M2-W5-D3（结构化输出：JSON schema约束+解析容错）

## A. 头部

- **Phase**：Month 2 - LLM API 工程化 / Week 5 - LLMClient 基础封装
- **今日核心目标**：当 LLM 输出不是纯 JSON 时，能稳定提取并解析，失败时优雅降级

------

## B. 正文

### Why：不学会导致的工程死穴

LLM 本质是文字接龙引擎，不是 JSON 生成器。即使 prompt 里写了"只返回 JSON"，它仍可能：

- 在 JSON 前后加解释文字
- 用单引号代替双引号
- 字段名拼错、多逗号

如果不做容错，`json.loads()` 一报错，整个请求链路就崩了。生产环境里这种问题每天都会发生。

------

### What：第一性原理 + 类比

结构化输出失败有三种形式：

- **包裹文本**：JSON 被自然语言包裹（最常见）
- **格式错误**：单引号、多余逗号、缺字段
- **内容缺失**：字段不全或类型不对

类比：就像快递员把包裹塞在一个大纸箱里，外面还缠了胶带和废纸。你要先拆包装（extract），再检查货物是否完好（parse），坏了就记录问题（except），不能直接扔掉整个快递。

------

### How：最小可运行范式

**第一步：提取——从文本里找 JSON**

```python
import re

def extract_json(text: str) -> str | None:
    match = re.search(r'\{.*?\}', text, re.DOTALL)
    return match.group() if match else None
```

关键点：

- `.*?` 非贪婪：找到第一个完整 `{...}` 就停，不会把两个 JSON 中间的文字也吞进去
- `re.DOTALL`：让 `.` 能匹配换行符，处理多行 JSON

**第二步：解析——提取后做容错 parse**

```python
import json

def parse_json(text: str) -> dict | None:
    raw = extract_json(text)
    try:
        return json.loads(raw) if raw else None
    except json.JSONDecodeError:
        return None
```

**第三步：集成到 LLMClient**

```python
content = parse_json(response.content) or response.content
# 解析成功 → 返回字典
# 解析失败（None）→ or fallback，返回原始字符串，不丢数据
```

------

### Pitfall：真实踩坑

- 正则里用了中文全角问号 `？` → 匹配失败，返回 None，排查半天找不到原因
- `try/except` 里忘了 `return` → 解析成功也返回 None，数据默默丢失
- Mock 数据用单引号 `'a': 1` → `json.loads` 报错，误以为 parse_json 有 bug，其实是测试数据不合法
- `.*` 贪婪匹配 → 两个 JSON 之间的文字被吞进去，拿到一个无法解析的大字符串

------

### Application：在 RAG/Agent/架构中的位置

```
用户请求
    ↓
LLMClient.chat()
    ↓
Provider 返回原始文本
    ↓
parse_json()  ← 今天的位置
    ↓
返回字典（成功）或原始字符串（失败）
    ↓
调用方
```

在 RAG 里，LLM 生成带引用的结构化答案（如 `{"answer": "...", "sources": [...]}`），必须用今天的方法解析。Agent 里，LLM 决策下一步工具调用时返回的也是 JSON，解析失败会导致整个 Agent 卡死。

------

## C. 视觉闭环

```
LLM 原始输出
"好的，分析结果：{\"intent\": \"查询\", \"city\": \"深圳\"} 希望有帮助"
        │
        ▼
  extract_json()
  re.search(r'\{.*?\}')
        │
        ├─ 找到 → "{\"intent\": \"查询\", \"city\": \"深圳\"}"
        │
        ▼
   parse_json()
   json.loads()
        │
        ├─ 成功 → {"intent": "查询", "city": "深圳"}  ✅
        │
        └─ 失败 → None → or → 原始字符串 fallback     ⚠️
```

------

## D. 工程师记忆分层

🗑️ **垃圾区（查文档）**

- `re.DOTALL` 的具体数值
- `json.JSONDecodeError` 的完整继承链
- `re.search` vs `re.match` vs `re.findall` 的全部差异

🔍 **索引区（记关键词）**

- 提取 JSON 用正则 `\{.*?\}`，非贪婪
- 解析失败用 `json.JSONDecodeError` 捕获
- fallback 用 `or` 原始字符串

💎 **核心区（必须内化）**

- LLM 不保证输出纯 JSON，容错是工程必选项，不是可选项
- 三种失败形式：包裹文本 / 格式错误 / 内容缺失
- 解析逻辑放在 LLMClient 内部，调用方不应该关心这个细节（封装原则）
- 失败时不能丢数据，要 fallback 到原始字符串

---

