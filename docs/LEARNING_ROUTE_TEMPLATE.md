# LEARNING_ROUTE_TEMPLATE.md（版本A｜32周全展开）
> 目标：深圳中厂｜LLM 应用开发 / AI 后端（RAG/Agent/生产化）  
> 不走：训练/算法研究岗  
> 时间：工作日 2h；周末 3h  
> 产出优先级：demo > snippet > notes；完成以 Git commit 为准  
> 调度方式：**确定性**（今日任务由 README 的 CurrentAnchor 精确映射到本模板条目）

---

## 0. 全局执行规则（AI 必须遵守）
1) 每天只学一个 **One Thing**（2小时内可完成）  
2) 每天必须有产出（demo/snippet/notes），可提交到 GitHub  
3) 默认 Teaching Mode：先问2检查题→我回答→≤10要点→≤60行示例→≤3练习→收口  
4) 只有我说“进入 Notebook Mode”才输出入库笔记  
5) 不得跨语言栈：Month1–Month6 默认 Python；Month7 才引入 Java；Month8 面试冲刺可混合  
6) “工程化要素”（日志/超时/重试/观测）必须匹配阶段：Month1 轻量、Month5+ 才系统化

---

## 1. Anchor 命名规则（README 用）
- 格式：`M{month}-W{week}-D{day}` 或 `M{month}-W{week}-WE{n}`
- 例：`M1-W2-D1` 表示 Month1 Week2 Day1（对应你旧编号 Day7）
- 每周默认 5 个工作日（D1–D5）+ 周末（WE1/WE2，可选）

---

# Month 1：Python 工程基石（Week1–Week4）
目标：能写“小而完整”的 Python 工程项目（结构清晰、可测试、可复现）

## Week1：Python 核心强化（推导式/生成器/装饰器/上下文/async）
周 Deliverable：10 个 kata + 1 个 async 最小 demo  
Exit：能解释关键边界与常见坑；demo 可跑

- M1-W1-D1 列表推导式（可读性与嵌套边界）| snippet | notes/m1w1d1.md | N/A
- M1-W1-D2 推导式进阶（dict/set/条件）| snippet | notes/m1w1d2.md | N/A
- M1-W1-D3 生成器（yield/惰性/内存）| demo | projects/week1-generator-demo/ | python demo.py
- M1-W1-D4 装饰器（计时/简单重试）| demo | projects/week1-decorator-demo/ | python demo.py
- M1-W1-D5 上下文管理器（with/资源释放）| demo | projects/week1-context-demo/ | python demo.py
- M1-W1-WE1 async 最小 demo（并发请求/限速占位）| demo | projects/week1-async-demo/ | python demo.py
- M1-W1-WE2 周验收（复述+最小实现+坑复现）| notes | notes/m1w1-review.md | N/A

## Week2：OOP + 类型系统（组合>继承 / 可替换 client/service / dataclass / pytest / logger/config）
周 Deliverable：Week2 Python 模块化骨架（client/service/logger/config）可运行  
Exit：可替换 MockClient 不改 Service；能讲清组合优于继承

> 兼容你旧编号：M1-W2-D1 = Day7，M1-W2-D2 = Day8 …

- M1-W2-D1（Day7）组合优于继承：可替换 Client（Real/Mock）+ Service 依赖接口 | demo | projects/week2-composition-client/ | python demo.py
- M1-W2-D2（Day8）Type Hints + dataclass：为 client/service 定签名与数据结构 | snippet | projects/week2-composition-client/ | python demo.py
- M1-W2-D3（Day9）模块化：包结构（client/service）+ 入口脚本 | demo | projects/week2-python-skeleton/ | python demo.py
- M1-W2-D4（Day10）pytest：≥3 测试（含 MockClient）| demo | projects/week2-python-skeleton/ | pytest -q
- M1-W2-D5（Day11）logger：最小 logger（统一格式）供 service 调用 | snippet | projects/week2-python-skeleton/ | python demo.py
- M1-W2-WE1（Day12）config：env + 默认值，驱动 client/service | snippet | projects/week2-python-skeleton/ | python demo.py
- M1-W2-WE2（Day13）整合 + README（可复现运行）| demo | projects/week2-python-skeleton/ | python demo.py

