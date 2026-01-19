"""
 * @Author : 顾清歌
 * @Time : 2026/1/19 23:27
 * @Description: 
"""
from dataclasses import dataclass
from dotenv import load_dotenv
import os

@dataclass
class Config:
    """
    配置类
    """
    api_key: str
    api_base: str = "https://api.example.com"
    timeout: int = 30
    debug: bool = False

    def __post_init__(self):
        # 这里会在 __init__ 执行完后自动调用
        if not self.api_key:
            raise ValueError("API_KEY is required")



def load_config():
    # 读取 .env 文件，注入到环境变量
    load_dotenv()
    return Config(
        api_key=os.getenv("API_KEY"),
        api_base=os.getenv("API_BASE", "https://api.example.com"),
        timeout=int(os.getenv("TIMEOUT", 30)),
        debug=str_to_bool(os.getenv("DEBUG", False))
    )


def str_to_bool(value: str) -> bool:
    if isinstance(value, bool):
        return value
    # "true", "1", "yes" → True
    if value.lower() in ["true", "1", "yes"]:
        return True
    # "false", "0", "no" → False
    if value.lower() in ["false", "0", "no"]:
        return False
    raise ValueError(f"Cannot convert '{value}' to bool")