# LEARNING_ROUTE_TEMPLATE.md（版本D｜36周全展开｜独立干活版）

> 目标：深圳中厂｜LLM 应用开发 / AI 后端（RAG/Agent/生产化）  
> 能力目标：**入职后能独立干活**（不只是拿 offer）  
> 不走：训练/算法研究岗  
> 时间：工作日 2h；周末 3h（每周约 16h）  
> 产出优先级：demo > snippet > notes；完成以 Git commit 为准  
> 调度方式：**确定性**（今日任务由 README 的 CurrentAnchor 精确映射到本模板条目）  
> 版本说明：v4.0 — 在 v3.0 基础上增加：AI 工程概念扫盲（M1-W4-WE2）、一键运行验证要求、Provider 抽象接口

---

## 0. 全局执行规则（AI 必须遵守）

1) 每天只学一个 **One Thing**（2小时内可完成）  
2) 每天必须有产出（demo/snippet/notes），可提交到 GitHub  
3) 默认 Teaching Mode：先问 2 检查题 → 我回答 → ≤10 要点 → ≤60 行示例 → ≤3 练习 → 收口  
4) 只有我说"进入 Notebook Mode"才输出入库笔记  
5) 不得跨语言栈：Month1–Month6 默认 Python；Month7 才引入 Java；Month8–9 面试冲刺可混合  
6) "工程化要素"（日志/超时/重试/观测）必须匹配阶段：Month1 轻量、Month5+ 才系统化  
7) 每周 WE2 为**弹性缓冲**：未卡住则用于盲点补充或提前预习；卡住则用于补课

---

## 1. Anchor 命名规则（README 用）

- 格式：`M{month}-W{week}-D{day}` 或 `M{month}-W{week}-WE{n}`
- 例：`M1-W2-D1` 表示 Month1 Week2 Day1
- 每周默认 5 个工作日（D1–D5）+ 周末（WE1 固定内容 / WE2 弹性缓冲）
- WE2 弹性用法：补课 > 盲点扩展 > 下周预习

---

## 2. 36 周总览

| Month | 周数 | 主题 | 核心产出 |
|-------|------|------|----------|
| M1 | W1–W4 | Python 工程基石 | python-app-template + CLI 工具 |
| M2 | W5–W8 | LLM API 工程化 | LLMClient + Tools + Prompt Kit + Service |
| M3 | W9–W13 | RAG 数据工程（5周） | RAG 端到端系统 + **开源项目阅读** |
| M4 | W14–W17 | RAG 评测闭环 | 评测体系 + **Badcase 排查 SOP** + 可投递作品集 |
| M5 | W18–W21 | Agent 开发 | Agent 核心 + 多步执行 + 作品集 |
| M6 | W22–W25 | 生产化 | 观测/缓存/成本 + **技术方案文档** + Capstone |
| M7 | W26–W30 | Java 混合 + 系统设计（5周） | Java 调用 + 系统设计 + 安全 |
| M8–9 | W31–W36 | 面试冲刺（6周） | 深挖 + 模拟面 + 投递闭环 |

---

## 3. v3.0 新增：独立干活三大能力

### 能力 1：Badcase 排查（M4-W15 落地）

**为什么重要**：线上出问题，老板不会告诉你是检索错了还是生成错了，你得自己查

**训练内容**：
- 拿到 badcase → 定位问题环节（检索/重排/生成/引用）
- 日志分析：看什么字段、怎么复现
- 形成《排查 SOP》文档

### 能力 2：阅读他人代码（M3-W13 落地）

**为什么重要**：入职后 90% 是接手现有系统，不是从零写

**训练内容**：
- 选一个中等复杂度开源 RAG 项目
- 画架构图 + 理清数据流
- 写阅读笔记：设计亮点 / 我会怎么改

### 能力 3：技术方案文档（M6-W25 落地）

**为什么重要**：做事之前要写方案、评审通过才能动手

**训练内容**：
- 背景与目标
- 方案设计（架构图 + 数据流）
- 技术选型对比（为什么选 A 不选 B）
- 风险与应对
- 排期与里程碑

---

## 3.5 v4.0 新增：AI 零基础过渡优化

### 优化 1：AI 工程概念扫盲（M1-W4-WE2 必做）

**为什么重要**：Month2 开始做 LLMClient/Tools/PromptKit，如果不懂 AI 核心概念，会变成机械封装

**必须理解的 8 个概念**：
1. **Token 与上下文窗口**：LLM 的输入输出单位、窗口限制、成本计算
2. **温度与随机性**：temperature 参数如何影响输出、何时用高/低温度
3. **结构化输出与失败模式**：JSON 输出、解析失败、容错策略
4. **Embedding 是什么**：文本 → 向量、语义表示、用途
5. **向量相似度**：余弦相似度、距离度量、检索原理
6. **RAG 与微调的区别**：什么时候用 RAG、什么时候用微调、各自优缺点
7. **幻觉与引用**：为什么 LLM 会"编"、如何用引用来约束
8. **评测为何必须做**：主观感觉不可靠、需要数据驱动改进

**产出**：notes/m1w4-ai-concepts.md（概念清单 + 自己的理解）

### 优化 2：一键运行验证（M1-W4-D5 硬门禁）

**为什么重要**：越早建立"可复现运行"习惯，后面 RAG/Agent 项目越不痛苦

**README 必须包含**：
1. 环境准备（3 步以内）
2. 安装依赖（1 条命令）
3. 运行验证（1 条命令 + 预期输出）

**验收标准**：陌生机器按 README 可在 3 分钟内跑通

### 优化 3：Provider 抽象接口（M2-W5-D1 预埋）

**为什么重要**：中国区环境 OpenAI 不稳定，必须预留可替换接口

**设计要求**：
- LLMClient 依赖抽象 Provider 接口，不直接依赖 OpenAI SDK
- 可以轻松切换：OpenAI / Azure / 本地 Ollama / 国产模型（如 DeepSeek、Qwen）
- 复用 Week2 学的"组合优于继承"思想

---

## 4. 盲点补充清单（穿插在 WE2 弹性时间）

| 阶段 | 盲点主题 | 建议补充时机 |
|------|----------|--------------|
| M1 | **🆕 AI 工程概念扫盲**（token/embedding/RAG/幻觉等 8 个核心概念） | **W4-WE2（必做）** |
| M2 | Embedding 模型选型（OpenAI/BGE/本地） | W7-WE2 或 W8-WE2 |
| M3 | 长上下文处理（超长文档切分策略） | W11-WE2 |
| M3 | 向量数据库原理（HNSW/IVF 索引） | W12-WE2 |
| M4 | LLM-as-Judge 评测方法 | W16-WE2 |
| M6 | 流式输出深入（SSE 断连/重连/背压） | W23-WE2 |
| M7 | 微调/LoRA 概念扫盲（不实操） | W29-WE2 |

---

# Month 1：Python 工程基石（Week1–Week4）

> 目标：能写"小而完整"的 Python 工程项目（结构清晰、可测试、可复现）

## Week1：Python 核心强化（推导式/生成器/装饰器/上下文/async）

