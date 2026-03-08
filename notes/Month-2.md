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

# M2-W5-D4 

**Phase**：Month 2 · Week 5 · Day 4 — LLM API 工程化
 **今日核心目标**：实现 MockProvider，用单元测试验证 LLMClient 的核心行为

------

## Why：不学会导致的工程死穴

没有 Mock，测试就必须真实调用 API：

- **烧钱**：每次跑 CI/CD 都在消耗 API 额度，积少成多
- **慢**：单次 1-3 秒，50 个测试就是 2 分钟，没人愿意频繁跑
- **不稳定**：模型每次返回不同，`assert response == "xxx"` 永远无法成立

结果是：要么不写测试，要么测试形同虚设。

------

## What：第一性原理 + 类比

**MockProvider 本质**：一个实现了 `Provider` 接口的"演员"。

它长得和真实 Provider 一模一样（同样的方法签名），但内部不调用任何网络，只是从预设列表里按顺序取字符串返回。

类比：话剧排练时用道具刀代替真刀——导演（LLMClient）不需要知道是真的还是假的，排练照样进行。

**为什么是实现 Provider 接口，而不是继承 LLMClient？**
 LLMClient 是"调用方"，Provider 是"数据来源方"。Mock 的是数据来源，不是调用逻辑。这正是 D1 学的"组合优于继承"的实际应用。

------

## How：最小可运行范式

### MockProvider

```python
class MockProvider:
    def __init__(self, responses: list[str]):
        self.responses = responses

    def chat(self, request: ChatRequest) -> ChatResponse:
        if not self.responses:
            raise ValueError("MockProvider 的预设回答已用完")
        return ChatResponse(
            content=self.responses.pop(0),
            input_tokens=len(request.messages),
            output_tokens=10,
        )
```

### 三类单元测试

```python
# 场景1：正常返回
def test_normal_response():
    mock = MockProvider(responses=["你好"])
    client = LLMClient(provider=mock, retry_handler=retry_handler)
    response = client.chat(ChatRequest(messages=[{"role": "user", "content": "Hi"}]))
    assert response.content == "你好"

# 场景2：多次调用顺序正确
def test_multiple_responses():
    mock = MockProvider(responses=["第一个", "第二个"])
    client = LLMClient(provider=mock, retry_handler=retry_handler)
    assert client.chat(...).content == "第一个"
    assert client.chat(...).content == "第二个"

# 场景3：预设用完抛异常
def test_responses_exhausted():
    with pytest.raises(ValueError):
        mock = MockProvider(responses=["仅一个"])
        client = LLMClient(provider=mock)
        client.chat(...)  # 第一次成功
        client.chat(...)  # 第二次触发 ValueError
```

------

## Pitfall：真实踩坑

- `pytest.raises` 的 `with` 块里，**异常之后的代码不会执行**。写在里面的 `assert` 如果放在触发异常的代码后面，永远不会跑到，属于无效断言，要删掉。

- `src` 布局下 pytest 找不到模块，需要在 `pyproject.toml` 配置：

  ```toml
  [tool.pytest.ini_options]
  pythonpath = ["src"]
  ```

  否则只能每次手动加 `PYTHONPATH=src` 前缀，容易忘。

- `MockProvider` 的 `responses` 列表**不要在方法参数里传**，要在 `__init__` 里传。方法参数只接受 `ChatRequest`，否则破坏 Protocol 接口一致性，注入进 LLMClient 会报类型错误。

------

## Application：在 RAG/Agent/架构中的位置

```
测试层
  └── test_llm_client.py
        ├── MockProvider（假数据源）  ← 今天
        └── LLMClient（被测对象）

生产层
  └── LLMClient
        └── OpenAIProvider / DeepSeekProvider（真实数据源）
```

MockProvider 在 Month 3 RAG、Month 5 Agent 中同样适用：凡是依赖外部服务的模块，都可以用同样的模式注入 Mock，让整个测试体系脱离网络独立运行。

------

## 视觉闭环

