"""
@Author : 顾清歌
@Time : 2026/2/20 16:15
@Description: 
"""
import json
import re


def extract_json(text):
    """
    结构化输出
    :param text:
    :return: 提取出的 JSON 字符串，如果找不到就返回 None
    """
    json_text = re.search(r'\{.*?\}', text, re.DOTALL)
    return json_text.group() if json_text else None


def parse_json(json_text):
    """
    解析 JSON
    :param json_text:
    :return: 解析后的字典
    """
    text = extract_json(json_text)
    try:
        return json.loads(text) if text else None
    except json.JSONDecodeError:
        return None



if __name__ == "__main__":
    # 场景1：正常带废话
    text1 = '结果是 {"a": 1} 另外还有 {"b": 2}'
    print(parse_json(text1))

    # 场景2：格式错误的JSON
    text2 = '{"a": 1,}'
    print(parse_json(text2))
