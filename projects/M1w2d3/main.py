"""入口脚本 - 演示如何使用模块"""
from M1w2d3.client import MockUserClient, RealUserClient
from M1w2d3.service import UserService


def main():
    # 场景1：使用 Mock 客户端（测试环境）
    print("=== 使用 MockUserClient ===")
    mock_client = MockUserClient()
    service_with_mock = UserService(client=mock_client)
    result = service_with_mock.get_user_display_name("user-001")
    print(f"结果: {result}")
    
    # 场景2：使用真实客户端（生产环境）
    print("\n=== 使用 RealUserClient ===")
    real_client = RealUserClient(base_url="https://api.example.com")
    service_with_real = UserService(client=real_client)
    result = service_with_real.get_user_display_name("user-001")
    print(f"结果: {result}")


if __name__ == "__main__":
    main()
