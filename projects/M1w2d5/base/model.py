'''
"""
 * @Author : 顾清歌
 * @Time : YYYY/MM/DD HH:mm
 * @Description: 
"""
'''

from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: str
    name: str
    email: str
    age: int
    phone: Optional[int] = None
