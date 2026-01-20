# Week2 Skeleton

Python 工程骨架示例，演示组合优于继承、依赖注入、配置管理。

## 快速开始

### 1. 安装依赖
```bash
cd week2-skeleton
pip install -e .
```

### 2. 配置环境变量
```bash
cp .env.example .env
# 编辑 .env 填入你的配置
```

### 3. 运行
```bash
python demo.py
```

### 4. 测试
```bash
pytest
```

## 项目结构
```
src/week2_skeleton/
├── clients/       # Client 层（Protocol + Mock + Real）
├── service/       # Service 层（业务逻辑）
├── models/        # 数据模型
├── utils/         # 工具（logger）
└── config.py      # 配置管理
```

## 核心设计

- **组合优于继承**：Service 依赖 Client 接口，不依赖具体实现
- **依赖注入**：Client 从外部传入，可替换 Mock/Real
- **配置管理**：敏感信息放 .env，不进代码库
```

---

### .env.example
```
API_KEY=your_api_key_here
API_BASE=https://api.example.com
TIMEOUT=30
DEBUG=true