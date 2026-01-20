"""
@Author : 顾清歌
@Time : 2026/1/21 00:19
@Description: 
"""

from week2_skeleton.service import UserService
from week2_skeleton.clients import MockUserClient
from week2_skeleton.clients import RealUserClient


def test_get_user_success():
    mock_client = MockUserClient()
    user_service = UserService(mock_client)
    user = user_service.get_user("123")

    # 验证 Mock 返回的可预测数据
    assert user.id == "123"
    assert user.name == "mock_name"
    assert user.email == "mock_email"


def test_get_user_not_found():
    # MockUserClient 不区分"存在/不存在"，都返回相同结构
    # 这个测试验证：任意 user_id 都能返回有效对象
    mock_client = MockUserClient()
    user_service = UserService(mock_client)
    user = user_service.get_user("any_id")

    assert user is not None
    assert user.name == "mock_name"


def test_with_real_client():
    real_client = RealUserClient()
    user_service = UserService(real_client)
    user = user_service.get_user("1")  # 用存在的 id

    assert user.name == "Leanne Graham"  # jsonplaceholder 固定数据