## Week3：工程模板化（src/tests/lint/typing/CI）
周 Deliverable：python-app-template（可复用脚手架）  
Exit：新项目3分钟可启动；test/lint 一键通过

- M1-W3-D1 包管理与 src 布局（uv/poetry 二选一）| demo | projects/python-app-template/ | (按README)
- M1-W3-D2 pytest 结构 + AAA 风格（≥3测试）| demo | projects/python-app-template/ | pytest -q
- M1-W3-D3 ruff 格式化/静态检查 | snippet | projects/python-app-template/ | ruff check .
- M1-W3-D4 typing 检查（pyright/mypy 选一）| snippet | projects/python-app-template/ | (按README)
- M1-W3-D5 GitHub Actions（test+lint）最小流水线 | demo | projects/python-app-template/ | (CI通过)
- M1-W3-WE1 模板固化（README/目录规范/约束）| notes | notes/m1w3-template.md | N/A
- M1-W3-WE2 周验收 | notes | notes/m1w3-review.md | N/A

## Week4：综合项目（小而完整 CLI）
周 Deliverable：可运行 CLI（带测试/日志/README）  
Exit：陌生机器按 README 跑通；你能讲清架构取舍

- M1-W4-D1 CLI 框架选型（argparse/typer）+ 命令结构 | demo | projects/cli-tool/ | python -m cli_tool --help
- M1-W4-D2 IO（文件/HTTP 选一）+ 错误处理 | demo | projects/cli-tool/ | (按README)
- M1-W4-D3 并发（async/线程池 选一）最小提速 | demo | projects/cli-tool/ | (按README)
- M1-W4-D4 测试 ≥5（正常/异常/边界）| demo | projects/cli-tool/ | pytest -q
- M1-W4-D5 README + 1分钟演示稿 | notes | notes/m1w4-cli.md | N/A
- M1-W4-WE1 周验收（复述+最小实现+坑复现）| notes | notes/m1w4-review.md | N/A
- M1-W4-WE2 补洞（本月 OpenQuestions Top3）| snippet | notes/m1w4-fix.md | N/A

---

# Month 2：LLM API 工程化（Week5–Week8）
目标：稳定调用模型、工具调用闭环、提示工程可回归、服务化可演示

## Week5：LLMClient 基础封装（timeout/retry/结构化/mock/测试）
周 Deliverable：Python LLMClient（可测试、可复现）  
Exit：能解释 token/成本/失败模式；可用 Mock 测试

- M2-W5-D1 设计 LLMClient 接口（req/resp dataclass）| demo | projects/llm-client/ | python demo.py
- M2-W5-D2 超时/重试（简化）+ 错误分类 | demo | projects/llm-client/ | python demo.py
- M2-W5-D3 结构化输出（JSON schema 思路）+ 解析容错 | demo | projects/llm-client/ | python demo.py
- M2-W5-D4 MockClient + 单测≥3 | demo | projects/llm-client/ | pytest -q
- M2-W5-D5 README（成本/限制/最佳实践）| notes | notes/m2w5-llmclient.md | N/A
- M2-W5-WE1 周验收 | notes | notes/m2w5-review.md | N/A
- M2-W5-WE2 补洞（失败模式清单）| notes | notes/m2w5-failures.md | N/A

## Week6：Tool/Function Calling（工具注册/路由/校验/回退/测试）
周 Deliverable：tools registry + 端到端 demo  
Exit：能做 schema、参数校验、错误回传；可 mock 测试

- M2-W6-D1 工具接口定义（name/schema/handler）| demo | projects/tools-demo/ | python demo.py
- M2-W6-D2 工具路由与参数校验 | demo | projects/tools-demo/ | python demo.py
- M2-W6-D3 多工具选择 + 失败回退 | demo | projects/tools-demo/ | python demo.py
- M2-W6-D4 mock LLM + 工具调用测试（≥3）| demo | projects/tools-demo/ | pytest -q
- M2-W6-D5 文档化（工具清单/边界）| notes | notes/m2w6-tools.md | N/A
- M2-W6-WE1 周验收 | notes | notes/m2w6-review.md | N/A
- M2-W6-WE2 小整合（接入 Week5 LLMClient）| demo | projects/tools-demo/ | python demo.py

