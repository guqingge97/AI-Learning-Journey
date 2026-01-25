"""
@Author : 顾清歌
@Time : 2026/1/22 20:52
@Description:
"""

from ..model import User


class MockUserClient:
    def get_user(self, user_id: int) -> User:
        """
        获取用户信息
        :param user_id: 用户id
        :return: 用户信息
        """
        return User(id=user_id, name="学生", age=18)
