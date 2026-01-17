"""
 * @Author : 顾清歌
 * @Time : 2026/1/18 01:03
 * @Description: 
"""

from M1w2d4.base.client import User

class RealClient:
    def get_user(self, user_id:str) -> User:
        if user_id == '222':
            return User("222", "222@qq.com", 18, 123456789)
        else:
            return User("None", "None", 0, None)