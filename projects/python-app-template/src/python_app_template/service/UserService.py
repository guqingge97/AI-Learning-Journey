"""
@Author : 顾清歌
@Time : 2026/1/22 20:56
@Description: 
"""

from ..client import UserClient
from ..model import User

class UserService:
    """
    @Author : 顾清歌
    @Time : 2026/1/22 20:57
    @Description:
    """
    def __init__(self, user_client: UserClient):
        self.user_client = user_client

    def get_user(self, user_id: int) -> User:
        return self.user_client.get_user(user_id)
