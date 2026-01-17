"""Mock客户端实现 - 用于测试"""
from M1w2d3.models import User


class MockUserClient:
    """Mock用户客户端，返回固定数据"""
    
    def get_user(self, user_id: str) -> User:
        return User(
            id=user_id,
            name="Mock用户",
            email="mock@test.com"
        )
