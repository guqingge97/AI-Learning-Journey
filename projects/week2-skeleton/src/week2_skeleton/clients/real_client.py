"""
@Author : 顾清歌
@Time : 2026/1/21 00:03
@Description: 
"""

from .protocol import UserClient
from ..models import User
import requests

class RealUserClient(UserClient):
    def get_user(self, user_id: str) -> User:
        try:
            result = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}", timeout=5)
            if result.status_code != 200:
                return User("None", "None", "None", 0)

            data = result.json()
            return User(data["id"], data["name"], data["email"], data.get("age", 0), data.get("phone"))
        except Exception:
            return User("None", "None", "None", 0)  # 网络异常也返回默认值