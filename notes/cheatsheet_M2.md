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

