"""
计时器装饰器
用途：记录函数执行时间
"""
import time

def timer(func):
    """记录函数执行时间的装饰器"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[{func.__name__}] 耗时: {end - start:.4f}秒")
        return result
    return wrapper

# 使用示例
if __name__ == "__main__":
    @timer
    def slow_function():
        time.sleep(1)
        return "完成"
    
    result = slow_function()
    print(f"结果: {result}")