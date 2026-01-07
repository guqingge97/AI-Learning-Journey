# 装饰器模板

Day 4 学习的装饰器模板，可以直接复用。

## timer.py
计时器装饰器，记录函数执行时间。

**使用：**
```python
from timer import timer

@timer
def my_function():
    # 你的代码
    pass
```

## logger.py
日志装饰器，记录函数调用信息（函数名、参数、返回值）。

**使用：**
```python
from logger import logger

@logger
def my_function(a, b):
    return a + b
```

## 通用装饰器模板
```python
def my_decorator(func):
    """装饰器说明"""
    def wrapper(*args, **kwargs):
        # 执行前的操作
        
        result = func(*args, **kwargs)
        
        # 执行后的操作
        
        return result
    return wrapper
```

## 学习笔记
- 装饰器本质：接收函数，返回新函数
- 必须用 `*args, **kwargs` 处理参数
- 必须 `return result` 保持原函数行为
- 闭包：内层函数记住外层变量

---

**Day 4 - 2026-01-08**