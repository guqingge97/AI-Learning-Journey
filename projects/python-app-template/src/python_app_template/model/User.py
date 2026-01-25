"""
@Author : 顾清歌
@Time : 2026/1/22 20:48
@Description:
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: int
    name: str
    age: int
    email: Optional[str] = None
