"""
@Author : 顾清歌
@Time : 2026/2/13 00:35
@Description: 
"""
import time

class RetryHandler:
    def __init__(self, max_retries=3, base_delay=1, max_delay=10, retryable_errors=()):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.retryable_errors = retryable_errors

    # 判断错误是否是可重试的
    def is_retryable_error(self, error):
        return isinstance(error, self.retryable_errors)

    # 执行操作
    def execute(self, operation, *args, **kwargs):
        retry_count = 0
        while True:
            try:
                return operation(*args, **kwargs)
            except Exception as e:
                if not self.is_retryable_error(e):
                    raise
                if retry_count >= self.max_retries:
                    raise
                retry_count += 1
                delay = self.base_delay * 2 ** (retry_count - 1)
                delay = min(delay, self.max_delay)
                print(f"Retrying operation after {delay} seconds...")
                time.sleep(delay)
