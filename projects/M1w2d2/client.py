"""
 * @Author : 顾清歌
 * @Time : 2026/1/14 21:27
 * @Description: 
"""

"""
客户端接口定义与实现
"""
from typing import Protocol
from models import User


class UserClient(Protocol):
    """用户客户端接口"""
    def get_user(self, user_id: str) -> User: ...


class RealUserClient:
    """真实客户端实现（调用外部 API）"""
    def get_user(self, user_id: str) -> User:
        # 实际项目中这里会调用真实的 API
        # response = requests.get(f"https://api.example.com/users/{user_id}")
        # return User(**response.json())
        raise NotImplementedError("真实 API 调用待实现")


class MockUserClient:
    """模拟客户端实现（用于测试）"""
    def get_user(self, user_id: str) -> User:
        if user_id == "123":
            return User("123", "沈清涵", "aaa@163.com", age=25)
        else:
            return User("222", "顾清歌", "bbb@163.com")