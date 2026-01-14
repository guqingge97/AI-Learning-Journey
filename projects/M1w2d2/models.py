"""
 * @Author : 顾清歌
 * @Time : 2026/1/14 21:29
 * @Description: 
"""

"""
数据模型定义
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    """用户信息"""
    id: str
    name: str
    email: str
    age: Optional[int] = None