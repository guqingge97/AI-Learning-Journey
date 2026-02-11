"""
@Author : 顾清歌
@Time : 2026/2/11 22:38
@Description: 
"""



from dataclasses import dataclass

@dataclass
class ChatRequest:
    messages: list[dict[str, str]]
    model: str = "gpt-3.5-turbo"

@dataclass
class ChatResponse:
    content: str
    input_tokens: int
    output_tokens: int

