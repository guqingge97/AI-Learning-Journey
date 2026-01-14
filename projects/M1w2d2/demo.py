"""
 * @Author : 顾清歌
 * @Time : 2026/1/14 21:26
 * @Description: 
"""
"""
M1-W2-D2 演示：Type Hints + dataclass

运行方式：python demo.py
"""
from client import MockUserClient
from service import UserService


def main():
    # 使用 MockUserClient 进行演示
    client = MockUserClient()
    service = UserService(client)

    # 测试用户 123
    user1 = service.get_user("123")
    print(f"用户1: {user1}")
    print(f"  - 名字: {user1.name}")
    print(f"  - 邮箱: {user1.email}")
    print(f"  - 年龄: {user1.age}")
    print(f"  - 显示名称: {service.get_user_display_name('123')}")

    print()

    # 测试用户 456
    user2 = service.get_user("456")
    print(f"用户2: {user2}")
    print(f"  - 名字: {user2.name}")
    print(f"  - 邮箱: {user2.email}")
    print(f"  - 年龄: {user2.age}")
    print(f"  - 显示名称: {service.get_user_display_name('456')}")


if __name__ == "__main__":
    main()