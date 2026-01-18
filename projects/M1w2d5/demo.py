'''
"""
 * @Author : 顾清歌
 * @Time : YYYY/MM/DD HH:mm
 * @Description: 
"""
'''

from M1w2d5.base.model import User
from M1w2d5.service import UserService
from M1w2d5.utils.logger import get_logger
from M1w2d5.client import MockUserClient

mock_client = MockUserClient()
user_service = UserService(mock_client)

user = user_service.get_user('1')

