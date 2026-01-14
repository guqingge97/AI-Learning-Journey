"""
 * @Author : 顾清歌
 * @Time : 2026/1/13 19:45
 * @Description: 组合优于继承
"""

"""
M1-W2-D1: 组合优于继承
演示：可替换的 Client (Real/Mock) + Service 依赖接口
"""
from typing import Protocol


# ============ 1. 定义接口 ============
class UserClient(Protocol):
    """用户客户端接口（约定）"""
    def fetch_user(self, user_id: str) -> dict: ...


# ============ 2. 实现类 ============
class RealClient:
    """真实 API 客户端"""
    def fetch_user(self, user_id: str) -> dict:
        # 实际项目中这里会调用真实 API
        # response = requests.get(f"https://api.example.com/users/{user_id}")
        # return response.json()
        return {"id": user_id, "name": "真实用户", "source": "api"}


class MockClient:
    """模拟客户端（用于测试）"""
    def fetch_user(self, user_id: str) -> dict:
        return {"id": user_id, "name": "模拟用户", "source": "mock"}


# ============ 3. 业务类 ============
class UserService:
    """用户服务（依赖接口，不依赖具体实现）"""
    def __init__(self, client: UserClient):
        self.client = client

    def get_user(self, user_id: str) -> dict:
        return self.client.fetch_user(user_id)


# ============ 4. 测试代码 ============
if __name__ == "__main__":
    # 使用 MockClient
    print("=== 使用 MockClient ===")
    mock_client = MockClient()
    service = UserService(mock_client)
    result = service.get_user("123")
    print(result)

    # 使用 RealClient（只需换一行）
    print("\n=== 使用 RealClient ===")
    real_client = RealClient()
    service = UserService(real_client)
    result = service.get_user("123")
    print(result)