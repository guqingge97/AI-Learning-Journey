"""
@Author : 顾清歌
@Time : 2026/1/22 20:47
@Description:
"""

from typing import Protocol

from ..model import User


class UserClient(Protocol):
    def get_user(self, user_id: int) -> User: ...
