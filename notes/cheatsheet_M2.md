## M2-W5-D1【速查表-LLMClient接口与Provider抽象】

| 概念          | 要点                                                         |
| ------------- | ------------------------------------------------------------ |
| ChatRequest   | `messages: list[dict[str, str]]` + `model: str`，messages 是 role/content 的消息列表 |
| ChatResponse  | `content: str` + `input_tokens: int` + `output_tokens: int`，token 分开记是因为输入输出单价不同 |
| LLMProvider   | Protocol 接口，只定义 `def chat(self, request) -> ChatResponse: ...` |
| LLMClient     | 持有 Provider 引用，`__init__(self, provider: LLMProvider)`，组合模式 |
| MockProvider  | 不继承 LLMProvider，鸭子类型——方法签名一致即可               |
| 新增 Provider | 只需新建类实现 `chat` 方法，LLMClient 代码零修改             |
| src 布局导入  | 包内用相对导入 `from .models import ...`，外部用包名 `from llm_client.models import ...` |
| 运行方式      | `uv run python demo.py`（uv 自动处理 src 布局路径）          |

------

---

## M2-W5-D2【速查表-本节知识】

### 错误分类

| 类型      | 含义                   | 可重试？ | 举例           |
| --------- | ---------------------- | -------- | -------------- |
| Transient | 暂时性故障，下次可能好 | ✅        | 超时、429、500 |
| Permanent | 永久性错误，重试也没用 | ❌        | 401、422       |

### 指数退避公式



```
delay = min(base_delay × 2^attempt, max_delay)
```

- `base_delay=1, max_delay=10` 时：1s → 2s → 4s → 8s → 10s(封顶)
- Jitter（随机抖动）：防止多客户端同时重试引发重试风暴

### RetryHandler 核心结构



python

~~~python
class RetryHandler:
    def __init__(self, max_retries, base_delay, max_delay, retryable_errors):
        ...

    def is_retryable_error(self, error) -> bool:
        return isinstance(error, self.retryable_errors)

    def execute(self, operation, *args, **kwargs):
        # retry_count 是局部变量（不是实例属性！）
        # 循环：try → catch → 判断可重试？→ 超次数？→ 计算delay → sleep → 重试
```
~~~

### 组合关系
```
LLMClient
├── provider: LLMProvider        ← D1 建的
├── retry_handler: RetryHandler  ← D2 新增
└── chat() → retry_handler.execute(provider.chat, request)
```

### 自定义异常体系
```
Exception
  └── LLMError（基类）
        ├── LLMTimeoutError    → 可重试
        ├── LLMRateLimitError  → 可重试
        ├── LLMServerError     → 可重试
        ├── LLMAuthError       → 不可重试
        └── LLMRequestError    → 不可重试
```

### 关键设计决策

- RetryHandler 独立成类 → 可复用（LLMClient、Tool调用、Embedding 都能用）
- retryable_errors 由外部传入 → RetryHandler 不耦合业务错误类型
- retry_count 是局部变量 → 每次 execute() 调用互不影响

### 组装方式（demo.py）



python

```python
retry_handler = RetryHandler(
    retryable_errors=(LLMTimeoutError, LLMRateLimitError, LLMServerError)
)
provider = SomeProvider()
client = LLMClient(provider=provider, retry_handler=retry_handler)
```

---

---

