"""
@Author : 顾清歌
@Time : 2026/2/11 22:43
@Description: 
"""
from typing import Protocol
from .models import ChatRequest, ChatResponse

class LLMProvider(Protocol):
    def chat(self, request: ChatRequest) -> ChatResponse: ...