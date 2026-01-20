"""
@Author : 顾清歌
@Time : 2026/1/21 00:03
@Description: 
"""

from ..models import User
from .protocol import UserClient


class MockUserClient(UserClient):
    def get_user(self, user_id: str) -> User:
        return User(user_id, "mock_name", "mock_email", 18)