**周 Deliverable**：10 个 kata + 1 个 async 最小 demo  
**Exit Criteria**：能解释关键边界与常见坑；demo 可跑

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M1-W1-D1 | 列表推导式（可读性与嵌套边界） | snippet | notes/m1w1d1.md | N/A |
| M1-W1-D2 | 推导式进阶（dict/set/条件过滤） | snippet | notes/m1w1d2.md | N/A |
| M1-W1-D3 | 生成器（yield/惰性求值/内存优势） | demo | projects/week1-generator-demo/ | python demo.py |
| M1-W1-D4 | 装饰器（计时/简单重试） | demo | projects/week1-decorator-demo/ | python demo.py |
| M1-W1-D5 | 上下文管理器（with/资源释放/__enter__/__exit__） | demo | projects/week1-context-demo/ | python demo.py |
| M1-W1-WE1 | async 最小 demo（asyncio.gather/并发请求） | demo | projects/week1-async-demo/ | python demo.py |
| M1-W1-WE2 | 【弹性】周复盘 或 补课 或 kata 强化 | notes | notes/m1w1-review.md | N/A |

---

## Week2：OOP + 类型系统（组合优于继承 / 可替换设计 / dataclass / pytest）

**周 Deliverable**：week2-skeleton（client/service/logger/config 模块化骨架）  
**Exit Criteria**：可替换 MockClient 不改 Service 代码；能讲清组合优于继承

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M1-W2-D1 | 组合优于继承：可替换 Client（Real/Mock）+ Service 依赖接口 | demo | projects/week2-skeleton/ | python demo.py |
| M1-W2-D2 | Type Hints + dataclass：为 client/service 定义签名与数据结构 | snippet | projects/week2-skeleton/ | python demo.py |
| M1-W2-D3 | 模块化：包结构（client/service/utils）+ __init__.py + 入口脚本 | demo | projects/week2-skeleton/ | python -m week2_skeleton |
| M1-W2-D4 | pytest 基础：≥3 测试（含 MockClient 注入测试） | demo | projects/week2-skeleton/ | pytest -q |
| M1-W2-D5 | logger：最小 logger 封装（统一格式/级别控制）供 service 调用 | snippet | projects/week2-skeleton/ | python demo.py |
| M1-W2-WE1 | config：env 文件 + 默认值 + 类型转换，驱动 client/service | snippet | projects/week2-skeleton/ | python demo.py |
| M1-W2-WE2 | 【弹性】整合 + README（可复现运行）或 补课 | demo | projects/week2-skeleton/ | python demo.py |

---

## Week3：工程模板化（src 布局 / lint / typing / CI）

**周 Deliverable**：python-app-template（可复用脚手架）  
**Exit Criteria**：新项目 3 分钟可启动；test/lint 一键通过

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M1-W3-D1 | 包管理与 src 布局（uv 或 poetry 二选一） | demo | projects/python-app-template/ | (按README) |
| M1-W3-D2 | pytest 进阶：fixtures + AAA 风格 + ≥3 测试 | demo | projects/python-app-template/ | pytest -q |
| M1-W3-D3 | ruff 格式化与静态检查（配置 + 自动修复） | snippet | projects/python-app-template/ | ruff check . |
| M1-W3-D4 | typing 检查（pyright 或 mypy 选一）+ 常见类型标注 | snippet | projects/python-app-template/ | (按README) |
| M1-W3-D5 | GitHub Actions：test + lint 最小流水线 | demo | projects/python-app-template/ | (CI 通过) |
| M1-W3-WE1 | 模板固化：README 规范 + 目录约定 + 快速启动脚本 | notes | notes/m1w3-template.md | N/A |
| M1-W3-WE2 | 【弹性】周复盘 或 补课 | notes | notes/m1w3-review.md | N/A |

---

## Week4：综合项目（小而完整的 CLI 工具）

**周 Deliverable**：cli-tool（可运行 CLI，带测试/日志/README）  
**Exit Criteria**：陌生机器按 README 可跑通；你能讲清架构取舍

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M1-W4-D1 | CLI 框架选型（argparse 或 typer）+ 命令结构设计 | demo | projects/cli-tool/ | python -m cli_tool --help |
| M1-W4-D2 | IO 处理（文件读写 或 HTTP 请求 选一）+ 错误处理 | demo | projects/cli-tool/ | (按README) |
| M1-W4-D3 | 并发优化（async 或 线程池 选一）最小提速演示 | demo | projects/cli-tool/ | (按README) |
| M1-W4-D4 | 测试覆盖：≥5 测试（正常/异常/边界场景） | demo | projects/cli-tool/ | pytest -q |
| M1-W4-D5 | 🆕 README 完善 + **一键运行验证**（陌生机器 3 步可跑）+ 1 分钟演示稿 | notes | notes/m1w4-cli.md | N/A |
| M1-W4-WE1 | Month 1 验收：复述核心概念 + 最小实现 + 踩坑复现 | notes | notes/m1w4-review.md | N/A |
| M1-W4-WE2 | 🆕 **AI 工程概念扫盲**（必做）：token/上下文窗口/温度/embedding/向量相似度/RAG vs 微调/幻觉/评测 | notes | notes/m1w4-ai-concepts.md | N/A |

---

# Month 2：LLM API 工程化（Week5–Week8）

> 目标：稳定调用模型、工具调用闭环、提示工程可回归、服务化可演示

## Week5：LLMClient 基础封装（timeout / retry / 结构化 / mock / 测试）

**周 Deliverable**：llm-client（Python LLMClient，可测试、可复现）  
**Exit Criteria**：能解释 token/成本/失败模式；可用 Mock 测试

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M2-W5-D1 | 🆕 设计 LLMClient 接口：ChatRequest/ChatResponse dataclass + **Provider 抽象**（可替换 OpenAI/本地/国产） | demo | projects/llm-client/ | python demo.py |
| M2-W5-D2 | 超时控制 + 指数退避重试（简化版）+ 错误分类（可重试/不可重试） | demo | projects/llm-client/ | python demo.py |
| M2-W5-D3 | 结构化输出：JSON schema 约束思路 + 解析容错（提取/修复） | demo | projects/llm-client/ | python demo.py |
| M2-W5-D4 | MockClient 实现 + 单元测试 ≥3（正常/超时/格式错误） | demo | projects/llm-client/ | pytest -q |
| M2-W5-D5 | README：成本估算方法 + 限制说明 + 最佳实践 | notes | notes/m2w5-llmclient.md | N/A |
| M2-W5-WE1 | 周复盘：失败模式清单整理 | notes | notes/m2w5-failures.md | N/A |
| M2-W5-WE2 | 【弹性】补课 或 Token 计算深入（tiktoken 实操） | snippet | notes/m2w5-token.md | N/A |

---

## Week6：Tool/Function Calling（工具注册 / 路由 / 校验 / 回退 / 测试）

**周 Deliverable**：tools-demo（tools registry + 端到端 demo）  
**Exit Criteria**：能做 schema、参数校验、错误回传；可 mock 测试

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M2-W6-D1 | 工具接口定义：Tool dataclass（name/description/schema/handler） | demo | projects/tools-demo/ | python demo.py |
| M2-W6-D2 | 工具路由：根据 LLM 返回的 tool_name 分发 + 参数校验（pydantic） | demo | projects/tools-demo/ | python demo.py |
| M2-W6-D3 | 多工具场景 + 失败回退策略（工具失败→告知 LLM→重选或放弃） | demo | projects/tools-demo/ | python demo.py |
| M2-W6-D4 | mock LLM + 工具调用测试 ≥3（正常调用/参数错误/工具执行失败） | demo | projects/tools-demo/ | pytest -q |
| M2-W6-D5 | 文档化：工具清单模板 + 边界说明 | notes | notes/m2w6-tools.md | N/A |
| M2-W6-WE1 | 整合：接入 Week5 的 LLMClient（import 复用） | demo | projects/tools-demo/ | python demo.py |
| M2-W6-WE2 | 【弹性】补课 或 工具设计模式扩展阅读 | notes | notes/m2w6-review.md | N/A |

