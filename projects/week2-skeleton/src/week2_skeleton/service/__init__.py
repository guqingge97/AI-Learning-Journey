'''
"""
 * @Author : 顾清歌
 * @Time : YYYY/MM/DD HH:mm
 * @Description:
"""
'''
from ..clients import UserClient
from ..models import User
from ..utils.logger import get_logger

__all__ = ['UserService']
logger = get_logger(__name__)  # 模块加载时只执行一次


class UserService:
    def __init__(self, client: UserClient):
        self.client = client

    def get_user(self, user_id: str) -> User:
        logger.info(f'get user {user_id}')
        user = self.client.get_user(user_id)
        logger.info(f'get user {user_id} result: {user}')
        return user