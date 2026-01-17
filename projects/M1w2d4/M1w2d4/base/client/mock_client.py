"""
 * @Author : 顾清歌
 * @Time : 2026/1/18 01:03
 * @Description: 
"""

from M1w2d4.base.client import User

class MockClient:
    def get_user(self, user_id:str) -> User:
        if user_id == '123':
            return User("123", "123@qq.com", 18, 13488798765)
        else:
            return User("None", "None", 0, None)