---

## Week7：Prompt 工程化（模板 / 版本 / 回归）

**周 Deliverable**：prompt-kit（模板 + 版本管理 + 回归用例）  
**Exit Criteria**：能解释"为什么这样写 prompt"；能回归验证不退步

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M2-W7-D1 | prompt 模板结构：system/developer/user 三层 + 变量注入（Jinja2 或 f-string） | snippet | projects/prompt-kit/ | python demo.py |
| M2-W7-D2 | prompt 版本化：v1/v2 文件管理 + 变更记录（为什么改/改了什么/效果） | notes | notes/m2w7-prompt-version.md | N/A |
| M2-W7-D3 | 约束输出：格式要求（JSON/列表）+ 边界处理（超长/拒答策略） | demo | projects/prompt-kit/ | python demo.py |
| M2-W7-D4 | 回归用例集：≤10 个 case + 自动跑通脚本 + 结果对比 | demo | projects/prompt-kit/ | python run_regression.py |
| M2-W7-D5 | 总结：Prompt 工程最佳实践清单 | notes | notes/m2w7-summary.md | N/A |
| M2-W7-WE1 | 周复盘：失败案例分析 → 修复 → 入库 | demo | projects/prompt-kit/ | python demo.py |
| M2-W7-WE2 | 【弹性】**盲点补充：Embedding 模型选型**（OpenAI/BGE/本地对比） | notes | notes/m2w7-embedding.md | N/A |

---

## Week8：服务化（FastAPI + SSE/stream + 基础观测）

**周 Deliverable**：llm-service（/chat 流式接口可演示）  
**Exit Criteria**：日志字段规范、错误码清晰、最小观测可用

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M2-W8-D1 | FastAPI 最小服务：项目结构 + /health 端点 + 启动脚本 | demo | projects/llm-service/ | uvicorn app:app |
| M2-W8-D2 | SSE/stream 返回：StreamingResponse + 逐 token 输出 | demo | projects/llm-service/ | curl 测试 |
| M2-W8-D3 | 错误码设计 + 异常中间件（统一捕获 → 标准格式返回） | demo | projects/llm-service/ | uvicorn app:app |
| M2-W8-D4 | 日志字段：trace_id / 耗时 / 失败原因 / token 用量 | snippet | projects/llm-service/ | uvicorn app:app |
| M2-W8-D5 | README + 2 分钟演示脚本（curl 命令 + 预期输出） | notes | notes/m2w8-service.md | N/A |
| M2-W8-WE1 | Month 2 作品集整理：把 Week5–8 聚合到一个 README 索引 | notes | notes/m2-portfolio-index.md | N/A |
| M2-W8-WE2 | 【弹性】补课 或 流式输出进阶（客户端断连处理占位） | notes | notes/m2w8-review.md | N/A |

---

# Month 3：RAG 数据工程（Week9–Week13，5 周）

> 目标：可用的检索增强（摄取/切分/索引/检索/混合/重排），端到端可跑
> **v3.0 新增**：Week13 增加开源项目阅读，练习"读懂别人代码"的能力

## Week9：数据摄取与切分（ingest / chunk / metadata）

**周 Deliverable**：rag-ingest（ingest + chunk 对比 demo）  
**Exit Criteria**：能解释 chunk 策略对检索效果的影响；可复现

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M3-W9-D1 | 文档加载器：md 或 pdf 二选一（推荐先 md） | demo | projects/rag-ingest/ | python demo.py |
| M3-W9-D2 | chunk 策略基础：固定长度 + 重叠（overlap）+ 参数实验 | demo | projects/rag-ingest/ | python demo.py |
| M3-W9-D3 | 元数据设计：source/page/section/title 字段定义 | snippet | projects/rag-ingest/ | python demo.py |
| M3-W9-D4 | 清洗与去噪：最小规则（去空行/特殊字符/重复段落） | demo | projects/rag-ingest/ | python demo.py |
| M3-W9-D5 | 总结：chunk 策略 checklist + 参数默认值建议 | notes | notes/m3w9-chunk.md | N/A |
| M3-W9-WE1 | 周复盘：失败案例（过长 chunk 漏召回 / 过短 chunk 碎片化） | demo | projects/rag-ingest/ | python demo.py |
| M3-W9-WE2 | 【弹性】补课 或 PDF 解析深入（表格/图片处理占位） | notes | notes/m3w9-review.md | N/A |

---

## Week10：向量库与基础检索（topK / 过滤 / context 拼装）

**周 Deliverable**：rag-retrieval（vector store + retrieval demo）  
**Exit Criteria**：能解释召回率/精确度权衡；可跑

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M3-W10-D1 | 向量库选型：本地优先（Chroma 或 FAISS）+ 最小接入 | demo | projects/rag-retrieval/ | python demo.py |
| M3-W10-D2 | topK 检索 + metadata 过滤（按 source/section 筛选） | demo | projects/rag-retrieval/ | python demo.py |
| M3-W10-D3 | query 预处理：简单 rewrite 或 多查询展开 | demo | projects/rag-retrieval/ | python demo.py |
| M3-W10-D4 | context 构造：拼装多个 chunk + 去重 + 截断（不超 token 限制） | demo | projects/rag-retrieval/ | python demo.py |
| M3-W10-D5 | 总结：检索参数默认值表 + 调参建议 | notes | notes/m3w10-retrieval.md | N/A |
| M3-W10-WE1 | 周复盘：检索失败模式 5 条（语义漂移/同义词/否定句等） | notes | notes/m3w10-failures.md | N/A |
| M3-W10-WE2 | 【弹性】**盲点补充：向量数据库原理**（HNSW/IVF 索引简介） | notes | notes/m3w10-vector-db.md | N/A |

---

## Week11：混合检索（BM25 + 向量）

**周 Deliverable**：rag-hybrid（混合检索 demo）  
**Exit Criteria**：能解释 BM25 与向量检索的互补性；能调权重

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M3-W11-D1 | BM25 接入：rank_bm25 或 Elasticsearch 简化版 | demo | projects/rag-hybrid/ | python demo.py |
| M3-W11-D2 | 混合策略：BM25 + 向量结果合并（RRF 或 加权分数） | demo | projects/rag-hybrid/ | python demo.py |
| M3-W11-D3 | 权重调优：不同场景（精确匹配 vs 语义理解）的权重建议 | demo | projects/rag-hybrid/ | python demo.py |
| M3-W11-D4 | 对比实验：纯向量 vs 纯 BM25 vs 混合（同一 query 集） | demo | projects/rag-hybrid/ | python compare.py |
| M3-W11-D5 | 总结：混合检索 checklist + 何时有效/何时无效 | notes | notes/m3w11-hybrid.md | N/A |
| M3-W11-WE1 | 周复盘：边界 case 分析（专有名词/数字/代码片段） | notes | notes/m3w11-review.md | N/A |
| M3-W11-WE2 | 【弹性】**盲点补充：长上下文处理**（超长文档切分策略） | notes | notes/m3w11-long-context.md | N/A |

---

## Week12：重排（Rerank）

