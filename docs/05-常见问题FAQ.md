# 常见问题 FAQ

## 🎯 目的
记录学习过程中遇到的问题和解决方案，避免重复踩坑

---

## 🔧 技术问题

### Python 相关

#### Q1: 虚拟环境如何创建和激活？

```bash
# 创建虚拟环境
python -m venv venv

# 激活（Windows）
venv\Scripts\activate

# 激活（Mac/Linux）
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

#### Q2: 如何管理 API Key？

不要直接写在代码里！

```python
# ❌ 错误做法
api_key = "sk-xxxxxxxxxxxxx"

# ✅ 正确做法
# 1. 创建 .env 文件
# OPENAI_API_KEY=sk-xxxxxxxxxxxxx

# 2. 在代码中读取
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

```

#### Q3: 如何处理中文编码问题？

```python
# 读写文件时指定编码
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(content)

```

### AI/大模型相关

#### Q1: Token 怎么计算？

##### 简单估算：

​	∙	英文：1 单词 ≈ 1.3 tokens
​	∙	中文：1 个字 ≈ 1.5-2 tokens
##### 精确计算：

```python
import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4")
text = "你好，世界！"
tokens = encoding.encode(text)
print(f"Token 数: {len(tokens)}")

```

#### Q2: 为什么我的 API 调用失败？

##### 常见原因：

	1.	API Key 错误或过期
	2.	余额不足
	3.	请求格式错误
	4.	网络问题（国内需要代理）
	5.	达到速率限制

##### 调试步骤：

```python
try:
    response = client.chat.completions.create(...)
except Exception as e:
    print(f"错误类型: {type(e)}")
    print(f"错误信息: {str(e)}")

```

#### Q3: 如何优化 API 成本？

	1.	使用合适的模型：不是所有任务都需要 GPT-4
	2.	控制 max_tokens：限制输出长度
	3.	压缩 Prompt：去除不必要的内容
	4.	使用缓存：相同问题不重复调用
	5.	批量处理：合并多个请求

### 📚 学习相关

#### Q1: 感觉学得太慢，要不要加快进度？
不要！
原因：
	∙	基础不扎实，后面会更慢
	∙	“学会” ≠ “看过”
	∙	稳扎稳打才能走得更远
建议：
	∙	按照计划进度来
	∙	重视验收和实践
	∙	不要和别人比进度
#### Q2: 遇到不懂的概念怎么办？
步骤：

	1.	先自己思考 5 分钟
	2.	尝试用自己的话解释
	3.	问 Claude（这就是 Teaching Mode 的作用）
	4.	不要直接搜索答案（会养成依赖）
	Q3: 什么时候该整理笔记？
	触发条件：
	∙	完成一个完整的知识点
	∙	需要总结和回顾
	∙	明确说：“可以整理【全栈宗师笔记】了”
	不要：
	∙	每学一点就要笔记
	∙	打断学习流程去整理

## 🛠️ 工具问题

#### Q1: 推荐的代码编辑器？
VS Code（强烈推荐）
必装插件：
	∙	Python
	∙	Pylance
	∙	Python Debugger
	∙	GitLens
	∙	Better Comments
#### Q2: 如何调试 Python 代码？

```python
# 方法1：print 调试（简单粗暴）
print(f"变量值: {variable}")

# 方法2：使用 logging
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug(f"调试信息: {variable}")

# 方法3：使用 VS Code 断点调试（最强大）
# 在代码行号左侧点击添加断点
# 按 F5 开始调试

```

