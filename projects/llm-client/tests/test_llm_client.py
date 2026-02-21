"""
@Author : 顾清歌
@Time : 2026/2/21 12:41
@Description: 
"""
from llm_client.mock_provider import MockProvider2
from llm_client.client import LLMClient
from llm_client.models import ChatRequest
from llm_client.retry import RetryHandler
from llm_client.exceptions import (
    LLMTimeoutError,
    LLMRateLimitError,
    LLMServerError,
)
import pytest

def test_normal_response():
    retry_handler = RetryHandler(
        retryable_errors=(LLMTimeoutError, LLMRateLimitError, LLMServerError)
    )
    # 1. 创建 MockProvider，预设一个回答
    mock = MockProvider2(responses=["你好"])

    # 2. 把 mock 注入 LLMClient
    client = LLMClient(provider=mock, retry_handler=retry_handler)

    # 3. 发请求
    request = ChatRequest(messages=[{"role": "user", "content": "Hello"}])
    response = client.chat(request)

    # 4. 断言
    assert response.content == "你好"


def test_multiple_responses():
    retry_handler = RetryHandler(
        retryable_errors=(LLMTimeoutError, LLMRateLimitError, LLMServerError)
    )
    mock = MockProvider2(responses=["第一个", "第二个"])
    # 调用两次，分别断言顺序正确

    # 2. 把 mock 注入 LLMClient
    client = LLMClient(provider=mock, retry_handler=retry_handler)

    responses = client.chat(ChatRequest(messages=[{"role": "user", "content": "Hello"}]))
    assert responses.content == "第一个"

    responses = client.chat(ChatRequest(messages=[{"role": "user", "content": "Hello"}]))
    assert responses.content == "第二个"

def test_responses_exhausted():
    retry_handler = RetryHandler(
        retryable_errors=(LLMTimeoutError, LLMRateLimitError, LLMServerError)
    )
    with pytest.raises(ValueError):
        # 只预设1个，调用2次，触发异常
        mock = MockProvider2(responses=["第一个"])
        client = LLMClient(provider=mock, retry_handler=retry_handler)
        client.chat(ChatRequest(messages=[{"role": "user", "content": "Hello"}]))
        client.chat(ChatRequest(messages=[{"role": "user", "content": "Hello"}]))