**周 Deliverable**：rag-rerank（rerank 接入 + 对比实验）  
**Exit Criteria**：能解释重排的价值与成本权衡

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M3-W12-D1 | Rerank 概念：为什么需要二次排序 + 常见 reranker 选型 | notes | notes/m3w12-rerank-intro.md | N/A |
| M3-W12-D2 | Rerank 接入：Cohere rerank 或 BGE-reranker 或 Cross-encoder | demo | projects/rag-rerank/ | python demo.py |
| M3-W12-D3 | 对比实验：无重排 vs 有重排（同一 query 集 + 人工标注 Top3） | demo | projects/rag-rerank/ | python compare.py |
| M3-W12-D4 | 成本分析：rerank 延迟 + 调用成本 + 何时值得用 | notes | notes/m3w12-rerank-cost.md | N/A |
| M3-W12-D5 | 总结：重排 checklist + 失败案例（重排反而变差的情况） | notes | notes/m3w12-rerank.md | N/A |
| M3-W12-WE1 | 整合：引用来源格式统一（chunk → 原文定位 → 引用输出） | snippet | projects/rag-rerank/ | python demo.py |
| M3-W12-WE2 | 【弹性】补课 或 其他 reranker 对比 | notes | notes/m3w12-review.md | N/A |

---

## Week13：RAG 端到端 + 🆕 开源项目阅读

**周 Deliverable**：rag-e2e + 开源项目阅读笔记  
**Exit Criteria**：自己的系统可跑；能画出别人项目的架构图

> **v3.0 新增**：本周增加"阅读开源 RAG 项目"任务，训练接手现有代码的能力

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M3-W13-D1 | 端到端 pipeline 串联：query → retrieval → rerank → LLM → response | demo | projects/rag-e2e/ | python demo.py |
| M3-W13-D2 | prompt 组装：system prompt + context 注入 + 引用指令 + 拒答占位 | demo | projects/rag-e2e/ | python demo.py |
| M3-W13-D3 | 简单缓存：query → result 缓存（避免重复检索，降低成本） | snippet | projects/rag-e2e/ | python demo.py |
| M3-W13-D4 | 服务化：FastAPI 最小接口（/ask 端点） | demo | projects/rag-e2e/ | uvicorn app:app |
| M3-W13-D5 | 🆕 **开源项目阅读（上）**：选一个 RAG 项目（推荐 QAnything/RAGFlow 的核心模块），clone 下来跑通 | notes | notes/m3w13-opensource-setup.md | N/A |
| M3-W13-WE1 | 🆕 **开源项目阅读（下）**：画架构图 + 数据流 + 写阅读笔记（亮点/槽点/我会怎么改） | notes | notes/m3w13-opensource-analysis.md | N/A |
| M3-W13-WE2 | 【弹性】Month 3 作品集整理：RAG 一页纸 | notes | notes/m3-rag-onepager.md | N/A |

---

# Month 4：RAG 评测闭环（Week14–Week17）

> 目标：用数据说话（dataset / metrics / baseline → 改进 → 回归门禁 → 可投递版本）
> **v3.0 新增**：Week15 增加 Badcase 排查实操，形成《排查 SOP》

## Week14：评测数据集与指标

**周 Deliverable**：rag-eval（小数据集 ≤20 + eval 脚本雏形）  
**Exit Criteria**：能跑出评测报告（json + markdown）

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M4-W14-D1 | 构造 QA 数据集：≤20 条（query + expected_answer + source_doc） | notes | data/eval-dataset.json | N/A |
| M4-W14-D2 | 指标定义：准确率 / 引用正确率 / 拒答率 / 答案一致性 | notes | notes/m4w14-metrics.md | N/A |
| M4-W14-D3 | eval 脚本雏形：跑通单条 → 批量 → 输出结果 | demo | projects/rag-eval/ | python eval.py |
| M4-W14-D4 | 报告输出：json 原始数据 + markdown 可读报告 | demo | projects/rag-eval/ | python eval.py |
| M4-W14-D5 | 总结：评测流程图 + 指标计算公式 | notes | notes/m4w14-summary.md | N/A |
| M4-W14-WE1 | 周复盘：坏 case 分析 3 条（为什么错 + 如何改） | notes | notes/m4w14-badcases.md | N/A |
| M4-W14-WE2 | 【弹性】补课 或 数据集扩充 | notes | notes/m4w14-review.md | N/A |

---

## Week15：Baseline 固化 + 改进 + 🆕 Badcase 排查实操

**周 Deliverable**：baseline + 改进对比报告 + **《Badcase 排查 SOP》**  
**Exit Criteria**：能解释为何提升；能拿到 badcase 独立定位问题

> **v3.0 新增**：本周增加 Badcase 排查实操，训练线上问题排查能力

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M4-W15-D1 | baseline 固化：锁定参数版本（chunk_size/topK/model）+ 跑基线 | demo | projects/rag-eval/ | python eval.py |
| M4-W15-D2 | 改进 1：chunk 策略调优（对比 2-3 组参数） | demo | projects/rag-eval/ | python eval.py |
| M4-W15-D3 | 改进 2：topK / 过滤 / rerank 策略调优 | demo | projects/rag-eval/ | python eval.py |
| M4-W15-D4 | 🆕 **Badcase 排查实操（上）**：我给你 5 个 badcase，你来定位是检索问题还是生成问题 | demo | projects/rag-eval/badcase-analysis/ | python analyze.py |
| M4-W15-D5 | 🆕 **Badcase 排查实操（下）**：形成《排查 SOP》文档（拿到 badcase → 看什么日志 → 如何复现 → 如何修复） | notes | notes/m4w15-troubleshoot-sop.md | N/A |
| M4-W15-WE1 | 周复盘：提升归因模板（改了什么 → 指标变化 → 原因分析） | notes | notes/m4w15-summary.md | N/A |
| M4-W15-WE2 | 【弹性】**盲点补充：LLM-as-Judge 评测方法** | notes | notes/m4w15-llm-judge.md | N/A |

---

## Week16：回归测试与质量门禁（不退步）

**周 Deliverable**：回归集 + 门禁规则 + 自动对比报告  
**Exit Criteria**：一键跑评测，输出"是否通过门禁"

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M4-W16-D1 | 回归用例集：从坏 case 中选 ≤10 条必须通过的 case | notes | data/regression-set.json | N/A |
| M4-W16-D2 | 失败分析模板：分类（检索失败/生成失败/引用错误）+ 根因 + 修复建议 | notes | notes/m4w16-failure-template.md | N/A |
| M4-W16-D3 | 门禁规则：不退步阈值（如：准确率不降超过 5%） | demo | projects/rag-eval/ | python eval.py --gate |
| M4-W16-D4 | 自动对比报告：新版本 vs baseline diff 输出 | demo | projects/rag-eval/ | python eval.py --diff |
| M4-W16-D5 | 总结：门禁说明文档 + CI 集成占位 | notes | notes/m4w16-summary.md | N/A |
| M4-W16-WE1 | 周复盘：门禁误报/漏报分析 | notes | notes/m4w16-review.md | N/A |
| M4-W16-WE2 | 【弹性】评测速度优化（并行/缓存） | snippet | projects/rag-eval/ | python eval.py |

---

## Week17：RAG 作品集版本（可投递）

