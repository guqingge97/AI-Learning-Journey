'''
"""
 * @Author : 顾清歌
 * @Time : YYYY/MM/DD HH:mm
 * @Description: logger
"""
'''
import logging


def get_logger(name):
    logger = logging.getLogger(name)

    if not logger.handlers:  # 只有没有 handler 时才添加
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

# def get_logger(name):
    # # 获取一个命名 logger
    # logger = logging.getLogger(name)
    #
    # # 设置日志级别
    # logger.setLevel(logging.INFO)
    #
    # # 创建一个文件处理器,输出到控制台
    # console_handler = logging.StreamHandler()
    #
    # # 创建一个格式器
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #
    # # 设置处理器的格式器
    # console_handler.setFormatter(formatter)
    #
    # # 添加处理器
    # logger.addHandler(console_handler)
    #
    # return logger
