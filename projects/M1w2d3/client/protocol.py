"""客户端协议定义"""
from typing import Protocol

from M1w2d3.models import User


class UserClient(Protocol):
    """用户客户端接口"""
    
    def get_user(self, user_id: str) -> User:
        """根据ID获取用户"""
        ...