**周 Deliverable**：rag-portfolio（README / 架构图 / 指标 / 部署）  
**Exit Criteria**：别人按 README 可跑；你能 2 分钟讲清楚

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M4-W17-D1 | 代码整理：目录规范化 + 删除调试代码 + 统一命名 | demo | projects/rag-portfolio/ | (按README) |
| M4-W17-D2 | README 完善：架构图（ASCII）+ 技术选型理由 + 指标展示 | notes | projects/rag-portfolio/README.md | N/A |
| M4-W17-D3 | 演示脚本 + 录屏提纲（2 分钟能讲什么） | notes | notes/m4w17-demo.md | N/A |
| M4-W17-D4 | Docker 最小部署：docker-compose.yml + 一键启动 | demo | projects/rag-portfolio/ | docker compose up |
| M4-W17-D5 | 周总结：RAG 一页纸更新（加入评测指标） | notes | notes/m4w17-summary.md | N/A |
| M4-W17-WE1 | Month 4 验收：完整跑一遍 demo + 回答 3 个面试问题 | notes | notes/m4w17-review.md | N/A |
| M4-W17-WE2 | 【弹性】作品集聚合 README 更新 | notes | README.md | N/A |

---

# Month 5：Agent 开发（Week18–Week21）

> 目标：可控 Agent（工具/状态/回退/多步），失败模式可解释

## Week18：工具编排与状态（Agent Core）

**周 Deliverable**：agent-core（tools registry + state + fallback）  
**Exit Criteria**：mock 可测；失败可回退；状态可追踪

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M5-W18-D1 | 工具注册中心：复用 Week6 的 Tool 定义 + 统一 registry | demo | projects/agent-core/ | python demo.py |
| M5-W18-D2 | 状态结构定义：AgentState dataclass（memory/context/history） | demo | projects/agent-core/ | python demo.py |
| M5-W18-D3 | 回退策略：工具失败 → 降级方案（重试/跳过/人工介入标记） | demo | projects/agent-core/ | python demo.py |
| M5-W18-D4 | 测试：mock 工具 + mock LLM，≥3 测试场景 | demo | projects/agent-core/ | pytest -q |
| M5-W18-D5 | 总结：Agent 失败模式清单（工具失败/LLM 幻觉/状态丢失等） | notes | notes/m5w18-summary.md | N/A |
| M5-W18-WE1 | 周复盘：错误分类与回退一致性检查 | snippet | projects/agent-core/ | python demo.py |
| M5-W18-WE2 | 【弹性】补课 或 Agent 框架调研（LangGraph/CrewAI 简读） | notes | notes/m5w18-review.md | N/A |

---

## Week19：规划与多步执行（Planner / Runner）

**周 Deliverable**：agent-plan（planner + runner 可演示）  
**Exit Criteria**：能中断/恢复（占位）；能统计成功率

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M5-W19-D1 | 简单 Planner：LLM 生成步骤列表（JSON 格式） | demo | projects/agent-plan/ | python demo.py |
| M5-W19-D2 | Step Runner：逐步执行 + 日志记录（每步输入/输出/耗时） | demo | projects/agent-plan/ | python demo.py |
| M5-W19-D3 | 中断/恢复：状态持久化占位（保存到 JSON 文件） | snippet | projects/agent-plan/ | python demo.py |
| M5-W19-D4 | 执行统计：成功率 / 失败分类 / 平均步骤数 | demo | projects/agent-plan/ | python demo.py |
| M5-W19-D5 | 总结：多步执行失败模式（计划错误/执行错误/状态不一致） | notes | notes/m5w19-summary.md | N/A |
| M5-W19-WE1 | 周复盘：工具参数校验强化 | demo | projects/agent-plan/ | python demo.py |
| M5-W19-WE2 | 【弹性】补课 或 ReAct 模式实现 | notes | notes/m5w19-review.md | N/A |

---

## Week20：多 Agent 协作（简化版）

**周 Deliverable**：multi-agent（planner / executor / reviewer 三角色）  
**Exit Criteria**：handoff schema 明确；冲突处理可解释

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M5-W20-D1 | 角色拆分：Planner / Executor / Reviewer 职责定义 | demo | projects/multi-agent/ | python demo.py |
| M5-W20-D2 | 协作协议：handoff schema（谁传什么给谁 + 格式约定） | snippet | projects/multi-agent/ | python demo.py |
| M5-W20-D3 | 冲突处理：Reviewer 否决 → Planner 重规划 → 最大轮次限制 | demo | projects/multi-agent/ | python demo.py |
| M5-W20-D4 | 回归用例：≤10 个场景（简单任务/复杂任务/失败恢复） | demo | projects/multi-agent/ | pytest -q |
| M5-W20-D5 | 总结：协作失败模式（角色越界/信息丢失/死循环） | notes | notes/m5w20-summary.md | N/A |
| M5-W20-WE1 | 周复盘：协议与实现一致性检查 | snippet | projects/multi-agent/ | python demo.py |
| M5-W20-WE2 | 【弹性】补课 或 Agent 监控思路 | notes | notes/m5w20-review.md | N/A |

---

## Week21：Agent 作品集版本

**周 Deliverable**：agent-portfolio（可投递）  
**Exit Criteria**：2 分钟演示；README / 部署 / 限制说明齐全

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M5-W21-D1 | 整理成可演示项目：合并 agent-core + agent-plan（或选一个） | demo | projects/agent-portfolio/ | (按README) |
| M5-W21-D2 | README：能力边界 + 失败模式 + 使用限制 | notes | projects/agent-portfolio/README.md | N/A |
| M5-W21-D3 | Docker 最小部署 | demo | projects/agent-portfolio/ | docker compose up |
| M5-W21-D4 | 测试与门禁：pytest + 基线成功率 | demo | projects/agent-portfolio/ | pytest -q |
| M5-W21-D5 | 周总结：Agent 一页纸 | notes | notes/m5w21-summary.md | N/A |
| M5-W21-WE1 | Month 5 验收：demo 演示 + 回答 3 个面试问题 | notes | notes/m5w21-review.md | N/A |
| M5-W21-WE2 | 【弹性】作品集聚合 README 更新 | notes | README.md | N/A |

---

# Month 6：生产化（Week22–Week25）

> 目标：服务化、观测、成本、缓存、限流、部署、回归评测
> **v3.0 新增**：Week25 增加技术方案文档撰写，训练"写方案"能力

## Week22：服务化与观测（基础）

**周 Deliverable**：prod-service（FastAPI + 基础观测）  
**Exit Criteria**：日志字段规范；错误码清晰；最小指标可用

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M6-W22-D1 | FastAPI + SSE 稳定版：整合之前的 llm-service | demo | projects/prod-service/ | uvicorn app:app |
| M6-W22-D2 | 日志字段规范：trace_id / request_id / 耗时 / 错误码 / token | snippet | projects/prod-service/ | uvicorn app:app |
| M6-W22-D3 | 指标采集（简化）：请求计数 / 延迟分布 / 错误率（print 或文件） | snippet | projects/prod-service/ | uvicorn app:app |
| M6-W22-D4 | 限流/降级（简化）：令牌桶或固定窗口 + 降级响应 | demo | projects/prod-service/ | uvicorn app:app |
| M6-W22-D5 | 总结：观测 checklist（日志该有什么/指标该有什么） | notes | notes/m6w22-summary.md | N/A |
| M6-W22-WE1 | 周复盘：观测字段一致性检查 | snippet | projects/prod-service/ | uvicorn app:app |
| M6-W22-WE2 | 【弹性】补课 或 Prometheus/Grafana 概念扫盲 | notes | notes/m6w22-review.md | N/A |

---

## Week23：缓存与成本控制

