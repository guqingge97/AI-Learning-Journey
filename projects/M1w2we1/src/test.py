"""
 * @Author : 顾清歌
 * @Time : 2026/1/19 23:44
 * @Description: 
"""
from M1w2we1.src.week2_skeleton.config import load_config

config = load_config()
print(f"api_key: {config.api_key}")
print(f"api_base: {config.api_base}")
print(f"timeout: {config.timeout}, type: {type(config.timeout)}")
print(f"debug: {config.debug}, type: {type(config.debug)}")