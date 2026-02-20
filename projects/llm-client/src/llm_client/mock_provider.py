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