## Week7：Prompt 工程化（模板/版本/回归）
周 Deliverable：prompt-kit（模板+版本+回归用例）  
Exit：能解释“为什么这样写”；能回归验证不退步

- M2-W7-D1 prompt 模板结构（system/dev/user）+ 变量注入 | snippet | projects/prompt-kit/ | python demo.py
- M2-W7-D2 prompt 版本化（v1/v2）+ 变更记录 | notes | notes/m2w7-prompt-version.md | N/A
- M2-W7-D3 约束输出（格式/边界/拒答策略）| demo | projects/prompt-kit/ | python demo.py
- M2-W7-D4 回归用例集（≤10）+ 自动跑通 | demo | projects/prompt-kit/ | python demo.py
- M2-W7-D5 总结（最佳实践清单）| notes | notes/m2w7-summary.md | N/A
- M2-W7-WE1 周验收 | notes | notes/m2w7-review.md | N/A
- M2-W7-WE2 补洞（失败案例→修复）| demo | projects/prompt-kit/ | python demo.py

## Week8：服务化（FastAPI + SSE/stream + 基础观测）
周 Deliverable：/chat 流式接口可演示  
Exit：日志字段、错误码、最小观测可用

- M2-W8-D1 FastAPI 最小服务 + /health | demo | projects/llm-service/ | uvicorn app:app
- M2-W8-D2 SSE/stream 返回 | demo | projects/llm-service/ | uvicorn app:app
- M2-W8-D3 错误码与异常中间件 | demo | projects/llm-service/ | uvicorn app:app
- M2-W8-D4 日志字段（trace_id/耗时/失败原因）| snippet | projects/llm-service/ | uvicorn app:app
- M2-W8-D5 README + 演示脚本（2分钟）| notes | notes/m2w8-service.md | N/A
- M2-W8-WE1 周验收 | notes | notes/m2w8-review.md | N/A
- M2-W8-WE2 作品集整理（把 Week5–8 聚合到一个 README）| notes | notes/m2-portfolio-index.md | N/A

---

# Month 3：RAG 数据工程（Week9–Week12）
目标：可用的检索增强（摄取/切分/索引/检索/混合/重排），端到端可跑

## Week9：数据摄取与切分（ingest/chunk/metadata）
周 Deliverable：ingest + chunk 对比 demo  
Exit：能解释 chunk 策略影响；可复现

- M3-W9-D1 文档加载器（md/pdf 二选一）| demo | projects/rag-ingest/ | python demo.py
- M3-W9-D2 chunk 策略（长度/重叠）对比实验 | demo | projects/rag-ingest/ | python demo.py
- M3-W9-D3 元数据设计（source/page/section）| snippet | projects/rag-ingest/ | python demo.py
- M3-W9-D4 清洗与去噪（最小规则）| demo | projects/rag-ingest/ | python demo.py
- M3-W9-D5 总结（chunk 策略 checklist）| notes | notes/m3w9-chunk.md | N/A
- M3-W9-WE1 周验收 | notes | notes/m3w9-review.md | N/A
- M3-W9-WE2 补洞（失败案例：过长/过短 chunk）| demo | projects/rag-ingest/ | python demo.py

## Week10：向量库与检索（topK/过滤/拼装context）
周 Deliverable：vector store + retrieval demo  
Exit：能解释召回/精度权衡；可跑

- M3-W10-D1 选向量库（本地优先）+ 最小接入 | demo | projects/rag-retrieval/ | python demo.py
- M3-W10-D2 topK 检索 + metadata 过滤 | demo | projects/rag-retrieval/ | python demo.py
- M3-W10-D3 query rewrite（简化）或多查询 | demo | projects/rag-retrieval/ | python demo.py
- M3-W10-D4 context 构造（拼装/去重/截断）| demo | projects/rag-retrieval/ | python demo.py
- M3-W10-D5 总结（检索参数默认值表）| notes | notes/m3w10-retrieval.md | N/A
- M3-W10-WE1 周验收 | notes | notes/m3w10-review.md | N/A
- M3-W10-WE2 补洞（检索失败模式 5 条）| notes | notes/m3w10-failures.md | N/A

## Week11：混合检索与重排（BM25+向量 / rerank）
周 Deliverable：rerank 接入 + 对比实验  
Exit：能解释何时有效/何时无效

