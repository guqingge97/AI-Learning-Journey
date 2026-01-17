"""
 * @Author : 顾清歌
 * @Time : 2026/1/18 00:59
 * @Description: 
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    name: str
    email: str
    age: int
    phone: Optional[int] = None