```
测试阶段                    生产阶段
──────────                  ──────────
LLMClient                   LLMClient
    │                           │
    ▼                           ▼
MockProvider               OpenAIProvider
  (假数据，可控)              (真实API，不可控)
  pop(0) 取预设值             HTTP 请求返回
    │                           │
    ▼                           ▼
ChatResponse               ChatResponse
  content="你好"             content="模型真实回复"

两者对 LLMClient 完全透明 → 组合优于继承的价值
```

------

## 工程师记忆分层

🗑️ 垃圾区（查文档）

- `pytest.raises` 的具体语法
- `pyproject.toml` 的配置字段名
- `pop(0)` 还是 `pop(-1)`

🔍 索引区（记关键词）

- Mock = 实现 Provider 接口的假数据源
- src 布局 → pythonpath 配置
- pytest 三段式：准备 / 执行 / 断言

💎 核心区（必须内化）

- **为什么需要 Mock**：省钱 + 够快 + 确定性，缺一不可
- **Mock 在哪一层**：替换 Provider，不替换 LLMClient，体现"组合优于继承"
- **pytest.raises 的语义**：不是"捕获异常"，是"断言必须抛异常，否则测试失败"

---

# M2-W5-D5：LLMClient README 工程文档

## A. 头部

**Phase**：Month 2 - LLM API 工程化 / Week 5 - LLMClient 基础封装

**今日核心目标**：写一份对使用者真正有价值的工程文档，覆盖成本估算、限制说明、最佳实践三块核心内容。

------

## B. 正文

### Why：不学会导致的工程死穴

- 没有成本估算说明 → 用户上生产后被账单吓到，反过来质疑整个库的可用性
- 没有限制说明 → 用户踩坑后才发现"这个库根本不支持多轮对话"，白白浪费调试时间
- 没有最佳实践 → 用户批量处理 10000 条数据，一个未捕获的异常让整个进程崩掉

一份缺少这三块的 README，等于把一个"半成品"扔给用户。

------

### What：第一性原理 + 类比

**工程文档的本质**：是对"潜在踩坑"的提前声明。

类比：买电器的说明书。好的说明书不只告诉你"怎么开机"，还会告诉你"不能在浴室使用（限制）"、"连续使用不超过2小时（最佳实践）"、"每度电消耗多少（成本估算）"。

**成本估算的本质**：token 是 LLM API 的计费单位，成本 = 消耗的 token × 单价。用户需要在上生产前知道大概花多少钱。

**限制说明的本质**：诚实地告诉用户这个库的边界在哪里，比用户自己踩坑发现要好得多。

**最佳实践的本质**：不是"应该这样做"的命令，而是"这样做的原因 + 不这样做的代价"，让用户信服而不是照抄。

------

### How：核心内容范式

#### 成本估算

**公式**：

```
成本 = 总token数 × (单价 / 1000)
```

**gpt-4o-mini 参考单价（2025）**：

- 输入：$0.00015 / 1K tokens
- 输出：$0.00060 / 1K tokens

**从 ChatResponse 提取成本**：

```python
response = client.chat(request)
cost = response.input_tokens * 0.00015/1000 \
     + response.output_tokens * 0.00060/1000
print(f"本次调用成本：${cost:.6f}")
```

**数字例子**：

```
1000次调用，平均输入500token，输出200token，使用gpt-4o-mini：

输入总token = 1000 × 500 = 500,000
输入成本 = 500,000 × $0.00015 / 1000 = $0.075

输出总token = 1000 × 200 = 200,000
输出成本 = 200,000 × $0.00060 / 1000 = $0.12

总成本 = $0.075 + $0.12 = $0.195
```

------

#### 限制说明（五条）

1. **不支持流式输出**：没有实现 streaming，返回的是完整响应
2. **不支持多轮对话**：每次请求不携带历史上下文，LLM 无法感知上一轮内容
3. **重试次数不可动态调整**：当前写死在代码里，无法按场景配置
4. **结构化输出不保证100%成功**：依赖模型能力，格式错误时只能容错处理，无法强制保证
5. **MockClient 仅限测试**：不能用于生产环境，输出是预设的假数据

