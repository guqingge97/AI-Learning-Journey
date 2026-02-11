"""
@Author : 顾清歌
@Time : 2026/2/11 22:46
@Description: 
"""

from .models import ChatRequest, ChatResponse

class MockProvider:
    def chat(self, request: ChatRequest) -> ChatResponse:
        return ChatResponse(
            content="Hello, this is a mock response.",
            input_tokens=len(request.messages),
            output_tokens=10,
        )