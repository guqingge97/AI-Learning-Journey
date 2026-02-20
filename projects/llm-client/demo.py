"""
@Author : 顾清歌
@Time : 2026/2/11 22:53
@Description: 
"""
from llm_client.models import ChatRequest
from llm_client.client import LLMClient
from llm_client.mock_provider import MockProvider
from llm_client.retry import RetryHandler
from llm_client.mock_provider import FailingMockProvider
from llm_client.exceptions import (
    LLMTimeoutError,
    LLMRateLimitError,
    LLMServerError,
    LLMAuthError,
    LLMRequestError,
)


retry_handler = RetryHandler(
    retryable_errors=(LLMTimeoutError, LLMRateLimitError, LLMServerError)
)
provider = MockProvider()
client = LLMClient(provider=provider, retry_handler=retry_handler)

response = client.chat(ChatRequest(messages=[{"role": "user", "content": "Hello, how are you?"}]))
print(response.content)