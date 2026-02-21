"""
@Author : 顾清歌
@Time : 2026/2/11 22:46
@Description: 
"""

from .models import ChatRequest, ChatResponse
from .exceptions import LLMError, LLMTimeoutError,LLMAuthError

class MockProvider:
    def chat(self, request: ChatRequest) -> ChatResponse:
        return ChatResponse(
            content="Hello, this is a mock response. {\"intent\": \"查询天气\", \"city\": \"深圳\"}",
            input_tokens=len(request.messages),
            output_tokens=10,
        )


class FailingMockProvider:
    def __init__(self):
        self.call_count = 0

    def chat(self, request):
        self.call_count += 1
        if self.call_count <= 2:
            raise LLMAuthError("认证错误")  # ← 手动抛
        return ChatResponse(content="成功了", input_tokens=len(request.messages), output_tokens=10)


class MockProvider2:
    def __init__(self, responses: list[str]):
        # 把 responses 存起来
        self.responses = responses

    def chat(self, request: ChatRequest) -> ChatResponse:
        if not self.responses:
            raise ValueError("MockProvider 的预设回答已用完")
        # 从存好的列表里取下一个
        # 取出的是字符串，要包装成 ChatResponse 返回
        return ChatResponse(
            content=self.responses.pop(0),
            input_tokens=len(request.messages),
            output_tokens=10,
        )


