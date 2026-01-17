"""
 * @Author : 顾清歌
 * @Time : 2026/1/18 01:21
 * @Description: 
"""
from M1w2d4.base.service import UserService
from M1w2d4.base.client.mock_client import MockClient
from M1w2d4.base.client.real_client import RealClient

def test_get_user_success():
    # 创建MockClient 注入 UserService
    mock_client = MockClient()
    user_service = UserService(mock_client)

    # 调用 service.get_user("123")
    user = user_service.get_user("123")

    # 验证返回
    assert user.name == "123"

def test_get_user_not_found():
    mock_client = MockClient()
    user_service = UserService(mock_client)
    user = user_service.get_user("222")

    # 验证返回
    assert user.name == "None"

def test_with_real_client():
    real_client = RealClient()
    user_service = UserService(real_client)

    user = user_service.get_user("222")

    # 验证返回
    assert user.name == "222"