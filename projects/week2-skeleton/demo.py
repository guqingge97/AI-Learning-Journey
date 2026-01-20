"""
Week2 Skeleton Demo
"""
from week2_skeleton.config import load_config
from week2_skeleton.clients import MockUserClient, RealUserClient
from week2_skeleton.service import UserService


def main():
    # 1. 加载配置
    config = load_config()
    print(f"Config loaded: debug={config.debug}")

    # 2. 选择 Client（可以根据 config.debug 切换）
    if config.debug:
        client = MockUserClient()
        print("Using MockUserClient")
    else:
        client = RealUserClient()
        print("Using RealUserClient")

    # 3. 注入到 Service
    service = UserService(client)

    # 4. 调用
    user = service.get_user("1")
    print(f"Result: {user}")


if __name__ == "__main__":
    main()