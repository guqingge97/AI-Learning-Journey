"""
 * @Author : 顾清歌
 * @Time : 2026/1/20 23:55
 * @Description: 
"""
from typing import Protocol
from ..models import User

class UserClient(Protocol):
    def get_user(self, user_id: str) -> User: ...