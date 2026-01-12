# AI-Learning-Journey

> 从 Java 后端到 AI 应用开发的完整学习记录
>  学习周期：8个月（32周）| 目标：深圳中厂 LLM 应用开发 / AI 后端

------

## 📍 当前进度

**CurrentAnchor**: `M1-W2-D1`
 **上次完成**: M1-W1-WE2 (Week 1 周验收)
 **今日任务**: 组合优于继承（Composition over Inheritance）

**进度追踪**:

- ✅ Month 1 Week 1 (M1-W1-D1 到 M1-W1-WE2) - Python 核心强化
- 🔄 Month 1 Week 2 (M1-W2) - OOP + 类型系统

------

## 🎯 学习目标

**最终目标**：

- 能独立开发企业知识库问答系统（RAG）
- 能开发 AI Agent 执行自动化任务
- 能把 AI 集成到现有 Java 后端项目
- 能拿作品集面试，找到 AI 开发工作（15-25K）

**不走的路**：

- ❌ 算法研究岗
- ❌ 模型训练岗
- ✅ 专注应用开发 + 工程落地

------

## 📚 学习路线

完整路线参见：[LEARNING_ROUTE_TEMPLATE.md](https://claude.ai/chat/docs/LEARNING_ROUTE_TEMPLATE.md)

### Anchor 命名规则

- 格式：`M{month}-W{week}-D{day}` 或 `M{month}-W{week}-WE{n}`
- 例如：`M1-W2-D1` = Month1 Week2 Day1
- 每周：5个工作日（D1-D5）+ 周末（WE1/WE2，可选）

### 路线总览（8个月 / 32周）

```
Month 1 (Week 1-4)   → Python 工程基石
Month 2 (Week 5-8)   → LLM API 工程化
Month 3 (Week 9-12)  → RAG 数据工程
Month 4 (Week 13-16) → RAG 评测闭环
Month 5 (Week 17-20) → Agent 开发
Month 6 (Week 21-24) → 生产化（观测/成本/部署）
Month 7 (Week 25-28) → Java 混合落地 + 系统设计
Month 8 (Week 29-32) → 面试冲刺
```

------

## 📂 项目结构

```
AI-Learning-Journey/
├── README.md                          # 本文件
├── docs/                              # 核心文档
│   ├── 01-教学协议.md                  # Teaching Mode 规则
│   ├── 02-学员档案.md                  # 个人背景与目标
│   ├── 03-学习路线总览.md              # 路线概览（旧版）
│   ├── 04-学习进度追踪.md              # 进度记录
│   ├── 05-教学风格记录.md              # 有效教学方式
│   ├── 06-代码规范与模板.md            # 代码规范
│   ├── 07-常见问题FAQ.md               # 常见问题
│   ├── 08-Git工作流程.md               # Git 操作指南
│   └── LEARNING_ROUTE_TEMPLATE.md      # 详细学习路线（32周精确拆解）
├── notes/                             # 学习笔记
│   ├── m1w1d1.md                      # Day 1 笔记
│   ├── m1w1-review.md                 # Week 1 复习笔记
│   └── ...
├── projects/                          # 项目代码
│   ├── week1-generator-demo/          # Week 1 生成器 demo
│   ├── week1-decorator-demo/          # Week 1 装饰器 demo
│   ├── week2-composition-client/      # Week 2 组合模式 demo
│   └── ...
└── progress.md                        # 学习进度快照
```

------

## 🔄 日常工作流

### 每天学习流程

1. **开新窗口**（Claude.ai Projects）
2. **说明 Anchor**：`十香，M1-W2-D1，开始`
3. **学习 + 产出**：demo / snippet / notes（2小时内完成）
4. **Git commit**：提交当天产出
5. **关闭窗口**

### Git Commit 规范

```bash
# Day 学习
git commit -m "M1-W2-D1: 组合优于继承 demo"

# Week 验收
git commit -m "M1-W2-WE2: Week 2 验收完成"

# 文档更新
git commit -m "docs: 更新学习进度"
```

------

## 📊 学习数据

### 时间投入

- **开始日期**：2026-01-06
- **当前累计**：~14 小时（Week 1）
- **目标总时长**：~480 小时（8个月）

### 已完成内容

- ✅ Python 核心特性（推导式/生成器/装饰器/上下文/async）
- ✅ Week 1 综合复习与验收

### 代码产出

- 项目数：5+ demos
- 代码行数：~500 行

------

## 🎓 教学协议

### Teaching Mode（默认）

- 小步慢行，必须中途互动
- 每讲完一个概念，必须提问/复述/验证
- 禁止直接给完整答案或完整笔记

### Notebook Mode（明确触发）

**触发条件**：

- 说："可以整理今天的【全栈宗师笔记】了"
- 或："进入 Notebook Mode，总结今天内容"

**笔记结构**：

- Why / What / How / Pitfall / Application
- ASCII 流程图
- 工程师记忆分层（垃圾区/索引区/核心区）

------

## 🔧 技术栈

### 当前已学（Month 1）

- **语言**：Python 3.x
- **核心特性**：推导式、生成器、装饰器、上下文管理器、async/await
- **工具**：Git、VS Code

### 即将学习（Month 2+）

- **AI 框架**：OpenAI API、LangChain
- **向量数据库**：Chroma / Qdrant
- **服务化**：FastAPI、Docker
- **测试**：pytest
- **观测**：日志、指标、追踪

------

## 📈 里程碑

### Month 1 验收（Week 4）

- [ ] 通过 Python 编程考核（3小时）
- [ ] 完成 CLI 工具项目
- [ ] 代码符合工程规范

### Month 4 验收（Week 16）

- [ ] RAG 系统可投递版本
- [ ] 召回率 > 90%、准确率 > 85%
- [ ] README/架构/指标齐全

### Month 6 验收（Week 24）

- [ ] Capstone 项目（RAG + Agent + Service）
- [ ] 一键部署（Docker Compose）
- [ ] 回归评测不退步

### Month 8 验收（Week 32）

- [ ] 简历终版 + 作品集首页
- [ ] 3套系统设计题完整讲解稿
- [ ] 开始投递简历

------

## 🔗 相关链接

- **GitHub 仓库**：https://github.com/guqingge97/AI-Learning-Journey
- **Claude Projects**：用于日常学习和进度追踪
- **学习路线详情**：[LEARNING_ROUTE_TEMPLATE.md](https://claude.ai/chat/docs/LEARNING_ROUTE_TEMPLATE.md)

------

## 📝 更新日志

- **2026-01-12**：更新为8个月路线 + Anchor 系统
- **2026-01-06**：完成 Week 1 学习
- **2026-01-05**：创建仓库，建立教学协议

------

## 💡 关键原则

1. **每天只学一个 One Thing**（2小时内可完成）
2. **每天必须有产出**（demo > snippet > notes）
3. **完成以 Git commit 为准**
4. **默认 Teaching Mode**（除非明确说"整理笔记"）
5. **稳扎稳打 > 快速过完**（学会 ≠ 看过）

------

**开始日期**：2026-01-06
 **当前进度**：M1-W2-D1
 **目标完成日期**：2026-09-06（预计）

**加油！从 Java 后端到 AI 应用开发，一步一个脚印！** 🚀
