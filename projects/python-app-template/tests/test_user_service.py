"""
@Author : 顾清歌
@Time : 2026/1/22 20:57
@Description: 
"""
import pytest
from python_app_template.client import MockUserClient
from python_app_template.service import UserService

@pytest.fixture()
def mock_client():
    return MockUserClient()

@pytest.fixture
def user_service(mock_client):
    return UserService(mock_client)

def test_get_user(user_service):       # Arrange（通过 fixture 注入）
    user = user_service.get_user(1)    # Act
    assert user.id == 1                # Assert
    assert user.name == "学生"          # Assert

def test_get_user_age(user_service): # Arrange
    user = user_service.get_user(1) # Act
    assert user.age == 18  # Assert

def test_get_different_user(user_service):
    user = user_service.get_user(2)
    assert user.id == 2