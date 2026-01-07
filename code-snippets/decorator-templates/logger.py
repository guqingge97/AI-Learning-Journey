"""
日志装饰器
用途：记录函数调用信息
"""

def logger(func):
    """记录函数调用信息的装饰器"""
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        print(f"参数: {args}")
        if kwargs:
            print(f"关键字参数: {kwargs}")
        
        result = func(*args, **kwargs)
        
        print(f"返回值: {result}")
        return result
    return wrapper

# 使用示例
if __name__ == "__main__":
    @logger
    def add(a, b):
        return a + b
    
    result = add(3, 5)