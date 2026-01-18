'''
"""
 * @Author : 顾清歌
 * @Time : YYYY/MM/DD HH:mm
 * @Description: 
"""
'''

from M1w2d5.base.model import User
from .user_client import UserClient


class MockUserClient(UserClient):
    def get_user(self, user_id: str) -> User:
        return User(user_id, "mock_name", "mock_email", 18)
