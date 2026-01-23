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

    #方法名：find_user
    #参数：user_id: int
    #返回值类型：User | None（找到返回 User，找不到返回 None）
    #实现逻辑：如果 user_id > 0 就调用 self.user_client.get_user(user_id) 返回，否则返回 None
    def find_user(self, user_id: int) -> User | None:
        if user_id > 0:
            return self.user_client.get_user(user_id)
        else:
            return None