- M3-W11-D1 BM25（简化）接入或占位实现 | demo | projects/rag-hybrid/ | python demo.py
- M3-W11-D2 混合检索（BM25+向量）权重/合并策略 | demo | projects/rag-hybrid/ | python demo.py
- M3-W11-D3 rerank 接入（接口 + 最小实现）| demo | projects/rag-rerank/ | python demo.py
- M3-W11-D4 对比实验（无重排 vs 有重排）| demo | projects/rag-rerank/ | python demo.py
- M3-W11-D5 总结（重排 checklist + 失败案例）| notes | notes/m3w11-rerank.md | N/A
- M3-W11-WE1 周验收 | notes | notes/m3w11-review.md | N/A
- M3-W11-WE2 补洞（引用来源格式统一）| snippet | projects/rag-rerank/ | python demo.py

## Week12：RAG 端到端最小系统（问题→检索→回答→引用）
周 Deliverable：RAG API / CLI 二选一（可演示）  
Exit：可跑、可复现、可展示引用来源

- M3-W12-D1 端到端 pipeline 串联 | demo | projects/rag-e2e/ | python demo.py
- M3-W12-D2 prompt 组装（引用来源/拒答占位）| demo | projects/rag-e2e/ | python demo.py
- M3-W12-D3 缓存（简化：query→result）| snippet | projects/rag-e2e/ | python demo.py
- M3-W12-D4 服务化（FastAPI 最小）| demo | projects/rag-e2e/ | uvicorn app:app
- M3-W12-D5 README + 2分钟演示脚本 | notes | notes/m3w12-rag-e2e.md | N/A
- M3-W12-WE1 周验收 | notes | notes/m3w12-review.md | N/A
- M3-W12-WE2 作品集整理（RAG 一页纸）| notes | notes/m3-rag-onepager.md | N/A

---

# Month 4：RAG 评测闭环（Week13–Week16）
目标：用数据说话（dataset/metrics/baseline→改进→回归门禁→可投递版本）

## Week13：评测数据集与指标
周 Deliverable：小数据集（≤20）+ eval 脚本雏形  
Exit：能跑出报告（json/markdown）

- M4-W13-D1 构造 QA 集（≤20条）| notes | notes/m4w13-dataset.md | N/A
- M4-W13-D2 指标定义（准确/引用/拒答/一致性）| notes | notes/m4w13-metrics.md | N/A
- M4-W13-D3 eval 脚本雏形（跑通）| demo | projects/rag-eval/ | python eval.py
- M4-W13-D4 报告输出（json + markdown）| demo | projects/rag-eval/ | python eval.py
- M4-W13-D5 总结（评测流程图）| notes | notes/m4w13-summary.md | N/A
- M4-W13-WE1 周验收 | notes | notes/m4w13-review.md | N/A
- M4-W13-WE2 补洞（坏case 3条）| notes | notes/m4w13-badcases.md | N/A

## Week14：baseline 固化 + 第一次改进
周 Deliverable：baseline + 改进对比报告  
Exit：能解释为何提升/为何无效

- M4-W14-D1 baseline 固化（参数/版本锁定）| demo | projects/rag-eval/ | python eval.py
- M4-W14-D2 改进1：chunk 策略对比 | demo | projects/rag-eval/ | python eval.py
- M4-W14-D3 改进2：topK/过滤策略对比 | demo | projects/rag-eval/ | python eval.py
- M4-W14-D4 改进3：rerank/混检（若已接）| demo | projects/rag-eval/ | python eval.py
- M4-W14-D5 总结（提升归因模板）| notes | notes/m4w14-summary.md | N/A
- M4-W14-WE1 周验收 | notes | notes/m4w14-review.md | N/A
- M4-W14-WE2 补洞（不升反降分析）| notes | notes/m4w14-regression.md | N/A

## Week15：回归测试与质量门禁（不退步）
周 Deliverable：回归集 + 门禁规则 + 自动对比报告  
Exit：一键跑评测，输出“是否通过”

