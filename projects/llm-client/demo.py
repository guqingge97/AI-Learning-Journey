"""
@Author : 顾清歌
@Time : 2026/2/11 22:53
@Description: 
"""
from llm_client.models import ChatRequest
from llm_client.client import LLMClient
from llm_client.mock_provider import MockProvider

client = LLMClient(MockProvider())
response = client.chat(ChatRequest(messages=[{"role": "user", "content": "Hello, how are you?"}]))
print(response.content)