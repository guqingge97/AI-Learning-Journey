"""
 * @Author : 顾清歌
 * @Time : 2026/1/18 01:02
 * @Description: 
"""
from typing import Protocol
from M1w2d4.base.models import User

class UserClient(Protocol):
    def get_user(self, user_id: str) -> User: ...