------

#### 最佳实践（三条）

**1. 批量处理时捕获异常**

- 建议：用 try/except 包住每次调用，失败记录单独存下来统一重跑
- 原因：重试有上限，超过上限会抛异常
- 不这样做：10000条里1%失败就是100条数据丢失，进程可能直接崩掉

**2. 控制 prompt 长度**

- 建议：每次请求只携带关键信息或摘要，避免 prompt 过长
- 原因：LLM 上下文窗口有上限，随对话次数增长，上下文呈线性增长，直至溢出
- 不这样做：上下文溢出后无法继续请求，token 消耗也会异常增大

**3. 测试时使用 MockClient**

- 建议：测试阶段统一使用 MockClient，不调用真实 API
- 原因：真实 API 调用按 token 计费，测试轮次多，费用累积快
- 不这样做：100次测试调用 × 每次 $0.001 = $0.1，大规模测试成本不可忽视

------

### Pitfall：真实踩坑

- 成本公式里单价是"每1000个token"，计算时要除以1000，写成 `price / 1000`，不要直接乘以价格，否则会差1000倍
- 限制说明不要只写"不支持XXX"，要补一句"会导致什么"，否则用户不知道自己是否受影响
- 最佳实践如果只写"建议这样做"而不写"为什么"，用户不会执行，等于没写

------

### Application：在工程链路中的位置

```
代码实现 → 测试通过 → [README 文档] → 用户接入 → 生产使用
```

README 是"代码实现"和"用户接入"之间的桥梁。没有它，用户要么不敢用、要么踩坑后骂人。

在 RAG/Agent 项目中，每一个封装好的模块（LLMClient、tools、prompt-kit）都需要类似的文档，否则协作开发时别人不知道怎么用、边界在哪里。

------

## C. 视觉闭环

```
【一次 API 调用的成本流向】

  ChatRequest
      │
      ▼
  LLMClient.chat()
      │
      ▼
  ChatResponse
  ┌─────────────────────────┐
  │ content                 │
  │ input_tokens  ──┐       │
  │ output_tokens ──┤       │
  └─────────────────┼───────┘
                    │
                    ▼
            成本计算
    input_tokens × 0.00015/1000
  + output_tokens × 0.00060/1000
    ─────────────────────────────
              = 本次成本 $


【README 三块结构关系】

  成本估算         → 帮用户预判账单（上线前决策）
  限制说明         → 帮用户识别边界（避免踩坑）
  最佳实践         → 帮用户正确使用（降低风险）
       └── 三者合一 = 一份负责任的工程文档
```

------

## D. 工程师记忆分层

🗑️ 垃圾区（查文档）

- gpt-4o-mini 具体单价数字（会变，每次查官网）
- tiktoken 的具体 API 用法

🔍 索引区（记关键词）

- 成本公式关键词：`总token × (单价/1000)`
- README 三块：成本估算 / 限制说明 / 最佳实践
- ChatResponse 字段：`input_tokens`、`output_tokens`、`content`

💎 核心区（必须内化）

- 好的最佳实践 = 建议 + 原因 + 不这样做的代价，缺一不可
- 限制说明的意义：诚实声明边界，比用户踩坑后发现要好
- 工程文档是代码和用户之间的桥梁，写文档不是"附加题"，是工程完整性的一部分

---

# M2-W5-WE1

**Phase**：Month 2 - LLM API 工程化
 **今日核心目标**：整理 LLMClient 失败模式清单，建立"失败分类 → 重试策略"的工程直觉

------

## Why

不做失败分类的后果：

- 对所有错误无脑重试 → 401/403 永远重试，白白浪费时间和资源
- 对所有错误不重试 → 超时/限流放弃，系统脆弱
- 响应内容出错不处理 → 上层代码直接崩溃，排查困难

核心死穴：**不分类就没有策略，没有策略就是一个脆弱的系统**。

------

## What

LLM API 调用的失败，按发生位置分三层：

**第一层：网络层** 请求还没到达服务器就失败了。