- M4-W15-D1 回归用例集（≤10）| notes | notes/m4w15-regression-set.md | N/A
- M4-W15-D2 失败分析模板（分类/根因/修复）| notes | notes/m4w15-failure-template.md | N/A
- M4-W15-D3 门禁规则（不退步阈值）| demo | projects/rag-eval/ | python eval.py
- M4-W15-D4 自动生成对比报告（diff）| demo | projects/rag-eval/ | python eval.py
- M4-W15-D5 总结（门禁说明）| notes | notes/m4w15-summary.md | N/A
- M4-W15-WE1 周验收 | notes | notes/m4w15-review.md | N/A
- M4-W15-WE2 补洞（评测速度优化占位）| snippet | projects/rag-eval/ | python eval.py

## Week16：RAG 作品集版本（可投递）
周 Deliverable：rag-portfolio（README/架构/指标/部署）  
Exit：别人按 README 可跑；你能讲 2 分钟

- M4-W16-D1 代码整理与目录规范 | demo | projects/rag-portfolio/ | (按README)
- M4-W16-D2 README（架构图/取舍/指标）| notes | notes/m4w16-readme.md | N/A
- M4-W16-D3 演示脚本与录屏提纲 | notes | notes/m4w16-demo.md | N/A
- M4-W16-D4 Docker 最小部署（compose）| demo | projects/rag-portfolio/ | docker compose up
- M4-W16-D5 周总结（RAG 一页纸更新）| notes | notes/m4w16-summary.md | N/A
- M4-W16-WE1 周验收 | notes | notes/m4w16-review.md | N/A
- M4-W16-WE2 作品集聚合 README 更新 | notes | README.md | N/A

---

# Month 5：Agent（Week17–Week20）
目标：可控 Agent（工具/状态/回退/多步），失败模式可解释

## Week17：工具编排与状态（Agent Core）
周 Deliverable：agent-core（tools registry + state + fallback）  
Exit：mock 可测；失败可回退

- M5-W17-D1 工具注册中心复用（schema/handler）| demo | projects/agent-core/ | python demo.py
- M5-W17-D2 状态结构（Memory/Context）定义 | demo | projects/agent-core/ | python demo.py
- M5-W17-D3 回退策略（失败→降级）| demo | projects/agent-core/ | python demo.py
- M5-W17-D4 测试：mock 工具/LLM（≥3）| demo | projects/agent-core/ | pytest -q
- M5-W17-D5 总结（Agent 失败模式清单）| notes | notes/m5w17-summary.md | N/A
- M5-W17-WE1 周验收 | notes | notes/m5w17-review.md | N/A
- M5-W17-WE2 补洞（错误分类与回退一致性）| snippet | projects/agent-core/ | python demo.py

## Week18：规划与多步执行（Planner/Runner）
周 Deliverable：agent-plan（planner+runner 可演示）  
Exit：能中断/恢复（占位）与成功率统计（简化）

- M5-W18-D1 简单 planner（步骤列表）| demo | projects/agent-plan/ | python demo.py
- M5-W18-D2 执行器（step runner）+ 日志 | demo | projects/agent-plan/ | python demo.py
- M5-W18-D3 中断/恢复（状态持久化占位）| snippet | projects/agent-plan/ | python demo.py
- M5-W18-D4 成功率/失败分类统计（简化）| demo | projects/agent-plan/ | python demo.py
- M5-W18-D5 总结（多步失败模式）| notes | notes/m5w18-summary.md | N/A
- M5-W18-WE1 周验收 | notes | notes/m5w18-review.md | N/A
- M5-W18-WE2 补洞（工具参数校验强化）| demo | projects/agent-plan/ | python demo.py

## Week19：多 Agent 协作（简化）
周 Deliverable：multi-agent（planner/executor/reviewer）  
Exit：handoff schema 明确；冲突处理可解释

- M5-W19-D1 角色拆分（planner/executor/reviewer）| demo | projects/multi-agent/ | python demo.py
- M5-W19-D2 协作协议（handoff schema）| snippet | projects/multi-agent/ | python demo.py
- M5-W19-D3 冲突处理（投票/优先级）| demo | projects/multi-agent/ | python demo.py
- M5-W19-D4 回归用例（≤10）| demo | projects/multi-agent/ | python demo.py
- M5-W19-D5 总结（协作失败模式）| notes | notes/m5w19-summary.md | N/A
- M5-W19-WE1 周验收 | notes | notes/m5w19-review.md | N/A
- M5-W19-WE2 补洞（协议与实现一致）| snippet | projects/multi-agent/ | python demo.py

