"""
@Author : 顾清歌
@Time : 2026/2/11 22:51
@Description: 
"""

from .provider import LLMProvider
from .models import ChatRequest, ChatResponse

class LLMClient:
    def __init__(self, provider: LLMProvider):
        self.provider = provider

    def chat(self, request: ChatRequest) -> ChatResponse:
        return self.provider.chat(request)