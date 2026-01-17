"""用户数据模型"""
from dataclasses import dataclass


@dataclass
class User:
    """用户实体"""
    id: str
    name: str
    email: str