## Week20：Agent 作品集版本
周 Deliverable：agent-portfolio（可投递）  
Exit：2分钟演示；README/部署/限制说明齐全

- M5-W20-D1 整理成可演示项目 | demo | projects/agent-portfolio/ | (按README)
- M5-W20-D2 README（能力边界/失败模式）| notes | notes/m5w20-readme.md | N/A
- M5-W20-D3 Docker 最小部署 | demo | projects/agent-portfolio/ | docker compose up
- M5-W20-D4 测试与门禁（pytest + 基线）| demo | projects/agent-portfolio/ | pytest -q
- M5-W20-D5 周总结（Agent 一页纸）| notes | notes/m5w20-summary.md | N/A
- M5-W20-WE1 周验收 | notes | notes/m5w20-review.md | N/A
- M5-W20-WE2 作品集聚合 README 更新 | notes | README.md | N/A

---

# Month 6：生产化（Week21–Week24）
目标：服务化、观测、成本、缓存、限流、部署、回归评测

## Week21：服务化与观测（基础）
周 Deliverable：prod-service（FastAPI + 基础观测）  
Exit：日志字段规范；错误码清晰；最小指标可用

- M6-W21-D1 FastAPI + SSE 稳定版 | demo | projects/prod-service/ | uvicorn app:app
- M6-W21-D2 日志字段规范（trace_id/耗时/错误）| snippet | projects/prod-service/ | uvicorn app:app
- M6-W21-D3 指标（简化：计数/延迟）| snippet | projects/prod-service/ | uvicorn app:app
- M6-W21-D4 限流/降级（简化）| demo | projects/prod-service/ | uvicorn app:app
- M6-W21-D5 总结（观测 checklist）| notes | notes/m6w21-summary.md | N/A
- M6-W21-WE1 周验收 | notes | notes/m6w21-review.md | N/A
- M6-W21-WE2 补洞（观测字段一致性）| snippet | projects/prod-service/ | uvicorn app:app

## Week22：缓存与成本控制
周 Deliverable：成本核算 + 缓存策略落地  
Exit：能解释成本；能跑压测占位（简化）

- M6-W22-D1 缓存策略（prompt/result）| demo | projects/prod-service/ | uvicorn app:app
- M6-W22-D2 token 统计与成本核算 | snippet | projects/prod-service/ | uvicorn app:app
- M6-W22-D3 失败重试与幂等（简化）| demo | projects/prod-service/ | uvicorn app:app
- M6-W22-D4 配置化开关（feature flag 简化）| snippet | projects/prod-service/ | uvicorn app:app
- M6-W22-D5 总结（成本优化清单）| notes | notes/m6w22-summary.md | N/A
- M6-W22-WE1 周验收 | notes | notes/m6w22-review.md | N/A
- M6-W22-WE2 补洞（缓存失效策略）| notes | notes/m6w22-cache.md | N/A

## Week23：网关与本地推理（可选但建议了解）
周 Deliverable：llm-gateway（统一 client + 路由占位）  
Exit：能讲清网关价值；能跑最小基准

- M6-W23-D1 本地推理概念与部署草图 | notes | notes/m6w23-local-llm.md | N/A
- M6-W23-D2 网关封装（统一 client 接口）| demo | projects/llm-gateway/ | python demo.py
- M6-W23-D3 负载/超时策略（简化）| demo | projects/llm-gateway/ | python demo.py
- M6-W23-D4 基准测试（QPS/延迟 占位）| demo | projects/llm-gateway/ | python bench.py
- M6-W23-D5 总结（网关设计要点）| notes | notes/m6w23-summary.md | N/A
- M6-W23-WE1 周验收 | notes | notes/m6w23-review.md | N/A
- M6-W23-WE2 补洞（失败回退策略）| snippet | projects/llm-gateway/ | python demo.py

## Week24：Capstone 整合（RAG + Agent + Service）
周 Deliverable：capstone（可投递系统雏形）  
Exit：一键部署；回归评测不退步；2分钟演示

