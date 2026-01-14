"""
 * @Author : 顾清歌
 * @Time : 2026/1/14 21:27
 * @Description: 
"""
"""
业务服务层
"""
from client import UserClient
from models import User


class UserService:
    """用户服务（依赖 UserClient 接口，不依赖具体实现）"""

    def __init__(self, client: UserClient):
        self.client = client

    def get_user(self, user_id: str) -> User:
        return self.client.get_user(user_id)

    def get_user_display_name(self, user_id: str) -> str:
        """获取用户显示名称"""
        user = self.get_user(user_id)
        if user.age:
            return f"{user.name} ({user.age}岁)"
        return user.name