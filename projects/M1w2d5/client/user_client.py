"""
 * @Author : 顾清歌
 * @Time : 2026/1/18 16:37
 * @Description: 
"""

from typing import Protocol
from M1w2d5.base.model import User


class UserClient(Protocol):
    def get_user(self, user_id: str) -> User:
        ...
