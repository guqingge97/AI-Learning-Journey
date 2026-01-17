"""真实客户端实现 - 调用外部API"""
from M1w2d3.models import User


class RealUserClient:
    """真实用户客户端，调用外部API"""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
    
    def get_user(self, user_id: str) -> User:
        # 实际项目中这里会调用 requests.get(...)
        # 这里简化，模拟返回
        return User(
            id=user_id,
            name="真实用户",
            email="real@api.com"
        )