**周 Deliverable**：成本核算文档 + 缓存策略落地  
**Exit Criteria**：能解释成本计算；能说清缓存策略

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M6-W23-D1 | 缓存策略：prompt 缓存 / result 缓存 / embedding 缓存 | demo | projects/prod-service/ | uvicorn app:app |
| M6-W23-D2 | token 统计与成本核算：输入 token + 输出 token + 单价 → 成本 | snippet | projects/prod-service/ | python cost.py |
| M6-W23-D3 | 失败重试与幂等：重试不重复计费 + 幂等 key 设计 | demo | projects/prod-service/ | uvicorn app:app |
| M6-W23-D4 | 配置化开关：feature flag 简化版（环境变量控制功能开关） | snippet | projects/prod-service/ | uvicorn app:app |
| M6-W23-D5 | 总结：成本优化清单（10 条可落地建议） | notes | notes/m6w23-summary.md | N/A |
| M6-W23-WE1 | 周复盘：缓存失效策略（TTL / 主动失效 / 版本号） | notes | notes/m6w23-cache.md | N/A |
| M6-W23-WE2 | 【弹性】**盲点补充：流式输出深入**（SSE 断连/重连/背压） | notes | notes/m6w23-sse.md | N/A |

---

## Week24：网关与本地推理（可选但建议了解）

**周 Deliverable**：llm-gateway（统一 client + 路由占位）  
**Exit Criteria**：能讲清网关价值；能跑最小基准

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M6-W24-D1 | 本地推理概念：Ollama / vLLM / llama.cpp 选型概览 | notes | notes/m6w24-local-llm.md | N/A |
| M6-W24-D2 | 网关封装：统一 LLMClient 接口（屏蔽后端差异） | demo | projects/llm-gateway/ | python demo.py |
| M6-W24-D3 | 路由策略：按模型名路由 + 负载均衡占位 | demo | projects/llm-gateway/ | python demo.py |
| M6-W24-D4 | 基准测试：QPS / 延迟测量脚本 | demo | projects/llm-gateway/ | python bench.py |
| M6-W24-D5 | 总结：网关设计要点 + 何时需要网关 | notes | notes/m6w24-summary.md | N/A |
| M6-W24-WE1 | 周复盘：失败回退策略（主模型挂 → 备用模型） | snippet | projects/llm-gateway/ | python demo.py |
| M6-W24-WE2 | 【弹性】补课 或 本地模型实操（Ollama 跑一个小模型） | notes | notes/m6w24-review.md | N/A |

---

## Week25：Capstone 整合 + 🆕 技术方案文档

**周 Deliverable**：capstone + **正式技术方案文档**  
**Exit Criteria**：一键部署；方案文档可用于评审

> **v3.0 新增**：本周增加技术方案文档撰写，训练"写方案给别人评审"的能力

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M6-W25-D1 | 整合：RAG + Agent + Service 端到端串联 | demo | projects/capstone/ | (按README) |
| M6-W25-D2 | 一键部署：docker-compose.yml（所有服务） | demo | projects/capstone/ | docker compose up |
| M6-W25-D3 | 回归评测：集成之前的 eval 脚本，确保不退步 | demo | projects/capstone/ | python eval.py |
| M6-W25-D4 | 🆕 **技术方案文档（上）**：背景/目标/方案设计/架构图 | notes | docs/capstone-tech-proposal.md | N/A |
| M6-W25-D5 | 🆕 **技术方案文档（下）**：技术选型对比/风险与应对/排期里程碑 | notes | docs/capstone-tech-proposal.md | N/A |
| M6-W25-WE1 | Month 6 验收：完整 demo + 方案文档自审 + 回答 5 个面试问题 | notes | notes/m6w25-review.md | N/A |
| M6-W25-WE2 | 【弹性】作品集首页聚合 + 下月预习 | notes | README.md | N/A |

---

# Month 7：Java 混合落地 + 系统设计（Week26–Week30，5 周）

> 目标：用 Java 接住工程化叙事，形成中厂"后端 + AI 应用"可投递故事线

## Week26：Java 调用 LLM/RAG 服务（HTTP / SSE / 错误码 / trace）

**周 Deliverable**：java-llm-client（可演示）  
**Exit Criteria**：能讲清重试/错误码/trace_id 打通

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M7-W26-D1 | Java HTTP Client 封装：调用 Python 服务的 /chat 接口 | demo | projects/java-llm-client/ | (按README) |
| M7-W26-D2 | 统一错误码：Java 侧错误码定义 + 与 Python 服务对齐 | demo | projects/java-llm-client/ | (按README) |
| M7-W26-D3 | 重试策略：指数退避 + 可重试错误判断 | demo | projects/java-llm-client/ | (按README) |
| M7-W26-D4 | SSE/流式消费：Java 客户端消费流式响应 | demo | projects/java-llm-client/ | (按README) |
| M7-W26-D5 | trace_id 贯通：请求头传递 → 日志打印 → 链路追踪 | snippet | projects/java-llm-client/ | (按README) |
| M7-W26-WE1 | 周复盘：Java 侧工程化要点总结 | notes | notes/m7w26-summary.md | N/A |
| M7-W26-WE2 | 【弹性】异常分类与告警占位 | notes | notes/m7w26-alert.md | N/A |

---

## Week27：系统设计题（RAG 服务架构）

**周 Deliverable**：RAG 架构题 1 套完整讲解稿（含图）  
**Exit Criteria**：能 10 分钟讲清组件/数据流/失败模式/扩展点

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M7-W27-D1 | 架构图：组件拆分 + 数据流（ASCII 图） | notes | notes/m7w27-arch.md | N/A |
| M7-W27-D2 | 存储与索引策略：文档更新 / 索引重建 / 一致性保证 | notes | notes/m7w27-storage.md | N/A |
| M7-W27-D3 | 缓存设计：缓存什么 / 失效策略 / 一致性 | notes | notes/m7w27-cache.md | N/A |
| M7-W27-D4 | 容灾与降级：无检索降级 / 低配模型兜底 / 熔断 | notes | notes/m7w27-fallback.md | N/A |
| M7-W27-D5 | 面试回答模板：开场 → 需求澄清 → 架构 → 深挖 → 总结 | notes | notes/m7w27-answer.md | N/A |
| M7-W27-WE1 | 周复盘：模拟讲一遍（计时 10 分钟） | notes | notes/m7w27-review.md | N/A |
| M7-W27-WE2 | 【弹性】容量估算练习（QPS / 存储 / 成本） | notes | notes/m7w27-capacity.md | N/A |

---

## Week28：系统设计题（Agent 平台架构）

**周 Deliverable**：Agent 架构题 1 套完整讲解稿（含图）  
**Exit Criteria**：能 10 分钟讲清工具管理/状态持久化/可观测性

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M7-W28-D1 | 架构图：Agent 平台组件（调度器/执行器/工具库/状态存储） | notes | notes/m7w28-arch.md | N/A |
| M7-W28-D2 | 工具管理：注册 / 版本 / 权限 / 沙箱 | notes | notes/m7w28-tools.md | N/A |
| M7-W28-D3 | 状态持久化：任务状态 / 断点续传 / 幂等执行 | notes | notes/m7w28-state.md | N/A |
| M7-W28-D4 | 可观测性：日志 / 指标 / 追踪 / 告警 | notes | notes/m7w28-observability.md | N/A |
| M7-W28-D5 | 面试回答模板：Agent 平台版本 | notes | notes/m7w28-answer.md | N/A |
| M7-W28-WE1 | 周复盘：模拟讲一遍（计时 10 分钟） | notes | notes/m7w28-review.md | N/A |
| M7-W28-WE2 | 【弹性】与 RAG 架构对比（共性/差异） | notes | notes/m7w28-compare.md | N/A |

