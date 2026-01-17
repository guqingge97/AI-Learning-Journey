"""
 * @Author : 顾清歌
 * @Time : 2026/1/18 01:16
 * @Description: 
"""

from M1w2d4.base.models import User
from M1w2d4.base.client import UserClient

class UserService:
    def __init__(self, client: UserClient):
        self.client = client

    def get_user(self, user_id: str) -> User:
        return self.client.get_user(user_id)
