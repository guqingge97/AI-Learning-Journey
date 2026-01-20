"""
@Author : 顾清歌
@Time : 2026/1/20 23:52
@Description:
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: str
    name: str
    email: str
    age: int
    phone: Optional[int] = None