---

## Week29：Agent 服务化与安全（提示注入 / 权限 / 审计）

**周 Deliverable**：安全 demo + 讲解稿  
**Exit Criteria**：能讲清风险与防护策略

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M7-W29-D1 | 工具权限模型：允许/拒绝/审批 + 最小权限原则 | notes | notes/m7w29-permission.md | N/A |
| M7-W29-D2 | 异步执行：任务队列 + 状态轮询 + 超时处理 | notes | notes/m7w29-async.md | N/A |
| M7-W29-D3 | 审计日志：操作记录 / 敏感字段脱敏 / 留存策略 | notes | notes/m7w29-audit.md | N/A |
| M7-W29-D4 | 提示注入攻防：攻击示例 + 防护措施（输入过滤/输出校验） | demo | projects/security-demo/ | python demo.py |
| M7-W29-D5 | 总结：安全清单（10 条必检项） | notes | notes/m7w29-summary.md | N/A |
| M7-W29-WE1 | 周复盘：红队用例 ≤10（模拟攻击场景） | notes | notes/m7w29-redteam.md | N/A |
| M7-W29-WE2 | 【弹性】**盲点补充：微调/LoRA 概念扫盲**（不实操） | notes | notes/m7w29-finetune.md | N/A |

---

## Week30：简历叙事与作品集打磨

**周 Deliverable**：项目一页纸 + 指标叙事 + 面试题库  
**Exit Criteria**：可投递、可讲述、可演示

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M7-W30-D1 | 项目一页纸（RAG）：背景 / 方案 / 指标 / 亮点 | notes | notes/m7w30-rag-onepager.md | N/A |
| M7-W30-D2 | 项目一页纸（Agent）：背景 / 方案 / 指标 / 亮点 | notes | notes/m7w30-agent-onepager.md | N/A |
| M7-W30-D3 | 指标叙事：baseline → 改进 → 提升百分比（数据驱动） | notes | notes/m7w30-metrics.md | N/A |
| M7-W30-D4 | 常见面试题库：工程题 / 系统设计题 / LLM 原理题（各 10 道） | notes | notes/m7w30-interview.md | N/A |
| M7-W30-D5 | 自我介绍 + 反问清单（终版草稿） | notes | notes/m7w30-pitch.md | N/A |
| M7-W30-WE1 | Month 7 验收：模拟自我介绍 + 项目讲解 | notes | notes/m7w30-review.md | N/A |
| M7-W30-WE2 | 【弹性】投递准备（岗位 JD 匹配清单） | notes | notes/m7w30-apply.md | N/A |

---

# Month 8–9：面试冲刺（Week31–Week36，6 周）

> 目标：稳定输出、系统设计答题、模拟面、投递闭环

## Week31：RAG 深挖（失败模式 / 重排 / 评测讲解）

**周 Deliverable**：RAG 讲解稿 + 2 分钟演示脚本  
**Exit Criteria**：能把失败模式讲清并给方案

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M8-W31-D1 | 检索失败模式清单：≥10 条（语义漂移/同义词/否定/多跳等） | notes | notes/m8w31-failures.md | N/A |
| M8-W31-D2 | 重排/混检讲解稿：原理 + 实现 + 效果 + 局限 | notes | notes/m8w31-rerank.md | N/A |
| M8-W31-D3 | 评测体系讲解稿：指标 / 数据集 / 门禁 / 回归 | notes | notes/m8w31-eval.md | N/A |
| M8-W31-D4 | 2 分钟演示脚本（RAG）：讲什么 / 演示什么 / 强调什么 | notes | notes/m8w31-demo.md | N/A |
| M8-W31-D5 | RAG 常问快答：15 个高频问题 + 简洁答案 | notes | notes/m8w31-qa.md | N/A |
| M8-W31-WE1 | 周复盘：最弱点识别 + 专项强化 | notes | notes/m8w31-review.md | N/A |
| M8-W31-WE2 | 【弹性】补洞（弱点专项练习） | notes | notes/m8w31-fix.md | N/A |

---

## Week32：Agent 深挖（工具 / 状态 / 回退 / 测试）

**周 Deliverable**：Agent 讲解稿 + 回归策略  
**Exit Criteria**：能讲清可控性与失败处理

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M8-W32-D1 | Agent 失败模式与回退讲解稿 | notes | notes/m8w32-fallback.md | N/A |
| M8-W32-D2 | 工具设计与权限讲解稿 | notes | notes/m8w32-tools.md | N/A |
| M8-W32-D3 | 状态机与可恢复性讲解稿 | notes | notes/m8w32-state.md | N/A |
| M8-W32-D4 | 测试策略讲解稿：mock / 回归 / 边界 | notes | notes/m8w32-tests.md | N/A |
| M8-W32-D5 | Agent 常问快答：15 个高频问题 + 简洁答案 | notes | notes/m8w32-qa.md | N/A |
| M8-W32-WE1 | 周复盘：最弱点识别 + 专项强化 | notes | notes/m8w32-review.md | N/A |
| M8-W32-WE2 | 【弹性】补洞（弱点专项练习） | notes | notes/m8w32-fix.md | N/A |

---

## Week33：系统设计模拟面（第一轮，2 套题）

**周 Deliverable**：2 套系统设计完整稿 + 模拟录音/笔记  
**Exit Criteria**：每套 10–15 分钟可讲清

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M8-W33-D1 | 题 1 模拟：RAG 服务设计（计时 15 分钟，自己讲 + 录音） | notes | notes/m8w33-sd1.md | N/A |
| M8-W33-D2 | 题 1 复盘：哪里卡顿 / 哪里漏讲 / 如何改进 | notes | notes/m8w33-sd1-retro.md | N/A |
| M8-W33-D3 | 题 2 模拟：Agent 平台设计（计时 15 分钟） | notes | notes/m8w33-sd2.md | N/A |
| M8-W33-D4 | 题 2 复盘 | notes | notes/m8w33-sd2-retro.md | N/A |
| M8-W33-D5 | 总结：系统设计答题框架优化 | notes | notes/m8w33-framework.md | N/A |
| M8-W33-WE1 | 周复盘：通用改进点（开场/深挖/收尾） | notes | notes/m8w33-review.md | N/A |
| M8-W33-WE2 | 【弹性】额外模拟或补洞 | notes | notes/m8w33-extra.md | N/A |

---

## Week34：系统设计模拟面（第二轮，综合题）

**周 Deliverable**：1 套综合题 + 反问清单终版  
**Exit Criteria**：能应对"成本/观测/稳定性"追问

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M8-W34-D1 | 综合题模拟：成本优化 + 观测体系 + 稳定性保障 | notes | notes/m8w34-sd3.md | N/A |
| M8-W34-D2 | 综合题复盘 | notes | notes/m8w34-sd3-retro.md | N/A |
| M8-W34-D3 | 追问应对：常见追问 Top10 + 应对策略 | notes | notes/m8w34-followup.md | N/A |
| M8-W34-D4 | 反问清单终版：问什么 / 为什么问 / 期望答案 | notes | notes/m8w34-questions.md | N/A |
| M8-W34-D5 | 自我介绍终版（1 分钟 + 3 分钟两个版本） | notes | notes/m8w34-pitch.md | N/A |
| M8-W34-WE1 | 周复盘：模拟面整体复盘 | notes | notes/m8w34-review.md | N/A |
| M8-W34-WE2 | 【弹性】最弱题重练 | notes | notes/m8w34-fix.md | N/A |