- M6-W24-D1 整合 RAG + Agent + Service（端到端）| demo | projects/capstone/ | (按README)
- M6-W24-D2 README（架构图/权衡/指标）| notes | notes/m6w24-readme.md | N/A
- M6-W24-D3 一键部署（docker compose）| demo | projects/capstone/ | docker compose up
- M6-W24-D4 回归评测（不退步）| demo | projects/capstone/ | python eval.py
- M6-W24-D5 总结（capstone 一页纸）| notes | notes/m6w24-summary.md | N/A
- M6-W24-WE1 周验收 | notes | notes/m6w24-review.md | N/A
- M6-W24-WE2 作品集首页聚合 | notes | README.md | N/A

---

# Month 7：Java 混合落地 + 系统设计（Week25–Week28）
目标：用 Java 接住工程化叙事，形成中厂“后端+AI应用”可投递故事线

## Week25：Java 调用 LLM/RAG 服务（HTTP/SSE/错误码/trace）
周 Deliverable：java-llm-client（可演示）  
Exit：能讲清重试/错误码/trace_id 打通

- M7-W25-D1 Java HTTP Client 最小封装（调用 /chat）| demo | projects/java-llm-client/ | (按README)
- M7-W25-D2 统一错误码与重试策略（简化）| demo | projects/java-llm-client/ | (按README)
- M7-W25-D3 SSE/流式消费（客户端）| demo | projects/java-llm-client/ | (按README)
- M7-W25-D4 trace_id 贯通（请求→日志）| snippet | projects/java-llm-client/ | (按README)
- M7-W25-D5 总结（Java 侧工程化要点）| notes | notes/m7w25-summary.md | N/A
- M7-W25-WE1 周验收 | notes | notes/m7w25-review.md | N/A
- M7-W25-WE2 补洞（异常分类与告警占位）| notes | notes/m7w25-alert.md | N/A

## Week26：系统设计题（RAG 服务架构）
周 Deliverable：RAG 架构题 1 套完整讲解稿（含图）  
Exit：能 10 分钟讲清组件/数据流/失败模式/扩展点

- M7-W26-D1 架构图（组件/数据流 ASCII）| notes | notes/m7w26-arch.md | N/A
- M7-W26-D2 存储与索引策略（更新/重建/一致性）| notes | notes/m7w26-storage.md | N/A
- M7-W26-D3 缓存/一致性/更新策略 | notes | notes/m7w26-cache.md | N/A
- M7-W26-D4 容灾与降级（无检索/低配模型/兜底）| notes | notes/m7w26-fallback.md | N/A
- M7-W26-D5 总结（面试回答模板）| notes | notes/m7w26-answer.md | N/A
- M7-W26-WE1 周验收 | notes | notes/m7w26-review.md | N/A
- M7-W26-WE2 补洞（容量估算占位）| notes | notes/m7w26-capacity.md | N/A

## Week27：Agent 服务化与安全（提示注入/权限/审计）
周 Deliverable：安全 demo + 讲解稿  
Exit：能讲清风险与防护策略

- M7-W27-D1 工具权限模型（允许/拒绝/审计）| notes | notes/m7w27-permission.md | N/A
- M7-W27-D2 异步执行（队列/任务状态占位）| notes | notes/m7w27-async.md | N/A
- M7-W27-D3 审计日志与合规（字段/留存）| notes | notes/m7w27-audit.md | N/A
- M7-W27-D4 提示注入/越权攻击最小 demo + 防护 | demo | projects/security-demo/ | python demo.py
- M7-W27-D5 总结（安全清单）| notes | notes/m7w27-summary.md | N/A
- M7-W27-WE1 周验收 | notes | notes/m7w27-review.md | N/A
- M7-W27-WE2 补洞（红队用例 ≤10）| notes | notes/m7w27-redteam.md | N/A

## Week28：简历叙事与作品集打磨
周 Deliverable：项目一页纸 + 指标叙事 + 面试题库  
Exit：可投递、可讲述、可演示

- M7-W28-D1 项目一页纸（RAG）| notes | notes/m7w28-rag-onepager.md | N/A
- M7-W28-D2 项目一页纸（Agent）| notes | notes/m7w28-agent-onepager.md | N/A
- M7-W28-D3 指标叙事（baseline→提升）| notes | notes/m7w28-metrics.md | N/A
- M7-W28-D4 常见面试题库（工程/系统/LLM）| notes | notes/m7w28-interview.md | N/A
- M7-W28-D5 总结（自我介绍/反问清单）| notes | notes/m7w28-pitch.md | N/A
- M7-W28-WE1 周验收 | notes | notes/m7w28-review.md | N/A
- M7-W28-WE2 投递准备（岗位JD匹配清单）| notes | notes/m7w28-apply.md | N/A