- 连接超时
- 连接失败（网络不通）
- DNS 解析失败

**第二层：API 服务层** 请求到达了服务器，服务器返回了错误码。

- 401 认证失败（API KEY 错误）
- 403 无权限
- 429 限流（Rate Limit）
- 500 服务器内部错误

**第三层：响应内容层** 请求返回 200，但内容是"坏的"。

- JSON 格式错误（不是合法 JSON）
- 字段缺失（缺少必要字段）
- 不符合 schema（类型错误、枚举值不对）

------

## How

**失败模式清单（最小可用版）**

| 失败场景                | 分类       | 能否重试   | 处理建议                |
| ----------------------- | ---------- | ---------- | ----------------------- |
| 连接超时                | 网络层     | ✅          | 指数退避重试            |
| 连接失败/DNS失败        | 网络层     | ✅          | 指数退避重试            |
| 401 认证失败            | API服务层  | ❌          | 检查并修正 API KEY      |
| 403 无权限              | API服务层  | ❌          | 检查并开通权限          |
| 429 限流                | API服务层  | ✅          | 指数退避重试，间隔更长  |
| 500 服务器错误          | API服务层  | ✅          | 指数退避重试            |
| 响应 JSON 格式错误      | 响应内容层 | ⚠️ 有限重试 | 最多重试1次，失败则报错 |
| 响应字段缺失/schema不符 | 响应内容层 | ⚠️ 有限重试 | 最多重试1次，失败则报错 |

**指数退避核心逻辑**

```python
wait_time = base * (2 ** attempt)
# 例：base=1 → 1s, 2s, 4s, 8s
```

**重试判断口诀**

- 网络层 → 全部可重试
- 4xx → 看具体：429 可重试，401/403 不可重试
- 5xx → 可重试
- 响应内容层 → 有限重试（最多1次）

------

## Pitfall

- 429 限流容易被误归为网络层，实际是 API 服务层（服务器返回了响应）
- 401 和 403 的区别：401 是"你是谁我不认识"，403 是"我认识你但你没资格"
- 响应内容层的失败不能无限重试：同一个 prompt 发两遍输出不同，但如果 prompt 本身设计有问题，重试再多也没用
- 指数退避的 base 和上限要设合理，不然等待时间会爆炸

------

## Application

在 RAG/Agent 架构中的位置：

```
用户请求
   │
   ▼
LLMClient（本周建设的层）
   ├── 网络层失败 → 重试 → 超过上限 → 抛出异常
   ├── API服务层失败 → 分类判断 → 可重试/不可重试
   └── 响应内容层失败 → 有限重试 → 失败则向上报错
   │
   ▼
上层业务逻辑（RAG检索 / Agent执行）
```

失败模式清单是 LLMClient 的"防御工事"，建好了上层才能稳定运行。

------

## 视觉闭环

```
调用 LLM API
      │
      ▼
  请求发出去了吗？
   ├── 否 → [网络层] 超时/连接失败 → ✅ 可重试
   └── 是 → 服务器返回了什么？
              ├── 错误码
              │    ├── 401/403 → ❌ 不可重试（改配置）
              │    ├── 429     → ✅ 可重试（等久一点）
              │    └── 500     → ✅ 可重试
              └── 200 成功
                   ├── JSON 合法且字段完整 → ✅ 正常使用
                   └── JSON 损坏/字段缺失  → ⚠️ 有限重试
```

------

## 工程师记忆分层

🗑️ 垃圾区（查文档就行）

- 各云厂商具体的限流规则（tokens/min 多少）
- requests 库的具体异常类名

🔍 索引区（记关键词，用时能想起来查）

- 三层分类的名字：网络层 / API服务层 / 响应内容层
- 状态码：401=认证失败，403=无权限，429=限流，500=服务器错误
- 指数退避公式结构

💎 核心区（必须内化，不能查）

- 判断能否重试的核心逻辑：**错误是"暂时的"还是"永久的"**
- 响应内容层的失败要有限重试，不是无限重试
- 429 属于 API服务层，不是网络层

---