---

## Week35：简历终版 + 作品集打磨

**周 Deliverable**：简历终版 + 作品集首页 + 投递策略  
**Exit Criteria**：可投递、可追踪

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M8-W35-D1 | 简历终版：项目描述优化 + 指标量化 + 关键词对齐 JD | notes | notes/m8w35-resume.md | N/A |
| M8-W35-D2 | 作品集首页：README 聚合 + 项目导航 + 快速上手 | notes | projects/README.md | N/A |
| M8-W35-D3 | 投递策略：目标公司列表 + JD 匹配度评分 + 优先级 | notes | notes/m8w35-apply.md | N/A |
| M8-W35-D4 | 投递渠道：Boss / 拉勾 / 内推 / 猎头（各渠道特点） | notes | notes/m8w35-channels.md | N/A |
| M8-W35-D5 | 投递节奏：每周投多少 / 如何跟进 / 如何记录 | notes | notes/m8w35-rhythm.md | N/A |
| M8-W35-WE1 | 周复盘：简历 + 作品集自查 | notes | notes/m8w35-review.md | N/A |
| M8-W35-WE2 | 【弹性】开始投递 或 继续打磨 | notes | notes/m8w35-action.md | N/A |

---

## Week36：收官 + 持续迭代准备

**周 Deliverable**：完整复盘 + 下一阶段规划  
**Exit Criteria**：36 周学习闭环；有明确的后续方向

| Anchor | 主题 | 产出类型 | 产出路径 | 验证命令 |
|--------|------|----------|----------|----------|
| M9-W36-D1 | 36 周学习复盘：学了什么 / 做了什么 / 还差什么 | notes | notes/m9w36-retrospective.md | N/A |
| M9-W36-D2 | 作品集终审：所有项目可跑 / README 完整 / 演示流畅 | notes | notes/m9w36-portfolio-check.md | N/A |
| M9-W36-D3 | 面试复盘模板：每场面试后记录什么 / 如何改进 | notes | notes/m9w36-interview-retro.md | N/A |
| M9-W36-D4 | 下一阶段规划：入职后学什么 / 1 年后目标 / 长期方向 | notes | notes/m9w36-next.md | N/A |
| M9-W36-D5 | 感谢与告别：给自己的一封信（可选） | notes | notes/m9w36-letter.md | N/A |
| M9-W36-WE1 | 最终验收：作品集走查 + 模拟面最后一轮 | notes | notes/m9w36-final.md | N/A |
| M9-W36-WE2 | 【弹性】持续投递 + 面试 + 迭代 | notes | notes/m9w36-ongoing.md | N/A |

---

# 附录 A：目录结构规范

```
AI-Learning-Journey/
├── README.md                    # 作品集首页（聚合所有项目）
├── LEARNING_ROUTE.md            # 本文件
├── data/                        # 评测数据集
│   ├── eval-dataset.json
│   └── regression-set.json
├── docs/                        # 正式文档
│   ├── capstone-tech-proposal.md   # 🆕 技术方案文档
│   └── troubleshoot-sop.md         # 🆕 排查 SOP
├── notes/                       # 学习笔记（按 Anchor 编号）
│   ├── m1w1d1.md
│   ├── m1w1d2.md
│   ├── m3w13-opensource-analysis.md  # 🆕 开源项目阅读笔记
│   ├── m4w15-troubleshoot-sop.md     # 🆕 排查 SOP
│   └── ...
├── projects/                    # 项目代码
│   ├── week1-generator-demo/
│   ├── week1-decorator-demo/
│   ├── week1-context-demo/
│   ├── week1-async-demo/
│   ├── week2-skeleton/
│   ├── python-app-template/
│   ├── cli-tool/
│   ├── llm-client/
│   ├── tools-demo/
│   ├── prompt-kit/
│   ├── llm-service/
│   ├── rag-ingest/
│   ├── rag-retrieval/
│   ├── rag-hybrid/
│   ├── rag-rerank/
│   ├── rag-e2e/
│   ├── rag-eval/
│   │   └── badcase-analysis/       # 🆕 Badcase 分析
│   ├── rag-portfolio/
│   ├── agent-core/
│   ├── agent-plan/
│   ├── multi-agent/
│   ├── agent-portfolio/
│   ├── prod-service/
│   ├── llm-gateway/
│   ├── capstone/
│   ├── java-llm-client/
│   └── security-demo/
└── teaching-docs/               # 教学文档（从 Project 同步）
    ├── 01-教学协议.md
    ├── 02-学员档案.md
    └── ...
```

---

# 附录 B：每日工作流

```
1. 打开对话，输入今日 Anchor（如：M1-W2-D1）
2. Claude 进入 Teaching Mode，开始教学
3. 完成教学 + 练习 + 产出
4. 提交到 GitHub：
   git add .
   git commit -m "M1-W2-D1: 组合优于继承"
   git push
5. 更新 README 的 CurrentAnchor
```

---

# 附录 C：关键里程碑

| 周数 | 里程碑 | 可交付物 |
|------|--------|----------|
| W4 | Month 1 完成 | python-app-template + cli-tool |
| W8 | Month 2 完成 | LLMClient + Tools + Service |
| W13 | Month 3 完成 | RAG 端到端 + **开源项目阅读笔记** |
| W17 | Month 4 完成 | RAG 作品集 + **《排查 SOP》** |
| W21 | Month 5 完成 | Agent 作品集 |
| W25 | Month 6 完成 | Capstone + **技术方案文档** |
| W30 | Month 7 完成 | 系统设计 + 简历叙事 |
| W36 | 全部完成 | 可投递 + 可面试 + **能独立干活** |

---

# 附录 D：v3.0 新增能力对照表

| 能力 | 落地位置 | 产出 |
|------|----------|------|
| Badcase 排查 | M4-W15-D4/D5 | 《排查 SOP》+ 5 个实操案例 |
| 阅读他人代码 | M3-W13-D5/WE1 | 开源项目架构图 + 阅读笔记 |
| 技术方案文档 | M6-W25-D4/D5 | Capstone 技术方案文档 |

---

# 附录 E：时间估算

- 每周：16h（工作日 10h + 周末 6h）
- 36 周总计：576h
- 每个 Anchor 平均：576h ÷ 252 ≈ 2.3h
- 弹性缓冲：36 个 WE2 ≈ 54h

---

# 版本历史

| 版本 | 日期 | 变更说明 |
|------|------|----------|
| v1.0 | 2026-01-05 | 初始版本（32 周） |
| v2.0 | 2026-01-12 | 扩展至 36 周：M3 拆为 5 周，M7 拆为 5 周，M8-9 合并为 6 周；增加弹性缓冲；补充盲点清单 |
| v3.0 | 2026-01-12 | 针对"入职后能独立干活"目标，新增三大能力训练：Badcase 排查（M4-W15）、开源项目阅读（M3-W13）、技术方案文档（M6-W25） |
| v4.0 | 2026-01-13 | 针对"AI 零基础过渡"问题，新增三项微调：(1) M1-W4-WE2 改为必做的 AI 工程概念扫盲；(2) M1-W4-D5 增加"一键运行验证"硬门禁；(3) M2-W5-D1 增加 Provider 抽象接口设计 |
