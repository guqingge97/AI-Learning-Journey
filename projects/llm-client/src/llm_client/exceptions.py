"""
@Author : 顾清歌
@Time : 2026/2/13 00:46
@Description: 
"""

# LLM基类
class LLMError(Exception):
    pass

class LLMTimeoutError (LLMError):
    """
    LLM 请求超时，可重试
    """
    pass

class LLMRateLimitError(LLMError):
    """
    LLM 请求频率过快 429 ，可重试
    """
    pass

class LLMServerError(LLMError):
    """
    LLM 服务器错误  500，可重试
    """
    pass

class LLMAuthError(LLMError):
    """
    LLM 认证错误 401，不可重试
    """
    pass

class LLMRequestError(LLMError):
    """
    LLM 请求错误 422，不可重试
    """
    pass