"""
@Author : 顾清歌
@Time : 2026/2/11 22:51
@Description: 
"""

from .provider import LLMProvider
from .models import ChatRequest, ChatResponse
from .retry import RetryHandler

class LLMClient:
    def __init__(self, provider: LLMProvider, retry_handler: RetryHandler):
        self.provider = provider
        self.retry_handler = retry_handler

    def chat(self, request: ChatRequest) -> ChatResponse:
        return self.retry_handler.execute(self.provider.chat, request)