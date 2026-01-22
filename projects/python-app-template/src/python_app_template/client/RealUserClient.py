"""
@Author : 顾清歌
@Time : 2026/1/22 20:54
@Description: 
"""
from ..model import User

class RealUserClient():
    def get_user(self, user_id: int) -> User:
        return User(id=user_id, name="御姐", age=20)