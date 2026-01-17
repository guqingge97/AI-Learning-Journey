"""用户服务 - 业务逻辑层"""
from M1w2d3.client import UserClient
from M1w2d3.models import User


class UserService:
    """用户服务，处理用户相关业务逻辑"""
    
    def __init__(self, client: UserClient):
        self._client = client
    
    def get_user_display_name(self, user_id: str) -> str:
        """获取用户显示名称"""
        user: User = self._client.get_user(user_id)
        return f"{user.name} <{user.email}>"
