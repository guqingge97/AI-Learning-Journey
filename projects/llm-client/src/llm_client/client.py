"""
@Author : 顾清歌
@Time : 2026/2/11 22:51
@Description: 
"""

from .provider import LLMProvider
from .models import ChatRequest, ChatResponse
from .retry import RetryHandler
from structured_output import parse_json

class LLMClient:
    def __init__(self, provider: LLMProvider, retry_handler: RetryHandler):
        self.provider = provider
        self.retry_handler = retry_handler

    def chat(self, request: ChatRequest) -> ChatResponse:
        responese = self.retry_handler.execute(self.provider.chat, request)
        return ChatResponse(
            content=parse_json(responese.content) or responese.content,
            input_tokens=responese.input_tokens,
            output_tokens=responese.output_tokens,
        )