---

# Month 8：面试冲刺（Week29–Week32）
目标：稳定输出、系统设计答题、模拟面、投递闭环

## Week29：RAG 深挖（失败模式/重排/评测讲解）
周 Deliverable：RAG 讲解稿 + 2分钟演示脚本  
Exit：能把失败模式讲清并给方案

- M8-W29-D1 检索失败模式清单（≥10）| notes | notes/m8w29-failures.md | N/A
- M8-W29-D2 重排/混检讲解稿 | notes | notes/m8w29-rerank.md | N/A
- M8-W29-D3 评测体系讲解稿（门禁/回归）| notes | notes/m8w29-eval.md | N/A
- M8-W29-D4 2分钟演示脚本（RAG）| notes | notes/m8w29-demo.md | N/A
- M8-W29-D5 总结（RAG 常问快答）| notes | notes/m8w29-qa.md | N/A
- M8-W29-WE1 周验收 | notes | notes/m8w29-review.md | N/A
- M8-W29-WE2 补洞（最弱点专项）| notes | notes/m8w29-fix.md | N/A

## Week30：Agent 深挖（工具/状态/回退/测试）
周 Deliverable：Agent 讲解稿 + 回归策略  
Exit：能讲清可控性与失败处理

- M8-W30-D1 Agent 失败模式与回退讲解稿 | notes | notes/m8w30-fallback.md | N/A
- M8-W30-D2 工具设计与权限讲解稿 | notes | notes/m8w30-tools.md | N/A
- M8-W30-D3 状态机与可恢复性讲解稿 | notes | notes/m8w30-state.md | N/A
- M8-W30-D4 测试策略（mock/回归）讲解稿 | notes | notes/m8w30-tests.md | N/A
- M8-W30-D5 总结（Agent 常问快答）| notes | notes/m8w30-qa.md | N/A
- M8-W30-WE1 周验收 | notes | notes/m8w30-review.md | N/A
- M8-W30-WE2 补洞（最弱点专项）| notes | notes/m8w30-fix.md | N/A

## Week31：系统设计模拟面（3套题）
周 Deliverable：3套系统设计完整稿  
Exit：每套 10–15 分钟可讲清

- M8-W31-D1 题1：RAG 服务设计（完整讲解稿）| notes | notes/m8w31-sd1.md | N/A
- M8-W31-D2 题2：Agent 平台设计（完整讲解稿）| notes | notes/m8w31-sd2.md | N/A
- M8-W31-D3 题3：成本/观测/稳定性（完整讲解稿）| notes | notes/m8w31-sd3.md | N/A
- M8-W31-D4 反问清单 + 自我介绍（终版）| notes | notes/m8w31-pitch.md | N/A
- M8-W31-D5 总结（模拟面复盘模板）| notes | notes/m8w31-retro.md | N/A
- M8-W31-WE1 周验收 | notes | notes/m8w31-review.md | N/A
- M8-W31-WE2 补洞（最弱题重练）| notes | notes/m8w31-fix.md | N/A

## Week32：投递与复盘闭环
周 Deliverable：简历终版 + 作品集首页 + 投递策略  
Exit：可投递、可追踪、可复盘

- M8-W32-D1 简历终版（项目突出/指标化）| notes | notes/m8w32-resume.md | N/A
- M8-W32-D2 作品集首页（README 聚合/目录）| notes | notes/m8w32-portfolio.md | N/A
- M8-W32-D3 投递策略（岗位JD匹配/渠道/节奏）| notes | notes/m8w32-apply.md | N/A
- M8-W32-D4 模拟面复盘与补洞（Top3）| notes | notes/m8w32-retro.md | N/A
- M8-W32-D5 收官总结（下一阶段规划）| notes | notes/m8w32-summary.md | N/A
- M8-W32-WE1 最终验收（作品集走查）| notes | notes/m8w32-final-review.md | N/A
- M8-W32-WE2 复盘与下一目标（涨薪/跳槽/扩展）| notes | notes/m8w32-next.md | N/A