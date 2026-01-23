# Day 1 - 列表推导式基础（2026-01-05）

## 核心目标

理解列表推导式的本质：表达意图而非描述过程

------

## Why（不学会导致的工程死穴）

如果不理解列表推导式的本质，你会：

- ❌ 把它当作"代码简化技巧"，只是背模板
- ❌ 写出冗长的循环代码，降低代码可读性
- ❌ 无法快速理解他人的 Python 代码（列表推导式在 Python 中极其常见）
- ❌ 在面试和 Code Review 时显得不够 Pythonic

------

## What（第一性原理 + 类比）

**本质：** 列表推导式不是"简化循环"，而是"声明式编程"的体现。

**传统循环（命令式）：**



python

```python
squares = []
for num in numbers:
    squares.append(num ** 2)
```

→ 关注**过程**："先创建空列表，再循环，再添加"

**列表推导式（声明式）：**



python

```python
squares = [num ** 2 for num in numbers]
```

→ 关注**结果**："我要一个新列表，内容是每个数的平方"

**类比：**

> 传统循环 = 在餐厅详细描述做菜步骤
>
> 列表推导式 = 直接说"我要一份番茄炒蛋"

------

## How（最小可运行范式）

**基础语法：**



python

```python
[表达式 for 变量 in 可迭代对象]
```

**示例1：平方数**



python

```python
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
# 结果: [1, 4, 9, 16, 25]
```

**示例2：字符串长度**



python

```python
words = ["hello", "world", "python"]
lengths = [len(word) for word in words]
# 结果: [5, 5, 6]
```

**带过滤条件：**



python

```python
[表达式 for 变量 in 可迭代对象 if 条件]
```

**示例3：筛选偶数**



python

```python
numbers = [1, 2, 3, 4, 5]
evens = [n for n in numbers if n % 2 == 0]
# 结果: [2, 4]
```

**示例4：偶数的平方**



python

```python
numbers = [1, 2, 3, 4, 5]
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
# 结果: [4, 16]
```

------

## Pitfall（真实踩坑）

**坑1：套用模板，不理解原理**



python

~~~python
# 错误思维：看到 range(10)，以为传入一个数字，输出一个数字
result = [x for x in range(10)]  # 实际输出 [0,1,2,3,4,5,6,7,8,9]
```
**教训：** 不要"背模板"，要拆解理解每个部分

**坑2：快速猜答案，不深入思考**
- 看到代码 → 凭感觉猜 ❌
- 应该：拆解每个部分 → 确认理解 → 再回答 ✅

---

### Application（在哪里用）

**实际应用场景：**
1. **数据处理**：提取、转换列表中的元素
2. **过滤数据**：根据条件筛选
3. **API 响应处理**：提取 JSON 数据中的特定字段
4. **文件处理**：批量处理文件名、路径

**在后续学习中的位置：**
- Month 2（大模型应用）：处理 API 返回的消息列表
- Month 3（RAG系统）：批量处理文档分块
- Month 5（Agent开发）：处理工具调用结果

---

### 视觉闭环
```
传统循环流程：
创建空列表 → 开始循环 → 处理元素 → 添加到列表 → 结束循环
   ↓           ↓          ↓          ↓           ↓
  []     for num in...  num**2   append()    完成

列表推导式流程：
声明需求："我要一个列表，内容是..." → 直接得到结果
           [num**2 for num in numbers]
~~~

------

## 工程师记忆分层

**🗑️ 垃圾区（查文档就行）：**

- 具体的语法细节（括号、逗号位置）
- 更复杂的推导式变体（字典推导式、集合推导式）

**🔍 索引区（记关键词）：**

- 遇到"需要创建新列表" → 想到列表推导式
- 遇到"需要过滤 + 转换" → 想到带 if 的推导式
- 看到 `[... for ... in ...]` → 知道是声明式创建列表

**💎 核心区（必须内化）：**

- 列表推导式 = 表达"要什么"，不是"怎么做"
- 结构：`[表达式 for 变量 in 可迭代对象 (if 条件)]`
- 学习方法：不背模板，要拆解理解
- 正确思维：慢慢分析 > 快速猜答案

---

# Day 2 - 列表推导式进阶（2026-01-06）

## 核心目标

理解列表推导式的适用边界，建立"可读性 > 简洁性"的工程思维

------

## Why（不学会导致的工程死穴）

如果不理解什么时候该用/不该用列表推导式，你会：

- ❌ 为了"炫技"写出复杂难懂的列表推导式
- ❌ 降低代码可维护性（3个月后自己都看不懂）
- ❌ 在 Code Review 时被批评"过度使用"
- ❌ 陷入"能用就用"的误区，忽视可读性

**工程上的真实代价：**

- 调试时间增加 3-5 倍
- 新人接手代码困难
- 容易引入 bug（复杂逻辑难以发现错误）

------

## What（第一性原理 + 类比）

**核心原则：**

> 可读性 > 简洁性

列表推导式不是为了"少写代码"，而是为了**更清晰地表达意图**。

**嵌套列表推导式：**



python

```python
# 能写，但不代表应该写
result = [num for row in matrix for num in row]
```

虽然语法上支持，但会降低可读性。

**判断标准（4条全满足才用）：**

1. ✅ 单层循环
2. ✅ 简单表达式（一眼看懂）
3. ✅ 简单条件（if 后面不超过 3 个单词，或清晰的 and 连接）
4. ✅ 3个月后再看，5秒内能懂

**类比：**

> 写代码 = 写给人看的，不是写给机器看的
>
> 列表推导式 = 餐厅点菜（清晰明确）
>
> 复杂的嵌套推导式 = 用密码对话（虽然能懂，但费劲）

------

## How（最小可运行范式）

### **应该用列表推导式的场景：**

**1. 简单转换**



python

```python
# ✅ 好：价格加税
prices_with_tax = [price * 1.1 for price in prices]

# ✅ 好：字符串转大写
upper_names = [name.upper() for name in names]
```

**2. 简单过滤**



python

```python
# ✅ 好：找偶数
evens = [x for x in numbers if x % 2 == 0]

# ✅ 好：找成年人
adults = [user for user in users if user['age'] >= 18]
```

**3. 简单过滤 + 转换**



python

```python
# ✅ 好：偶数的平方
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
```

**4. 清晰的多条件过滤**



python

```python
# ✅ 好：北京的成年人的名字
names = [u['name'] for u in users 
         if u['age'] >= 18 and u['city'] == "Beijing"]
```

------

### **不应该用列表推导式的场景：**

**1. 嵌套循环（两层及以上）**



python

```python
# ❌ 不好：二维拉平
result = [num for row in matrix for num in row]

# ✅ 改用传统循环
result = []
for row in matrix:
    for num in row:
        result.append(num)
```

**2. 复杂的逻辑**



python

```python
# ❌ 不好：找质数（需要复杂函数）
primes = [n for n in range(2, 101) if is_prime(n)]

# ✅ 改用传统循环
primes = []
for n in range(2, 101):
    if is_prime(n):
        primes.append(n)
```

**3. 复杂的条件判断**



python

```python
# ❌ 不好：多重条件，难以理解
result = [x * 2 if x > 0 else x / 2 for x in numbers if x != 0]

# ✅ 改用传统循环
result = []
for x in numbers:
    if x != 0:
        if x > 0:
            result.append(x * 2)
        else:
            result.append(x / 2)
```

**4. 需要复杂判断的过滤**



python

```python
# ❌ 不好：判断回文（需要反转对比）
palindromes = [w for w in words if w == w[::-1]]

# ✅ 改用传统循环（逻辑更清晰）
palindromes = []
for word in words:
    if word == word[::-1]:
        palindromes.append(word)
```

------

## Pitfall（真实踩坑）

**坑1：为了"简洁"牺牲可读性**



python

```python
# ❌ 过度使用，团队成员看不懂
data = [item['value'] * 1.5 for sublist in nested_data 
        for item in sublist if item['status'] == 'active' 
        and item['priority'] > 3]
```

**教训：** 当你需要换行才能写完列表推导式时，考虑用传统循环

**坑2：混淆"一个复杂条件" vs "多个if"**



python

```python
# ✅ 可以用：一个条件，用 and 连接
[x for x in data if cond1 and cond2]

# ⚠️ 不推荐：多个 if，看起来奇怪
[x for x in data if cond1 if cond2]
```

**坑3：忘记嵌套列表推导式的语法顺序**



python

```python
# 传统循环：
for row in matrix:      # 外层
    for num in row:     # 内层
        result.append(num)

# 列表推导式（顺序相同）：
[num for row in matrix for num in row]
      ↑   ↑外层在前    ↑内层在后
```

**虽然顺序对了，但还是不推荐用！**

------

## Application（在哪里用）

**实际应用场景：**

1. **API 数据处理**：提取 JSON 响应中的特定字段



python

```python
   user_ids = [user['id'] for user in api_response['users']]
```

1. **数据清洗**：过滤无效数据



python

```python
   valid_emails = [e for e in emails if '@' in e and '.' in e]
```

1. **批量转换**：统一数据格式



python

```python
   formatted_dates = [d.strftime('%Y-%m-%d') for d in date_list]
```

1. **快速筛选**：从列表中提取符合条件的元素



python

~~~python
   high_scores = [s for s in scores if s >= 90]
```

**在后续学习中的位置：**
- Month 2（大模型应用）：处理消息历史、提取回复内容
- Month 3（RAG系统）：过滤文档、批量处理文本块
- Month 5（Agent开发）：筛选可用工具、处理执行结果

---

### 视觉闭环
```
判断是否使用列表推导式的决策树：

                    需要处理列表？
                         ↓
                      是/否
                    ↙        ↘
                 YES          NO（用其他方式）
                  ↓
            单层循环？
              ↙    ↘
           YES      NO
            ↓        ↓
        简单表达式？  用传统循环
          ↙    ↘
       YES      NO
        ↓        ↓
    简单条件？   用传统循环
      ↙    ↘
   YES      NO
    ↓        ↓
  5秒看懂？  用传统循环
    ↙  ↘
  YES   NO
   ↓     ↓
 用推导式  用传统循环
~~~

------

## 工程师记忆分层

**🗑️ 垃圾区（查文档就行）：**

- 嵌套列表推导式的具体语法顺序
- 更复杂的推导式变体（字典推导式、集合推导式）
- 多个 if 的写法（反正不推荐用）

**🔍 索引区（记关键词）：**

- 遇到"简单转换/过滤" → 考虑列表推导式
- 遇到"两层循环" → 用传统循环
- 遇到"复杂逻辑" → 用传统循环
- 遇到"需要调试" → 用传统循环（容易加 print）
- 写完后问自己"5秒能看懂吗" → 决定用不用

**💎 核心区（必须内化）：**

- **可读性 > 简洁性**（最核心的原则）
- 列表推导式 = 清晰表达意图，不是炫技
- 判断标准：4条全满足才用（单层/简单表达式/简单条件/5秒看懂）
- 当需要换行才能写完时，考虑传统循环
- and 连接的多条件可以接受，多个 if 不推荐

---

# Day 3 - 生成器入门（2026-01-07）

## 核心目标

理解生成器的惰性计算本质，建立内存效率的工程意识

------

## Why（不学会导致的工程死穴）

如果不理解生成器，你会：

- ❌ 处理大文件时内存爆炸（10GB 文件占用 10GB+ 内存）
- ❌ 程序崩溃或卡死（内存不足）
- ❌ 无法处理超大数据集（如几亿条记录）
- ❌ 写出低效的代码（占用大量不必要的内存）

**工程上的真实代价：**

- 服务器内存成本增加
- 程序响应变慢
- 无法处理大规模数据
- 用户体验差（程序卡顿）

**典型场景：**

- 读取日志文件（几GB）
- 处理数据库查询结果（百万条记录）
- 批量处理文件
- 实时数据流处理

------

## What（第一性原理 + 类比）

**生成器的本质：惰性计算（Lazy Evaluation）**

**列表 = 容器（盒子）**

- 一次性创建所有元素
- 全部存在内存里
- 立即计算
- 占用空间 = 所有元素的大小

**生成器 = 配方（食谱）**

- 不创建所有元素
- 用一个生成一个
- 按需计算
- 占用空间 = 配方大小（几百字节）

**类比：**

> **列表 = 录制好的电影**
>
> - 所有画面都已拍好
> - 存在硬盘里（占空间）
> - 可以暂停、快进、回放
>
> **生成器 = 电视直播**
>
> - 画面实时生成
> - 播完就没了
> - 只能往前看，不能回放
> - 不占存储空间

------

## How（最小可运行范式）

### **生成器的两种语法（独立，不混用）**

------

**方式1：生成器表达式（Generator Expression）**



python

```python
# 语法：圆括号 + 类似列表推导式
gen = (x ** 2 for x in range(10))

# 对比列表推导式
lst = [x ** 2 for x in range(10)]  # 列表（方括号）
gen = (x ** 2 for x in range(10))  # 生成器（圆括号）
```

**适用场景：简单的一行表达式**



python

```python
# ✅ 简单转换
squares = (x ** 2 for x in numbers)

# ✅ 简单过滤
evens = (x for x in numbers if x % 2 == 0)

# ✅ 配合聚合函数
total = sum(x ** 2 for x in range(1000000))
max_value = max(x for x in huge_list if x > 0)
```

------

**方式2：生成器函数（Generator Function）**



python

```python
# 语法：def 函数 + yield 关键字
def my_generator(n):
    for i in range(n):
        yield i ** 2

gen = my_generator(10)
```

**适用场景：复杂逻辑**



python

```python
# ✅ 读取文件
def read_errors(filename):
    with open(filename, 'r') as f:
        for line in f:
            if 'ERROR' in line:
                yield line.strip()

# ✅ 复杂算法（斐波那契）
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# ✅ 无限序列
def counter(start=0, step=1):
    current = start
    while True:
        yield current
        current += step
```

------

### **yield 的工作机制**

**yield = "暂停按钮"**



python

```python
def count_up_to(n):
    i = 0
    while i < n:
        print(f"生成 {i}")
        yield i  # ← 暂停，返回 i 给外面
        print(f"继续...")
        i += 1

gen = count_up_to(3)
print(next(gen))  # 生成 0 → 暂停 → 返回 0
print("外面做其他事")
print(next(gen))  # 继续... → 生成 1 → 暂停 → 返回 1
```

------

### **内存对比（实际测试）**



python

```python
import sys

# 列表：存储所有元素
numbers_list = [i for i in range(10000000)]
print(sys.getsizeof(numbers_list))  # 约 800MB

# 生成器：只存配方
numbers_gen = (i for i in range(10000000))
print(sys.getsizeof(numbers_gen))  # 约 120 字节

# 相差约 666 万倍！
```

------

### **使用生成器**



python

```python
# 方式1：for 循环（最常用）
for item in (x ** 2 for x in range(10)):
    print(item)

# 方式2：next() 函数（手动获取）
gen = (x for x in range(3))
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2
# print(next(gen))  # StopIteration 异常

# 方式3：转换为列表（失去内存优势）
gen = (x for x in range(10))
lst = list(gen)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

------

## Pitfall（真实踩坑）

**坑1：生成器只能遍历一次**



python

```python
gen = (x for x in range(5))
print(list(gen))  # [0, 1, 2, 3, 4]
print(list(gen))  # [] ← 空了！

# 解决：如果需要多次使用，用列表
lst = [x for x in range(5)]
print(list(lst))  # [0, 1, 2, 3, 4]
print(list(lst))  # [0, 1, 2, 3, 4] ← 还在
```

**坑2：生成器不支持索引和切片**



python

```python
gen = (x for x in range(10))
# print(gen[5])  # ❌ TypeError
# print(len(gen))  # ❌ TypeError

# 解决：转换为列表
lst = list(gen)
print(lst[5])  # 5
print(len(lst))  # 10
```

**坑3：混淆两种生成器语法**



python

```python
# ❌ 错误：以为要混合使用
# (yield x for x in range(10))  # 语法错误

# ✅ 正确：两种语法独立
# 方式1：表达式
gen1 = (x for x in range(10))

# 方式2：函数
def gen2():
    for x in range(10):
        yield x
```

**坑4：过度使用生成器**



python

```python
# ❌ 数据很小，没必要用生成器
small_data = (x for x in range(10))  # 反而更复杂

# ✅ 小数据直接用列表
small_data = [x for x in range(10)]
```

------

## Application（在哪里用）

**实际应用场景：**

**1. 处理大文件**



python

```python
def read_large_log(filename):
    with open(filename, 'r') as f:
        for line in f:
            if 'ERROR' in line:
                yield line.strip()

# 使用：内存始终只占几KB
for error in read_large_log('huge.log'):
    process(error)
```

**2. 数据库查询结果**



python

```python
def query_users(limit=None):
    results = db.query("SELECT * FROM users")
    for row in results:
        yield process_row(row)
        if limit and count >= limit:
            break
```

**3. 数据流处理（管道）**



python

```python
# 链式处理，内存效率高
numbers = range(1000000)
squares = (x ** 2 for x in numbers)
evens = (x for x in squares if x % 2 == 0)
result = sum(evens)  # 只占几百字节内存
```

**4. 生成无限序列**



python

~~~python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 取前10个
from itertools import islice
first_10 = list(islice(fibonacci(), 10))
```

**在后续学习中的位置：**
- Month 2（大模型应用）：流式输出 API 响应
- Month 3（RAG系统）：批量处理大量文档
- Month 4（Agent开发）：处理长时间运行的任务
- 所有涉及大数据处理的场景

---

### 视觉闭环
```
列表 vs 生成器内存对比：

列表（立即计算）：
┌──────────────────────────────────┐
│ [1, 4, 9, 16, 25, ..., 10000^2] │ ← 全部存储
└──────────────────────────────────┘
   内存：约 800MB

生成器（惰性计算）：
┌────────────────┐
│ Recipe:        │
│ for i in range │ ← 只存配方
│   yield i**2   │
└────────────────┘
   内存：约 120 字节

使用时：
生成 1 → 使用 → 释放
生成 4 → 使用 → 释放
生成 9 → 使用 → 释放
...（依次进行）

---

判断使用哪种生成器语法：

需要生成数据？
    ↓
能用一行表达式写出来？
  ↙              ↘
YES              NO
 ↓                ↓
生成器表达式    生成器函数
(x for x in)    def + yield
~~~

------

## 工程师记忆分层

**🗑️ 垃圾区（查文档就行）：**

- `next()` 函数的具体用法
- `itertools` 模块的各种函数
- 生成器的内部实现细节

**🔍 索引区（记关键词）：**

- 遇到"大文件处理" → 想到生成器
- 遇到"内存不够" → 想到生成器
- 遇到"只需遍历一次" → 可以用生成器
- 看到 `(...)` → 生成器表达式
- 看到 `yield` → 生成器函数
- 简单逻辑 → 生成器表达式
- 复杂逻辑 → 生成器函数

**💎 核心区（必须内化）：**

- 生成器 = 配方/食谱，不是容器
- 惰性计算：用一个生成一个，用完释放
- 内存优势：可以相差百万倍
- 两种语法独立：表达式 vs 函数（不混用）
- yield = 暂停按钮，返回值给外面
- 何时用：大数据、单次遍历、管道处理
- 何时不用：需要多次访问、随机访问、小数据

---

# Day 4 - 装饰器基础（2026-01-08）

## 核心目标

理解装饰器的本质，掌握函数式编程的核心思维

------

## Why（不学会导致的工程死穴）

如果不理解装饰器，你会：

- ❌ 写大量重复代码（每个函数都要复制粘贴计时、日志逻辑）
- ❌ 无法理解 Python 框架的核心机制（Flask 的 @app.route、Django 的 @login_required）
- ❌ 无法阅读他人的 Python 代码（装饰器在 Python 中极其常见）
- ❌ 错过 Python 最优雅的特性之一

**工程上的真实代价：**

- 代码维护成本高（修改一个地方要改 100 处）
- 代码可读性差（业务逻辑和基础设施代码混在一起）
- 无法使用主流框架的高级特性

**类比 Java：**

- 装饰器 ≈ Spring AOP（面向切面编程）
- 装饰器 ≈ 动态代理
- 但 Python 的装饰器更简洁、更优雅

------

## What（第一性原理 + 类比）

**装饰器的本质：**

> 装饰器 = 接收函数 + 返回新函数的函数

**三个前置概念：**

**1. 函数是第一类对象（First-Class Object）**

- 函数可以赋值给变量
- 函数可以作为参数传递
- 函数可以作为返回值



python

```python
def greet():
    print("Hello")

my_func = greet  # 函数赋值给变量
my_func()        # 调用变量
```

------

**2. 函数可以作为参数**



python

```python
def execute(func):
    print("准备执行...")
    func()
    print("执行完成")

execute(greet)  # 把函数作为参数传入
```

------

**3. 闭包（Closure）**

- 内层函数"记住"了外层函数的变量
- 即使外层函数执行完，变量还活着
- 每次调用外层函数，创建新的闭包



python

```python
def make_counter():
    count = 0  # ← 这个变量被"捕获"到闭包
    
    def increment():
        nonlocal count  # ← 修改外层变量
        count += 1
        return count
    
    return increment

counter1 = make_counter()  # 创建闭包1
counter2 = make_counter()  # 创建闭包2

print(counter1())  # 1 ← counter1 的 count
print(counter1())  # 2
print(counter2())  # 1 ← counter2 的 count（独立）
```

**关键点：**

- 不是"拷贝"，而是"绑定"
- 每个闭包都有自己独立的变量

------

**装饰器的结构：**



python

```python
def decorator(func):      # ← 接收原函数
    def wrapper(*args, **kwargs):  # ← 包装函数（闭包）
        # 执行前的操作
        result = func(*args, **kwargs)  # ← 调用原函数
        # 执行后的操作
        return result      # ← 返回原函数的结果
    return wrapper         # ← 返回包装函数
```

**类比理解：**

> **Java 动态代理：**
>
> 
>
> java
>
> ```java
> InvocationHandler handler = (proxy, method, args) -> {
>     System.out.println("方法执行前");
>     Object result = method.invoke(target, args);
>     System.out.println("方法执行后");
>     return result;
> };
> ```
>
> **Python 装饰器：**
>
> 
>
> python
>
> ```python
> def my_decorator(func):
>     def wrapper(*args, **kwargs):
>         print("方法执行前")
>         result = func(*args, **kwargs)
>         print("方法执行后")
>         return result
>     return wrapper
> ```

------

## How（最小可运行范式）

### **基础装饰器**



python

~~~python
def my_decorator(func):
    def wrapper():
        print("执行前")
        func()
        print("执行后")
    return wrapper

# 方式1：手动装饰
def say_hello():
    print("Hello")

say_hello = my_decorator(say_hello)
say_hello()

# 方式2：@ 语法糖（推荐）
@my_decorator
def say_hello():
    print("Hello")

say_hello()  # 自动被装饰
```

**输出：**
```
执行前
Hello
执行后
~~~

------

### **处理参数的装饰器**



python

```python
def timer(func):
    def wrapper(*args, **kwargs):  # ← 接收任意参数
        import time
        start = time.time()
        result = func(*args, **kwargs)  # ← 传递给原函数
        end = time.time()
        print(f"[{func.__name__}] 耗时: {end - start:.4f}秒")
        return result  # ← 返回原函数的结果
    return wrapper

@timer
def add(a, b):
    return a + b

@timer
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(add(3, 5))           # 8，并记录时间
print(greet("Alice"))      # Hello, Alice!，并记录时间
```

------

### **实用装饰器示例**

**1. 计时器装饰器**



python

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[{func.__name__}] 耗时: {end - start:.4f}秒")
        return result
    return wrapper

@timer
def process_data():
    time.sleep(1)
    return "完成"
```

------

**2. 日志装饰器**



python

~~~python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        print(f"参数: {args}")
        if kwargs:
            print(f"关键字参数: {kwargs}")
        
        result = func(*args, **kwargs)
        
        print(f"返回值: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)
```

**输出：**
```
调用函数: add
参数: (3, 5)
返回值: 8
~~~

------

**3. 修改返回值的装饰器**



python

```python
def double_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@double_result
def add(a, b):
    return a + b

print(add(3, 5))  # 16 (不是8)
```

------

## Pitfall（真实踩坑）

**坑1：忘记 return result**



python

```python
# ❌ 错误
def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"结果: {result}")
        # 忘记 return result

@my_decorator
def add(a, b):
    return a + b

x = add(3, 5)
print(x)  # None ← 丢失了返回值！
```

**教训：**

- 装饰器的 wrapper 必须 `return result`
- 否则原函数的返回值会丢失

------

**坑2：忘记 *args 和 **kwargs**



python

```python
# ❌ 错误
def timer(func):
    def wrapper():  # ← 不接收参数
        func()      # ← 不传递参数
    return wrapper

@timer
def add(a, b):
    return a + b

add(3, 5)  # ❌ TypeError: wrapper() takes 0 positional arguments
```

**教训：**

- 通用装饰器必须用 `*args, **kwargs`
- 才能处理任意参数的函数

------

**坑3：在装饰器里写具体函数名**



python

```python
# ❌ 错误
def logger(func):
    def wrapper(*args, **kwargs):
        result = test(*args, **kwargs)  # ← 写死了函数名
        return result

# test 在装饰器里不存在！
```

**教训：**

- 装饰器内部要用 `func`，不是具体函数名
- `func` 是传入的参数

------

**坑4：nonlocal 的误用**



python

```python
def make_counter():
    count = 0
    
    def increment():
        count += 1  # ❌ UnboundLocalError
        return count
    
    return increment
```

**正确写法：**



python

```python
def make_counter():
    count = 0
    
    def increment():
        nonlocal count  # ✅ 告诉 Python 修改外层变量
        count += 1
        return count
    
    return increment
```

------

## Application（在哪里用）

**实际应用场景：**

**1. 性能监控**



python

```python
@timer
def expensive_operation():
    # 复杂计算
    pass
```

**2. 日志记录**



python

```python
@logger
def api_call():
    # API 请求
    pass
```

**3. 权限验证（Web框架）**



python

```python
@login_required  # Flask/Django
def admin_page():
    pass
```

**4. 缓存结果**



python

```python
@cache
def get_data():
    # 查询数据库
    pass
```

**5. 重试机制**



python

~~~python
@retry(times=3)
def unstable_api():
    # 可能失败的操作
    pass
```

**在后续学习中的位置：**
- Month 2（大模型应用）：API 调用的重试装饰器
- Month 3（RAG系统）：缓存装饰器优化检索
- Month 5（Agent开发）：工具函数的日志装饰器
- Month 6（生产部署）：性能监控装饰器

---

### 视觉闭环
```
装饰器的工作流程：

原函数：
def add(a, b):
    return a + b

↓ 应用装饰器 @timer

等价于：
add = timer(add)

↓ timer 返回 wrapper

实际调用：
add(3, 5)
    ↓
wrapper(3, 5)
    ↓
    记录开始时间
    ↓
    调用原 add(3, 5) → 8
    ↓
    记录结束时间
    ↓
    打印耗时
    ↓
    返回 8

---

闭包的内存模型：

counter1 = make_counter()
counter2 = make_counter()

内存中：
┌─────────────────┐
│ counter1 闭包   │
│ count = 0 → 1   │ ← 独立的 count
└─────────────────┘

┌─────────────────┐
│ counter2 闭包   │
│ count = 0       │ ← 另一个独立的 count
└─────────────────┘
~~~

------

## 工程师记忆分层

**🗑️ 垃圾区（查文档就行）：**

- `func.__name__` 等函数属性
- `functools.wraps` 装饰器（进阶）
- 复杂的装饰器变体

**🔍 索引区（记关键词）：**

- 遇到"重复代码" → 想到装饰器
- 遇到"横切关注点"（日志、计时、缓存） → 想到装饰器
- 看到 `@xxx` → 知道是装饰器
- 想不起语法 → 查"通用装饰器模板"
- Python 框架的 `@` 语法 → 都是装饰器

**💎 核心区（必须内化）：**

- 装饰器本质：接收函数 + 返回新函数
- `@decorator` = `func = decorator(func)`
- 通用装饰器模板必须有：`*args, **kwargs, return result`
- 闭包：内层函数记住外层变量（绑定，不是拷贝）
- `nonlocal` 用于修改外层变量
- 装饰器解决的核心问题：消除重复代码
- 函数是第一类对象（可以传递、返回）

---

##Day 5 - 装饰器进阶（2026-01-09）

## 核心目标

掌握带参数的装饰器、装饰器叠加和 functools.wraps

------

## Why（不学会导致的工程死穴）

如果不掌握装饰器进阶，你会：

- ❌ 无法写出灵活可配置的装饰器（如 `@retry(times=3)`）
- ❌ 装饰器叠加时逻辑混乱（不知道执行顺序）
- ❌ 装饰后函数元数据丢失（调试困难、文档消失）
- ❌ 无法理解主流框架的装饰器用法（Flask、Django）

**工程上的真实代价：**

- 重试、权限、日志等通用功能难以复用
- 装饰器组合时出现 bug
- IDE 无法正确提示被装饰函数的信息
- 代码可维护性差

**实际场景：**



python

```python
# Flask 路由（带参数的装饰器）
@app.route('/user/<id>', methods=['GET', 'POST'])
def user_profile(id):
    pass

# Django 权限检查（装饰器叠加）
@login_required
@permission_required('admin')
def admin_panel(request):
    pass
```

------

## What（第一性原理 + 类比）

### **带参数的装饰器**

**本质：装饰器工厂**

> 带参数的装饰器实际上是一个返回装饰器的函数

**结构对比：**

**Day 4（两层）：**



python

```python
def decorator(func):           # 接收函数
    def wrapper(*args, **kwargs):  # 包装
        return func(*args, **kwargs)
    return wrapper
```

**Day 5（三层）：**



python

```python
def decorator(参数):            # 第1层：接收装饰器参数
    def inner_decorator(func):  # 第2层：接收函数
        def wrapper(*args, **kwargs):  # 第3层：包装
            # 使用参数
            return func(*args, **kwargs)
        return wrapper
    return inner_decorator
```

**关键：**



python

```python
@repeat(times=3)
def my_func():
    pass

# 等价于：
my_func = repeat(times=3)(my_func)
#         ↑第1步返回装饰器  ↑第2步应用装饰器
```

------

### **装饰器叠加**

**执行顺序：**

- **应用顺序（定义时）：从下往上**（靠近函数的先应用）
- **执行顺序（调用时）：从上往下**（最外层先执行）



python

```python
@A    ← 第2个应用，第1个执行（最外层）
@B    ← 第1个应用，第2个执行
def func():
    pass  ← 最后执行（最内层）
```

**等价于：**



python

```python
func = A(B(func))
```

------

### **functools.wraps**

**问题：** 装饰后函数元数据丢失



python

```python
def timer(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@timer
def add(a, b):
    """相加两个数"""
    return a + b

print(add.__name__)  # wrapper ← 丢失了函数名
print(add.__doc__)   # None    ← 丢失了文档
```

**解决：**



python

```python
from functools import wraps

def timer(func):
    @wraps(func)  # ← 保留原函数元数据
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@timer
def add(a, b):
    """相加两个数"""
    return a + b

print(add.__name__)  # add ✅
print(add.__doc__)   # 相加两个数 ✅
```

------

## How（最小可运行范式）

### **1. 带参数的装饰器（三层结构）**

**基础模板：**



python

```python
from functools import wraps

def my_decorator(参数):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 使用参数
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@my_decorator(参数值)
def my_function():
    pass
```

------

**实例1：重复执行**



python

```python
from functools import wraps

def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hello():
    print("Hello")

say_hello()
# 输出：
# Hello
# Hello
# Hello
```

------

**实例2：重试机制**



python

```python
from functools import wraps
import time

def retry(times=3, delay=1):
    """失败后自动重试的装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i == times - 1:  # 最后一次尝试
                        raise e
                    time.sleep(delay)  # 等待后重试
        return wrapper
    return decorator

@retry(times=3, delay=2)
def unstable_api():
    # 可能失败的 API 调用
    import random
    if random.random() < 0.7:
        raise Exception("API 失败")
    return "成功"
```

------

**实例3：日志级别**



python

```python
from functools import wraps

def log(level="INFO"):
    """带日志级别的装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{level}] 调用 {func.__name__}")
            result = func(*args, **kwargs)
            print(f"[{level}] 返回: {result}")
            return result
        return wrapper
    return decorator

@log(level="DEBUG")
def calculate(a, b):
    return a + b

@log(level="ERROR")
def risky_operation():
    pass
```

------

### **2. 装饰器叠加**

**示例：**



python

~~~python
def add_brackets(func):
    @wraps(func)
    def wrapper():
        print("[")
        func()
        print("]")
    return wrapper

def add_quotes(func):
    @wraps(func)
    def wrapper():
        print('"')
        func()
        print('"')
    return wrapper

@add_brackets
@add_quotes
def say_hello():
    print("Hello")

say_hello()
```

**输出：**
```
[
"
Hello
"
]
```

**执行流程：**
```
应用阶段（定义时）：
say_hello = add_brackets(add_quotes(say_hello))
           ↑后应用            ↑先应用

调用阶段（执行时）：
add_brackets wrapper
  → 打印 [
  → 调用 add_quotes wrapper
      → 打印 "
      → 调用 say_hello
          → 打印 Hello
      ← 返回
      → 打印 "
  ← 返回
  → 打印 ]
~~~

------

**实际应用（权限检查）：**



python

```python
@login_required       # 第3个应用，第1个执行
@role_check("admin")  # 第2个应用，第2个执行
@log                  # 第1个应用，第3个执行
def delete_user(user_id):
    # 删除用户
    pass

# 执行顺序：
# 1. 检查是否登录
# 2. 检查是否有 admin 权限
# 3. 记录日志
# 4. 执行删除操作
```

------

### **3. functools.wraps 的使用**

**标准装饰器模板（无参数）：**



python

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # ← 必须加
    def wrapper(*args, **kwargs):
        # 执行前
        result = func(*args, **kwargs)
        # 执行后
        return result
    return wrapper
```

**标准装饰器模板（带参数）：**



python

```python
from functools import wraps

def my_decorator(参数):
    def decorator(func):
        @wraps(func)  # ← 在第二层加
        def wrapper(*args, **kwargs):
            # 使用参数
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
```

**wraps 保留的信息：**

- `__name__`（函数名）
- `__doc__`（文档字符串）
- `__module__`（模块名）
- `__annotations__`（类型注解）
- `__qualname__`（限定名）

------

## Pitfall（真实踩坑）

**坑1：for 循环写错**



python

```python
# ❌ 错误
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for time in times:  # times 是数字，不能直接遍历
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# ✅ 正确
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):  # 用 range(times)
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
```

------

**坑2：return 位置错误**



python

```python
# ❌ 错误：return 在循环内
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
                return result  # 第一次循环就返回了
        return wrapper
    return decorator

# ✅ 正确：return 在循环外
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result  # 循环结束后再返回
        return wrapper
    return decorator
```

------

**坑3：忘记三层 return**



python

```python
# ❌ 错误：缺少最外层的 return
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    # 缺少 return decorator

# ✅ 正确：三层都要 return
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator  # 必须返回 decorator
```

------

**坑4：忘记 @wraps(func)**



python

```python
# ❌ 不好：元数据丢失
def timer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@timer
def add(a, b):
    """相加两个数"""
    return a + b

print(add.__name__)  # wrapper ← 错误
print(add.__doc__)   # None    ← 丢失

# ✅ 正确：加上 @wraps(func)
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper
```

------

**坑5：装饰器叠加顺序混乱**



python

```python
# 容易混淆执行顺序
@A
@B
@C
def func():
    pass

# 记住：应用从下往上，执行从上往下
# 等价于：func = A(B(C(func)))
# 执行时：A wrapper → B wrapper → C wrapper → func
```

------

## Application（在哪里用）

**实际应用场景：**

**1. API 重试机制**



python

```python
@retry(times=3, delay=2)
def call_external_api():
    # 调用可能失败的外部 API
    pass
```

**2. 权限检查**



python

```python
@login_required
@require_role("admin")
def admin_panel():
    pass
```

**3. 性能监控**



python

```python
@timer
@log(level="INFO")
def expensive_operation():
    pass
```

**4. 缓存**



python

```python
@cache(expire=3600)
def get_user_data(user_id):
    # 查询数据库
    pass
```

**5. 限流**



python

~~~python
@rate_limit(calls=100, period=60)
def api_endpoint():
    pass
```

**在后续学习中的位置：**
- Month 2（大模型应用）：API 调用的重试和日志装饰器
- Month 3（RAG系统）：缓存装饰器优化检索性能
- Month 5（Agent开发）：工具函数的权限和日志装饰器
- Month 6（生产部署）：性能监控和限流装饰器

---

### 视觉闭环
```
带参数装饰器的三层结构：

@repeat(times=3)
def my_func():
    pass

↓ 展开

my_func = repeat(times=3)(my_func)
          ↑第1步          ↑第2步

↓ 第1步：repeat(times=3)

def decorator(func):      ← 返回这个装饰器
    def wrapper(...):
        for _ in range(3):  ← 使用参数 times
            func(...)
    return wrapper

↓ 第2步：decorator(my_func)

my_func = wrapper  ← 最终结果

---

装饰器叠加执行顺序：

定义时（从下往上应用）：
@A
@B     ← 先应用
@C     ← 最先应用
def func():
    pass

等价于：func = A(B(C(func)))

调用时（从上往下执行）：
func()
 ↓
A.wrapper
 ↓
B.wrapper
 ↓
C.wrapper
 ↓
原 func

---

functools.wraps 的作用：

装饰前：
def add(a, b):
    """相加两个数"""
    return a + b

add.__name__ = "add"
add.__doc__ = "相加两个数"

↓ 装饰（没有 @wraps）

def timer(func):
    def wrapper(...):
        return func(...)
    return wrapper

add = timer(add)

add.__name__ = "wrapper" ← 丢失
add.__doc__ = None       ← 丢失

↓ 装饰（有 @wraps）

def timer(func):
    @wraps(func)  ← 复制元数据
    def wrapper(...):
        return func(...)
    return wrapper

add = timer(add)

add.__name__ = "add"     ← 保留
add.__doc__ = "相加两个数" ← 保留
~~~

------

## 工程师记忆分层

**🗑️ 垃圾区（查文档就行）：**

- `functools.wraps` 保留的所有元数据列表
- 更复杂的装饰器变体（类装饰器、装饰器类）
- 装饰器的内部实现细节

**🔍 索引区（记关键词）：**

- 遇到"需要配置的装饰器" → 想到三层结构
- 遇到"多个装饰器" → 记住"应用从下往上，执行从上往下"
- 写装饰器 → 记得加 `@wraps(func)`
- 看到 `@decorator()` 有括号 → 知道是带参数的装饰器
- 看到 `raise` → 知道是抛出异常

**💎 核心区（必须内化）：**

- 带参数装饰器 = 三层函数 + 三个 return
- 装饰器叠加：应用从下往上，执行从上往下
- `@A @B def func()` = `func = A(B(func))`
- 必须在 wrapper 上加 `@wraps(func)` 保留元数据
- `for _ in range(times)` 不是 `for time in times`
- return 在循环外面，不是循环里面
- 三层结构模板必须记住：



python

```python
  def decorator(参数):
      def inner_decorator(func):
          @wraps(func)
          def wrapper(*args, **kwargs):
              # 使用参数
              return func(*args, **kwargs)
          return wrapper
      return inner_decorator
```

------

# Day 6 - 上下文管理器（2026-01-10）

## 核心目标

理解 with 语句的原理，掌握上下文管理器的使用和编写

------

## Why（不学会导致的工程死穴）

如果不掌握上下文管理器，你会：

- ❌ 资源泄漏（文件、数据库连接、锁等没有正确释放）
- ❌ 写大量重复的 try-finally 代码
- ❌ 异常时资源无法释放（程序崩溃导致资源占用）
- ❌ 无法理解 Python 标准库和框架的核心机制

**工程上的真实代价：**

- 文件句柄泄漏 → 超过系统限制 → 程序无法打开新文件
- 数据库连接不释放 → 连接池耗尽 → 新请求无法处理
- 锁没有释放 → 死锁 → 整个系统卡死
- 代码可维护性差（资源管理逻辑分散）

**实际场景：**



python

```python
# ❌ 传统方式：容易出错
f = open('data.txt', 'r')
try:
    content = f.read()
    process(content)
finally:
    f.close()  # 必须记得写

# ✅ 上下文管理器：自动管理
with open('data.txt', 'r') as f:
    content = f.read()
    process(content)
# 自动关闭，即使发生异常
```

------

## What（第一性原理 + 类比）

### **上下文管理器的本质**

**定义：**

> 上下文管理器 = 实现了 `__enter__` 和 `__exit__` 方法的对象

**核心协议：**



python

```python
class ContextManager:
    def __enter__(self):
        # 1. 进入 with 块时调用
        # 2. 返回值赋给 as 后面的变量
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 离开 with 块时调用
        # 即使发生异常也会调用
        # exc_type: 异常类型
        # exc_val: 异常值
        # exc_tb: 异常追踪信息
        pass
```

------

### **with 语句的工作原理**

**with 语句等价于：**



python

```python
# with 语句
with obj as value:
    # with 块
    pass

# 等价于
value = obj.__enter__()
try:
    # with 块
    pass
finally:
    obj.__exit__(None, None, None)
```

**执行流程：**

1. 调用 `__enter__()` 方法
2. `__enter__()` 的返回值赋给 `as` 后的变量
3. 执行 with 块内的代码
4. 无论正常结束还是异常，都调用 `__exit__()`

------

### **类比理解**

**类比 Java 的 try-with-resources：**

**Java (JDK 7+)：**



java

```java
try (FileReader fr = new FileReader("file.txt")) {
    // 使用 fr
} // 自动调用 fr.close()
```

**Python：**



python

```python
with open('file.txt', 'r') as f:
    # 使用 f
# 自动调用 f.close()
```

**本质一样：**

- Java：实现 `AutoCloseable` 接口
- Python：实现 `__enter__` 和 `__exit__` 方法

------

## How（最小可运行范式）

### **1. 使用内置的上下文管理器**

**文件操作：**



python

```python
# ❌ 传统方式
f = open('data.txt', 'r')
content = f.read()
f.close()

# ✅ 上下文管理器
with open('data.txt', 'r') as f:
    content = f.read()
# 自动关闭
```

------

### **2. 自己写上下文管理器（类方式）**

**基础模板：**



python

```python
class MyContextManager:
    def __init__(self, params):
        # 初始化参数
        self.params = params
        
    def __enter__(self):
        # 进入 with 块时执行
        # 获取资源、初始化状态
        print("进入 with 块")
        return self  # 返回值给 as 变量
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 离开 with 块时执行
        # 释放资源、清理状态
        print("离开 with 块")
        
        # 处理异常（可选）
        if exc_type is not None:
            print(f"发生异常: {exc_type.__name__}")
        
        # return True: 抑制异常
        # return False/None: 异常继续传播
        return False

# 使用
with MyContextManager(params) as obj:
    # with 块
    pass
```

------

**实例1：计时器**



python

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        print("开始计时")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print(f"耗时: {self.end - self.start:.4f}秒")

# 使用
with Timer() as t:
    time.sleep(1)
    print("执行任务")

# 输出：
# 开始计时
# 执行任务
# 耗时: 1.0012秒
```

------

**实例2：数据库连接管理**



python

```python
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        print(f"连接数据库: {self.db_name}")
        # 实际项目中这里会真正连接数据库
        self.connection = f"<连接到 {self.db_name}>"
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"关闭数据库: {self.db_name}")
        # 实际项目中这里会关闭连接
        self.connection = None

# 使用
with DatabaseConnection("user_db") as conn:
    print(f"使用连接: {conn}")
    print("执行查询...")

# 输出：
# 连接数据库: user_db
# 使用连接: <连接到 user_db>
# 执行查询...
# 关闭数据库: user_db
```

------

**实例3：切换目录**



python

```python
import os

class ChangeDirectory:
    def __init__(self, path):
        self.path = path
        self.current_path = None
        
    def __enter__(self):
        # 进入 with 块时才保存当前目录
        self.current_path = os.getcwd()
        os.chdir(self.path)
        print(f"切换到: {self.path}")
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 恢复原目录
        os.chdir(self.current_path)
        print(f"恢复到: {self.current_path}")

# 使用
print(f"原目录: {os.getcwd()}")
with ChangeDirectory('/tmp'):
    print(f"当前目录: {os.getcwd()}")

print(f"恢复后: {os.getcwd()}")
```

------

### **3. 用 @contextmanager 装饰器（更简洁）**

**需要导入：**



python

```python
from contextlib import contextmanager
```

**基础模板：**



python

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    # __enter__ 部分：进入 with 块前执行
    print("准备资源")
    
    try:
        yield  # ← 暂停点，with 块在这里执行
    finally:
        # __exit__ 部分：离开 with 块后执行
        print("清理资源")

# 使用
with my_context():
    print("使用资源")

# 输出：
# 准备资源
# 使用资源
# 清理资源
```

------

**@contextmanager 里 yield 的特殊用法：**

**Day 3 的生成器 yield（返回值）：**



python

```python
def count():
    yield 1  # 返回 1
    yield 2  # 返回 2

for x in count():
    print(x)  # 1, 2
```

**@contextmanager 的 yield（暂停点）：**



python

```python
@contextmanager
def my_context():
    print("进入")
    yield "可选的值"  # 暂停，返回值给 as
    print("退出")

with my_context() as value:
    print(value)  # 可选的值

# 输出：
# 进入
# 可选的值
# 退出
```

**关键区别：**

- 生成器 yield：可以多次 yield，每次返回一个值
- @contextmanager yield：只能 yield 一次，标记 with 块位置
  - yield 前 = `__enter__`
  - yield 时 = 执行 with 块
  - yield 后 = `__exit__`

------

**实例1：切换目录（@contextmanager 版本）**



python

```python
from contextlib import contextmanager
import os

@contextmanager
def change_directory(path):
    # yield 前 = __enter__
    current_path = os.getcwd()
    os.chdir(path)
    
    try:
        yield  # with 块在这里执行
    finally:
        # yield 后 = __exit__
        os.chdir(current_path)

# 使用（和类方式完全一样）
with change_directory('/tmp'):
    print(os.getcwd())  # /tmp
```

------

**实例2：临时修改环境变量**



python

```python
from contextlib import contextmanager
import os

@contextmanager
def temp_env(key, value):
    old_value = os.environ.get(key)
    os.environ[key] = value
    
    try:
        yield
    finally:
        if old_value is None:
            del os.environ[key]
        else:
            os.environ[key] = old_value

# 使用
with temp_env('DEBUG', 'true'):
    print(os.environ['DEBUG'])  # true
```

------

**实例3：抑制特定异常**



python

```python
from contextlib import contextmanager

@contextmanager
def suppress_exception(exc_type):
    try:
        yield
    except exc_type:
        pass  # 忽略异常

# 使用
with suppress_exception(ValueError):
    int('abc')  # ValueError 被抑制
    print("这行不会执行")

print("程序继续运行")
```

------

### **4. 异常处理**

**`__exit__` 的参数含义：**



python

```python
def __exit__(self, exc_type, exc_val, exc_tb):
    # exc_type: 异常类型（如 ValueError）
    # exc_val: 异常实例
    # exc_tb: 异常追踪信息
    
    if exc_type is None:
        # 正常退出，没有异常
        print("正常结束")
    else:
        # 有异常发生
        print(f"异常: {exc_type.__name__}: {exc_val}")
    
    # return True: 抑制异常（不向外传播）
    # return False/None: 异常继续传播
    return False
```

------

**示例：异常处理**



python

```python
class SafeOperation:
    def __enter__(self):
        print("开始操作")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"出错了: {exc_val}")
            return True  # 抑制异常
        print("操作成功")
        return False

# 使用
with SafeOperation():
    print("执行中...")
    raise ValueError("测试异常")
    print("这行不会执行")

print("程序继续运行")  # 因为异常被抑制了

# 输出：
# 开始操作
# 执行中...
# 出错了: 测试异常
# 程序继续运行
```

------

## Pitfall（真实踩坑）

**坑1：在 \**init\** 里获取状态**



python

```python
# ❌ 不好：过早获取状态
class ChangeDirectory:
    def __init__(self, path):
        self.path = path
        self.current_path = os.getcwd()  # 在 __init__ 时获取
        
    def __enter__(self):
        os.chdir(self.path)

# 问题：如果在创建对象和使用 with 之间目录变了，就不准了

# ✅ 正确：在 __enter__ 时获取
class ChangeDirectory:
    def __init__(self, path):
        self.path = path
        self.current_path = None
        
    def __enter__(self):
        self.current_path = os.getcwd()  # 进入时才获取
        os.chdir(self.path)
```

------

**坑2：忘记在 \**exit\** 里清理资源**



python

```python
# ❌ 错误：没有清理
class FileHandler:
    def __enter__(self):
        self.file = open('data.txt', 'r')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass  # 忘记关闭文件！

# ✅ 正确：必须清理
class FileHandler:
    def __enter__(self):
        self.file = open('data.txt', 'r')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()  # 确保关闭
```

------

**坑3：@contextmanager 缺少 try-finally**



python

```python
# ❌ 危险：异常时不会执行清理
@contextmanager
def my_context():
    setup()
    yield
    cleanup()  # 如果 with 块抛异常，这行不会执行

# ✅ 正确：用 try-finally 保证清理
@contextmanager
def my_context():
    setup()
    try:
        yield
    finally:
        cleanup()  # 一定会执行
```

------

**坑4：混淆 yield 的用法**



python

```python
# ❌ 错误理解：以为可以多次 yield
@contextmanager
def wrong():
    yield 1
    yield 2  # ← 错误！@contextmanager 只能 yield 一次

# ✅ 正确：只 yield 一次
@contextmanager
def correct():
    yield "value"  # 只有一个 yield
```

------

**坑5：return True 抑制所有异常**



python

```python
# ❌ 危险：抑制了所有异常
class BadContext:
    def __exit__(self, exc_type, exc_val, exc_tb):
        return True  # 所有异常都被吞掉

# ✅ 正确：只抑制特定异常
class GoodContext:
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is ValueError:
            return True  # 只抑制 ValueError
        return False  # 其他异常继续传播
```

------

## Application（在哪里用）

**实际应用场景：**

**1. 文件和 I/O 操作**



python

```python
# 文件
with open('data.txt', 'r') as f:
    data = f.read()

# 网络连接
with socket.socket() as s:
    s.connect(('localhost', 8080))
```

**2. 数据库操作**



python

```python
# 数据库连接
with db.connect() as conn:
    conn.execute("SELECT * FROM users")

# 事务管理
with db.transaction():
    db.insert(...)
    db.update(...)
# 自动提交或回滚
```

**3. 锁和同步**



python

```python
# 线程锁
with lock:
    critical_section()

# 信号量
with semaphore:
    limited_resource()
```

**4. 临时状态管理**



python

```python
# 临时切换目录
with change_directory('/tmp'):
    process_files()

# 临时修改配置
with temp_config(debug=True):
    run_tests()
```

**5. 资源计量**



python

~~~python
# 计时
with Timer():
    expensive_operation()

# 内存监控
with MemoryProfiler():
    memory_intensive_task()
```

**在后续学习中的位置：**
- Month 2（大模型应用）：API 连接管理
- Month 3（RAG系统）：向量数据库连接管理
- Month 5（Agent开发）：工具资源管理
- Month 6（生产部署）：数据库事务、锁管理

---

### 视觉闭环
```
with 语句的执行流程：

with obj as value:
    # with 块
    pass

↓ 展开

1. value = obj.__enter__()
   ↓
2. try:
       # with 块
   ↓
3. finally:
       obj.__exit__(exc_type, exc_val, exc_tb)

---

类方式 vs @contextmanager：

类方式：
class MyContext:
    def __enter__(self):    ← 进入时
        setup()
        return value
        
    def __exit__(self, ...): ← 退出时
        cleanup()

@contextmanager 方式：
@contextmanager
def my_context():
    setup()           ← __enter__ 部分
    try:
        yield value   ← with 块
    finally:
        cleanup()     ← __exit__ 部分

---

@contextmanager 的 yield 执行流程：

@contextmanager
def my_context():
    print("1. 准备")
    yield "value"
    print("3. 清理")

with my_context() as v:
    print("2. 使用")

执行顺序：
1. 准备 → yield 暂停
2. 使用 → with 块执行
3. 清理 → yield 之后继续

---

异常处理流程：

with 块正常：
__enter__() → with 块 → __exit__(None, None, None)

with 块异常：
__enter__() → with 块异常 → __exit__(exc_type, exc_val, exc_tb)
                                  ↓
                          return True → 抑制异常
                          return False → 异常传播
~~~

------

## 工程师记忆分层

**🗑️ 垃圾区（查文档就行）：**

- `__exit__` 参数的详细含义
- contextlib 模块的其他工具（suppress、closing等）
- 更复杂的上下文管理器变体

**🔍 索引区（记关键词）：**

- 遇到"需要自动清理资源" → 想到上下文管理器
- 写了 open/connect/acquire → 考虑用 with
- 需要 try-finally → 考虑改成上下文管理器
- 看到重复的获取/释放代码 → 封装成上下文管理器
- 简单场景 → 用 @contextmanager
- 复杂场景 → 用类方式

**💎 核心区（必须内化）：**

- 上下文管理器 = `__enter__` + `__exit__`
- with 语句自动调用这两个方法
- `__enter__` 返回值 → 给 as 变量
- `__exit__` 一定会执行（即使异常）
- @contextmanager 的 yield 是暂停点，不是返回值
  - yield 前 = `__enter__`
  - yield 后 = `__exit__`
  - 必须用 try-finally 包裹 yield
- return True 抑制异常，return False 传播异常
- 在 `__enter__` 里获取状态，不是 `__init__`
- 类方式 vs @contextmanager：
  - 简单 → @contextmanager
  - 需要保存状态 → 类方式

---

# Day 7 - 异步编程入门（2026-01-11）

## 核心目标

理解异步编程的概念，掌握 async/await 基础语法

------

## Why（不学会导致的工程死穴）

如果不掌握异步编程，你会：

- ❌ I/O 密集型任务效率极低（串行等待，浪费大量时间）
- ❌ 无法处理高并发场景（每个请求都阻塞）
- ❌ 无法理解现代 Python 框架（FastAPI、aiohttp 等都基于异步）
- ❌ 在 AI 应用开发中遇到瓶颈（调用大模型 API 必须用异步）

**工程上的真实代价：**

- API 调用串行执行 → 10 个请求需要 10 秒，而不是 1 秒
- 数据库查询阻塞 → 无法处理多个用户请求
- 文件批量处理效率低 → 处理 100 个文件需要几小时
- 系统吞吐量低 → 无法支撑生产环境

**实际场景：**



python

~~~python
# ❌ 同步方式：调用 10 个 API
for i in range(10):
    result = requests.get(api_url)
# 总耗时：10 × 1秒 = 10秒

# ✅ 异步方式：并行调用
results = await asyncio.gather(*[
    fetch_api(url) for url in urls
])
# 总耗时：约 1 秒
```

---

### What（第一性原理 + 类比）

#### **同步 vs 异步**

**同步（Synchronous）：**
> 一件一件做，做完一件再做下一件

**类比：**
```
烧水（5分钟）→ 等水烧开 → 洗菜（3分钟）→ 切菜（2分钟）
总耗时：10 分钟
```

**异步（Asynchronous）：**
> 等待时可以做其他事，多件事同时进行

**类比：**
```
开始烧水 → 等水烧的时候去洗菜 → 再切菜
总耗时：5 分钟（烧水时间）
~~~

------

### **什么任务适合异步？**

**I/O 密集型任务（适合异步）：**

- 网络请求（API 调用、下载文件）
- 文件读写（读取大文件）
- 数据库查询
- 等待用户输入

**特点：**

- CPU 大部分时间在等待外部响应
- 等待时 CPU 闲置
- 可以利用等待时间做其他事

------

**CPU 密集型任务（不适合异步）：**

- 大量计算（如计算 1+2+3+...+1000000）
- 图像处理
- 数据分析

**特点：**

- CPU 一直在工作
- 没有等待时间
- 异步帮不上忙（需要多进程）

------

### **Python 异步编程的核心概念**

**1. 协程（Coroutine）**



python

```python
async def my_function():
    # 这是一个协程
    pass
```

- 用 `async def` 定义的函数
- 可以暂停和恢复执行
- 是异步编程的基础单元

------

**2. async 关键字**



python

```python
async def download_file():
    # 异步函数
    pass
```

**作用：** 定义异步函数（协程）

------

**3. await 关键字**



python

```python
result = await some_async_function()
```

**两个核心作用：**

**作用1：让异步函数真正执行，并获取结果**



python

```python
# ❌ 没有 await：函数不会执行
async def main():
    task()  # 只是创建协程对象，不执行

# ✅ 有 await：函数会执行
async def main():
    await task()  # 真正执行
```

**作用2：等待时释放控制权（让其他任务执行）**



python

```python
async def task1():
    print("任务1开始")
    await asyncio.sleep(2)  # 等待时，切换到其他任务
    print("任务1结束")

async def task2():
    print("任务2开始")
    await asyncio.sleep(2)
    print("任务2结束")

# 并行执行：任务1等待时，任务2可以执行
await asyncio.gather(task1(), task2())
```

**关键理解：**

- await 不是"傻等"
- await 是"我在等待，但我去做别的事"
- 这是异步能并行的原因

------

**4. asyncio.run()**



python

```python
asyncio.run(main())
```

**作用：** 启动异步程序的入口点

------

### **为什么需要多层 await？**

**规则：**

> async 函数调用 async 函数，必须用 await

**原因：**

1. async 函数不会自动执行
2. 没有 await，只是创建协程对象
3. 有 await，协程才会真正执行

**例子：**



python

~~~python
async def level3():
    await asyncio.sleep(1)  # ← 异步操作需要 await

async def level2():
    await level3()  # ← 调用 async 函数需要 await

async def level1():
    await level2()  # ← 调用 async 函数需要 await

asyncio.run(level1())  # ← 启动入口
```

**调用链：**
```
asyncio.run → await level1 → await level2 → await level3 → await sleep
~~~

每一层都需要 await，就像传递接力棒。

------

### **即使不需要返回值，也必须 await**

**错误理解：**

> "我的异步函数只是下载文件，不返回值，不需要 await"

**正确理解：**

> "调用 async 函数必须 await，和是否需要返回值无关"

**例子：**



python

```python
async def download_file(url, filename):
    print(f"开始下载 {filename}")
    await asyncio.sleep(2)  # 模拟下载
    with open(filename, 'w') as f:
        f.write("内容")
    print(f"{filename} 下载完成")
    # 没有 return

async def main():
    # ❌ 错误：文件不会被下载
    download_file("url", "file.txt")
    
    # ✅ 正确：文件会被下载
    await download_file("url", "file.txt")

asyncio.run(main())
```

**原因：**

- 不用 await → async 函数不会执行
- 用 await → 函数执行，且可以并行

------

## How（最小可运行范式）

### **1. 基础异步函数**



python

~~~python
import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# 运行
asyncio.run(hello())
```

**输出：**
```
Hello
World    ← 1秒后
~~~

------

### **2. 并行执行多个任务**

**串行执行（慢）：**



python

~~~python
import asyncio

async def task(name, seconds):
    print(f"{name} 开始")
    await asyncio.sleep(seconds)
    print(f"{name} 结束")

async def main():
    await task("任务1", 2)
    await task("任务2", 2)

asyncio.run(main())
# 总耗时：4秒
```

**输出：**
```
任务1 开始
任务1 结束    ← 2秒后
任务2 开始
任务2 结束    ← 再过2秒
~~~

------

**并行执行（快）：**



python

~~~python
import asyncio

async def task(name, seconds):
    print(f"{name} 开始")
    await asyncio.sleep(seconds)
    print(f"{name} 结束")
    return f"{name} 完成"

async def main():
    # asyncio.gather 并行执行
    results = await asyncio.gather(
        task("任务1", 2),
        task("任务2", 2),
        task("任务3", 2)
    )
    print(f"结果: {results}")

asyncio.run(main())
# 总耗时：2秒
```

**输出：**
```
任务1 开始
任务2 开始
任务3 开始
任务1 结束    ← 2秒后（几乎同时）
任务2 结束
任务3 结束
结果: ['任务1 完成', '任务2 完成', '任务3 完成']
~~~

------

### **3. 实际应用：并发 API 请求**



python

```python
import asyncio
import aiohttp  # 异步 HTTP 库

async def fetch_url(session, url):
    async with session.get(url) as response:
        data = await response.text()
        return len(data)

async def main():
    urls = [
        "https://api1.com/data",
        "https://api2.com/data",
        "https://api3.com/data"
    ]
    
    async with aiohttp.ClientSession() as session:
        # 并行请求所有 URL
        results = await asyncio.gather(
            *[fetch_url(session, url) for url in urls]
        )
    
    print(f"获取了 {len(results)} 个结果")
    print(f"数据大小: {results}")

asyncio.run(main())
```

**优势：**

- 3 个请求并行执行
- 总耗时 ≈ 最慢的那个请求
- 而不是 3 个请求时间相加

------

### **4. 批量下载文件（不需要返回值）**



python

~~~python
import asyncio

async def download_file(url, filename):
    print(f"开始下载 {filename}")
    await asyncio.sleep(2)  # 模拟下载耗时
    
    # 保存文件
    with open(filename, 'w') as f:
        f.write(f"从 {url} 下载的内容")
    
    print(f"{filename} 下载完成")
    # 没有 return

async def main():
    files = [
        ("http://url1.com", "file1.txt"),
        ("http://url2.com", "file2.txt"),
        ("http://url3.com", "file3.txt")
    ]
    
    # 并行下载（即使不需要返回值，也要 await）
    await asyncio.gather(
        *[download_file(url, name) for url, name in files]
    )
    
    print("全部下载完成")

asyncio.run(main())
```

**输出：**
```
开始下载 file1.txt
开始下载 file2.txt
开始下载 file3.txt
file1.txt 下载完成    ← 2秒后
file2.txt 下载完成
file3.txt 下载完成
全部下载完成

总耗时：2秒（而不是6秒）
~~~

------

### **5. 常用 asyncio 工具**

**asyncio.gather() - 并行执行多个任务**



python

```python
# 同时执行多个任务，等待全部完成
results = await asyncio.gather(
    task1(),
    task2(),
    task3()
)
# results = [task1结果, task2结果, task3结果]
```

------

**asyncio.create_task() - 创建后台任务**



python

```python
async def background_task():
    await asyncio.sleep(5)
    print("后台任务完成")

async def main():
    # 创建后台任务（不立即等待）
    task = asyncio.create_task(background_task())
    
    print("做其他事")
    await asyncio.sleep(1)
    
    # 等待后台任务完成
    await task

asyncio.run(main())
```

------

**asyncio.wait_for() - 设置超时**



python

```python
async def slow_operation():
    await asyncio.sleep(10)
    return "完成"

async def main():
    try:
        # 最多等 3 秒
        result = await asyncio.wait_for(
            slow_operation(), 
            timeout=3
        )
    except asyncio.TimeoutError:
        print("操作超时")

asyncio.run(main())
```

------

## Pitfall（真实踩坑）

**坑1：忘记 await**



python

```python
# ❌ 错误：async 函数不会执行
async def main():
    download_file("url", "file.txt")  # 缺少 await
    print("结束")

asyncio.run(main())

# 输出：
# 结束
# （文件没有下载）

# ✅ 正确：必须 await
async def main():
    await download_file("url", "file.txt")
    print("结束")
```

------

**坑2：在非 async 函数里用 await**



python

```python
# ❌ 错误：await 只能在 async 函数里使用
def my_function():
    await asyncio.sleep(1)  # SyntaxError

# ✅ 正确：必须是 async 函数
async def my_function():
    await asyncio.sleep(1)
```

------

**坑3：混用同步和异步**



python

```python
# ❌ 错误：在异步函数里用同步 sleep
import time

async def task():
    time.sleep(2)  # 阻塞！其他任务也无法执行

# ✅ 正确：用异步 sleep
async def task():
    await asyncio.sleep(2)  # 不阻塞，其他任务可以执行
```

------

**坑4：忘记 asyncio.run()**



python

```python
# ❌ 错误：直接调用异步函数
async def main():
    print("Hello")

main()  # 返回协程对象，不会执行

# ✅ 正确：用 asyncio.run() 启动
asyncio.run(main())
```

------

**坑5：以为不需要返回值就不需要 await**



python

```python
# ❌ 错误理解
async def save_data(data):
    # 保存数据，不返回值
    pass

async def main():
    # "不需要返回值，所以不用 await"（错误！）
    save_data(data)  # 函数不会执行

# ✅ 正确：即使不需要返回值，也必须 await
async def main():
    await save_data(data)  # 函数会执行
```

------

## Application（在哪里用）

**实际应用场景：**

**1. 大模型 API 批量调用**



python

```python
async def call_llm(prompt):
    # 调用 Claude/GPT API
    response = await client.messages.create(...)
    return response

# 批量调用
prompts = ["问题1", "问题2", "问题3"]
results = await asyncio.gather(
    *[call_llm(p) for p in prompts]
)
```

**2. RAG 系统的并行检索**



python

```python
async def search_vector_db(query):
    # 搜索向量数据库
    pass

async def search_web(query):
    # 搜索网络
    pass

# 并行搜索多个数据源
results = await asyncio.gather(
    search_vector_db(query),
    search_web(query)
)
```

**3. 批量数据处理**



python

```python
# 批量处理用户数据
user_ids = [1, 2, 3, ..., 100]
results = await asyncio.gather(
    *[process_user(uid) for uid in user_ids]
)
```

**4. Web 爬虫**



python

~~~python
# 并发爬取多个页面
urls = [url1, url2, url3, ...]
pages = await asyncio.gather(
    *[fetch_page(url) for url in urls]
)
```

**在后续学习中的位置：**
- Month 2（大模型应用）：异步调用大模型 API
- Month 3（RAG系统）：并行检索多个数据源
- Month 5（Agent开发）：Agent 并发执行多个工具
- Month 6（生产部署）：FastAPI 异步接口开发

---

### 视觉闭环
```
同步 vs 异步执行对比：

同步执行（串行）：
任务1 ████████ (2秒)
              任务2 ████████ (2秒)
                            任务3 ████████ (2秒)
总耗时：6秒

异步执行（并行）：
任务1 ████████ (2秒)
任务2 ████████ (2秒)
任务3 ████████ (2秒)
总耗时：2秒

---

await 的执行流程：

async def task1():
    print("A")
    await asyncio.sleep(1)  ← 暂停，释放控制权
    print("B")

async def task2():
    print("C")
    await asyncio.sleep(1)  ← 暂停，释放控制权
    print("D")

await asyncio.gather(task1(), task2())

执行顺序：
A → C → (等待1秒) → B → D

---

调用链中的 await：

asyncio.run(level1())
    ↓
async def level1():
    await level2()  ← 必须 await
        ↓
    async def level2():
        await level3()  ← 必须 await
            ↓
        async def level3():
            await asyncio.sleep(1)  ← 必须 await

每一层都需要 await，否则不会执行

---

即使不需要返回值也要 await：

async def download(url):
    # 下载文件，不返回值
    pass

# ❌ 错误：不会下载
download(url)

# ✅ 正确：会下载
await download(url)

# ✅ 并行下载
await asyncio.gather(
    download(url1),
    download(url2)
)
~~~

------

### 工程师记忆分层

**🗑️ 垃圾区（查文档就行）：**

- asyncio 模块的所有方法
- 各种异步库的具体用法
- 异步上下文管理器的详细实现
- 异步生成器的高级用法

**🔍 索引区（记关键词）：**

- 遇到"多个 I/O 操作" → 想到异步
- 遇到"API 批量调用" → 想到 asyncio.gather
- 遇到"并发" → 想到异步
- 需要超时控制 → 想到 asyncio.wait_for
- 后台任务 → 想到 asyncio.create_task
- 看到 async def → 知道是异步函数
- 调用 async 函数 → 记得用 await

**💎 核心区（必须内化）：**

- 异步适合 I/O 密集型任务，不适合 CPU 密集型

- `async def` 定义异步函数（协程）

- ```
  await
  ```

   有两个作用：

  1. 让异步函数执行并获取结果
  2. 等待时释放控制权，让其他任务执行

- 调用 async 函数必须用 await（无论是否需要返回值）

- 在非 async 函数里不能用 await

- `asyncio.run()` 是异步程序入口

- `asyncio.gather()` 并行执行多个任务

- 同步代码（time.sleep）会阻塞，异步代码（asyncio.sleep）不会

- 多层 async 函数调用，每层都需要 await

- await 不是"傻等"，而是"等待时做其他事"

---

# M1-W2-D1: 组合优于继承

**Phase**: Month 1 - Python 工程基石
 **今日核心目标**: 理解并实现可替换的 Client（Real/Mock）+ Service 依赖接口

------

## Why：不学会导致的工程死穴

假设你用 `if debug:` 来区分测试和生产环境：

```python
class UserService:
    def get_user(self, user_id):
        if self.debug:
            return {"name": "测试用户"}
        else:
            return requests.get(...).json()
```

**三个死穴**：

| 问题   | 后果                                                        |
| ------ | ----------------------------------------------------------- |
| 多环境 | `if debug elif staging elif prod...` 越来越长               |
| 多方法 | 每个方法都要写同样的判断逻辑                                |
| 多场景 | 超时、报错、慢响应... 每种都加 flag，业务代码被测试逻辑污染 |

------

## What：第一性原理 + 类比

**核心思想**：Service 不关心具体是哪个环境，只依赖一个接口（约定），想换行为就换实现类，Service 代码不用动。

**类比**：

- **继承** = 儿子继承父亲的姓，生下来就定了，改不了
- **组合** = 你有一部手机，可以随时换成另一部

**继承的问题**：2 个依赖 × 2 种实现 = 4 个子类；3 个依赖 × 2 种实现 = 8 个子类（爆炸增长）

**组合的优势**：1 个 Service 类 + 随意搭配实现类

------

## How：最小可运行范式

### 三种角色

| 角色   | 写法                                | 作用     |
| ------ | ----------------------------------- | -------- |
| 接口类 | `class X(Protocol):` + 只有方法签名 | 定义约定 |
| 实现类 | `class X:` + 有具体实现             | 实现约定 |
| 业务类 | `class X:` + 依赖接口类型           | 使用约定 |

### 完整代码

```python
from typing import Protocol

# 1. 定义接口（约定）
class UserClient(Protocol):
    def fetch_user(self, user_id: str) -> dict: ...

# 2. 实现类（具体实现）
class RealClient:
    def fetch_user(self, user_id: str) -> dict:
        return {"id": user_id, "name": "真实用户", "source": "api"}

class MockClient:
    def fetch_user(self, user_id: str) -> dict:
        return {"id": user_id, "name": "模拟用户", "source": "mock"}

# 3. 业务类（依赖接口）
class UserService:
    def __init__(self, client: UserClient):
        self.client = client

    def get_user(self, user_id: str) -> dict:
        return self.client.fetch_user(user_id)

# 4. 使用：换行为只需换实现类
mock_client = MockClient()
service = UserService(mock_client)
print(service.get_user("123"))  # {'id': '123', 'name': '模拟用户', 'source': 'mock'}

real_client = RealClient()
service = UserService(real_client)
print(service.get_user("123"))  # {'id': '123', 'name': '真实用户', 'source': 'api'}
```

------

## Pitfall：真实踩坑

### 1. Protocol 用错位置

```python
# ❌ 错误：实现类不需要写 Protocol
class RealClient(Protocol):
    def fetch_user(self, user_id: str) -> dict:
        return {...}

# ✅ 正确：只有接口定义才用 Protocol
class UserClient(Protocol):
    def fetch_user(self, user_id: str) -> dict: ...

class RealClient:  # 不需要 Protocol
    def fetch_user(self, user_id: str) -> dict:
        return {...}
```

### 2. 接口方法漏写 self

```python
# ❌ 错误
class UserClient(Protocol):
    def fetch_user(user_id: str) -> dict: ...

# ✅ 正确
class UserClient(Protocol):
    def fetch_user(self, user_id: str) -> dict: ...
```

### 3. 实例化接口而非实现类

```python
# ❌ 错误：接口不能实例化
mock_client = UserClient(MockClient)

# ✅ 正确：实例化具体实现类
mock_client = MockClient()
```

------

## Application：在 RAG/Agent/架构中的位置

| 场景           | 应用                                                         |
| -------------- | ------------------------------------------------------------ |
| **LLMClient**  | 定义 `LLMProvider` 接口，实现 `OpenAIProvider` / `OllamaProvider` / `MockProvider`，可随时切换 |
| **RAG 检索**   | 定义 `Retriever` 接口，实现 `VectorRetriever` / `BM25Retriever` / `HybridRetriever` |
| **Agent 工具** | 定义 `Tool` 接口，实现 `SearchTool` / `CalculatorTool` / `MockTool` |
| **测试**       | 用 `MockClient` 替换真实 API，不花钱、不依赖网络、可模拟各种异常场景 |

------

## 视觉闭环

```
┌─────────────────────────────────────────────────────┐
│                    UserService                       │
│                  (业务类)                            │
│                       │                              │
│                       │ 依赖                         │
│                       ▼                              │
│              ┌─────────────────┐                     │
│              │   UserClient    │                     │
│              │    (接口)       │                     │
│              └─────────────────┘                     │
│                       △                              │
│          ┌───────────┴───────────┐                  │
│          │                       │                  │
│   ┌──────┴──────┐         ┌──────┴──────┐          │
│   │ RealClient  │         │ MockClient  │          │
│   │  (实现类)    │         │  (实现类)    │          │
│   └─────────────┘         └─────────────┘          │
└─────────────────────────────────────────────────────┘

关键：UserService 只认识 UserClient 接口
      不关心具体是 Real 还是 Mock
      换实现类 = 换一行代码
```

------

## 工程师记忆分层

### 🗑️ 垃圾区（查文档）

- `Protocol` 的具体导入路径（`from typing import Protocol`）
- 各种类型注解的写法细节

### 🔍 索引区（记关键词）

- Python 用 `Protocol` 定义接口
- 鸭子类型：有方法就算符合接口，不需要显式声明

### 💎 核心区（必须内化）

- **组合优于继承**：依赖接口，不依赖具体实现
- **换行为只需换实现类**：Service 代码不用动
- **三种角色**：接口类（Protocol）、实现类、业务类
- **判断标准**：只有方法签名 → 接口；有具体实现 → 普通类

------

## 今日产出

- 文件：`projects/week2-skeleton/M1w2d1/demo.py`
- 提交：`git commit -m "M1-W2-D1: 组合优于继承"`

---

# M1-W2-D2: Type Hints + dataclass

> **Phase**: Month 1 - Python 工程基石 **今日核心目标**: 让代码"自解释"——参数类型明确、数据结构有保障

------

## Why：不学会导致的工程死穴

### 死穴 1：接口靠猜

```python
def get_user(self, user_id):  # user_id 是 str？int？都不知道
    ...
```

同事要用你的代码，只能：看变量名猜 → 看注释（如果有）→ 跑挂了再改

### 死穴 2：字典拼错运行时才爆

```python
user = {"id": "123", "name": "张三", "email": "a@b.com"}
print(user["nme"])  # 拼错了，IDE 不标红，运行时 KeyError
```

### 死穴 3：重构地狱

没有类型，改一个函数签名，不知道会影响哪些调用方。只能全局搜索 + 祈祷。

------

## What：第一性原理

### Type Hints = 代码里的文档

```python
def get_user(self, user_id: str) -> User:
```

一行签名告诉你：传什么、返回什么。不用看实现，不用猜。

### dataclass = 带字段约束的字典

```python
@dataclass
class User:
    id: str
    name: str
    email: str
```

本质：用类的字段代替字典的 key，让 IDE 能帮你检查拼写。

### 类比

| 概念       | 类比                                       |
| ---------- | ------------------------------------------ |
| Type Hints | 函数的"说明书"，告诉调用方怎么用           |
| dataclass  | 结构化的"表格"，每列有固定名字和类型       |
| dict       | 自由的"便签纸"，写什么都行，但没人帮你检查 |

------

## How：最小可运行范式

### 1. dataclass 定义数据结构

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: str
    name: str
    email: str
    age: Optional[int] = None  # 可选字段放后面，给默认值
```

### 2. Protocol 定义接口签名

```python
from typing import Protocol

class UserClient(Protocol):
    def get_user(self, user_id: str) -> User: ...
```

### 3. 实现类遵循签名

```python
class MockUserClient:
    def get_user(self, user_id: str) -> User:
        return User("123", "张三", "a@b.com", age=25)
```

### 4. 业务类标注依赖类型

```python
class UserService:
    def __init__(self, client: UserClient):
        self.client = client
    
    def get_user(self, user_id: str) -> User:
        return self.client.get_user(user_id)
```

------

## Pitfall：真实踩坑

### 坑 1：可选字段放前面

```python
# ❌ 报错：non-default argument follows default argument
@dataclass
class User:
    age: Optional[int] = None
    name: str  # 必填字段不能放在可选字段后面

# ✅ 正确：必填在前，可选在后
@dataclass
class User:
    name: str
    age: Optional[int] = None
```

### 坑 2：Protocol 忘记 `...`

```python
# ❌ 语法不完整
class UserClient(Protocol):
    def get_user(self, user_id: str) -> User

# ✅ 正确：方法体用 ... 占位
class UserClient(Protocol):
    def get_user(self, user_id: str) -> User: ...
```

### 坑 3：Type Hints 不强制

Python 的类型提示是**静态检查用的**，运行时不会强制校验。

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

greet(123)  # 运行时不会报错！只有 IDE/mypy 会标红
```

要强制校验，需要配合 `mypy` 或 `pyright` 等工具。

------

## Application：在 RAG/Agent/架构中的位置

```
┌─────────────────────────────────────────────────────┐
│                   LLM 应用架构                        │
├─────────────────────────────────────────────────────┤
│  API 层     │  def chat(request: ChatRequest) -> ChatResponse
│             │       ↑ Type Hints 让接口清晰
├─────────────────────────────────────────────────────┤
│  Service 层 │  class ChatService:
│             │      def __init__(self, llm: LLMClient): ...
│             │       ↑ 依赖接口，可替换实现
├─────────────────────────────────────────────────────┤
│  数据层     │  @dataclass
│             │  class Document:
│             │      content: str
│             │      embedding: list[float]
│             │      metadata: dict
│             │       ↑ dataclass 定义 RAG 文档结构
└─────────────────────────────────────────────────────┘
```

**实际应用场景**：

- **RAG**：Document、Chunk、SearchResult 都用 dataclass 定义
- **Agent**：Tool 参数用 dataclass，LLM 返回结构化数据
- **API**：Request/Response 用 dataclass，配合 FastAPI 自动生成文档

------

## 视觉闭环：dict vs dataclass 对比

```
使用 dict:
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ 写代码       │ ──▶ │ user["nme"]  │ ──▶ │ 运行时爆炸   │
│ (拼错 key)   │     │ IDE 不管     │     │ KeyError     │
└──────────────┘     └──────────────┘     └──────────────┘

使用 dataclass:
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ 写代码       │ ──▶ │ user.nme     │ ──▶ │ 根本跑不到   │
│ (拼错字段)   │     │ IDE 标红 🔴  │     │ 写时就改了   │
└──────────────┘     └──────────────┘     └──────────────┘
```

------

## 工程师记忆分层

### 🗑️ 垃圾区（查文档）

- dataclass 的所有装饰器参数（frozen、order、slots...）
- typing 模块的完整类型列表

### 🔍 索引区（记关键词）

- `Optional[X] = None` —— 可选字段的写法
- `Protocol` —— 定义接口用
- `-> ReturnType` —— 返回类型标注

### 💎 核心区（必须内化）

- **dataclass 解决什么问题**：把松散字典变成有约束的结构
- **Type Hints 解决什么问题**：让接口自解释，IDE 能帮忙检查
- **可选字段必须放后面**：否则语法错误
- **类型提示不强制运行时校验**：需要配合 mypy/pyright

------

## 今日代码结构

```
week2-skeleton/
├── models.py   # User dataclass（数据结构）
├── client.py   # UserClient Protocol + 实现类（接口层）
├── service.py  # UserService（业务层，依赖接口）
└── demo.py     # 演示入口
```

**运行验证**：

```bash
cd projects/week2-skeleton
python demo.py
```

------

## Git 提交

```bash
git add ./
git commit -m "M1-W2-D2: Type Hints + dataclass"
git push
```

---

# M1-W2-D3 模块化

## Phase

Month 1 - Python 工程基石 > Week 2 - OOP + 类型系统 > Day 3 - 模块化

## 今日核心目标

把代码按职责组织成 Python 包结构，实现"一眼能看出每个模块是干什么的"

------

## Why：不学会导致的工程死穴

所有代码堆在一个文件里（比如 500 行的 main.py）会导致：

| 问题     | 后果                                     |
| -------- | ---------------------------------------- |
| 找代码难 | 想改 UserClient，要在 500 行里翻         |
| 改代码怕 | 改一个地方，不知道影响哪里               |
| 测试难   | 想单独测 Service，但它和 Client 混在一起 |
| 协作冲突 | 两个人都改 main.py，必然冲突             |

**Java 对比**：`com.company.service`、`com.company.dao` 这种分包思想，Python 一样需要。

------

## What：Python 包结构的第一性原理

### 核心概念 1：`__init__.py` = 包的身份证

```
week2_skeleton/
├── __init__.py          ← 有这个，Python 才认这是个包
├── client/
│   ├── __init__.py      ← 子包也要有
│   └── ...
```

**没有 `__init__.py` 会怎样？**

```python
from week2_skeleton.client import MockUserClient
# → 报错：ModuleNotFoundError
```

### 核心概念 2：`__init__.py` 控制导出

```python
# client/__init__.py
from .protocol import UserClient
from .mock_client import MockUserClient
from .real_client import RealUserClient

__all__ = ["UserClient", "MockUserClient", "RealUserClient"]
```

效果：

```python
# 简洁写法（推荐）
from week2_skeleton.client import MockUserClient

# 而不是
from week2_skeleton.client.mock_client import MockUserClient
```

### 核心概念 3：`python -m` 运行方式

```bash
# ✅ 正确：把当前目录加入 Python 路径
python -m week2_skeleton.main

# ❌ 错误：路径设置不对，导入会失败
python week2_skeleton/main.py
```

------

## How：最小可运行范式

### 标准包结构

```
week2_skeleton/
├── __init__.py              # 顶层包标识
├── client/
│   ├── __init__.py          # 导出：UserClient, MockUserClient, RealUserClient
│   ├── protocol.py          # Protocol 定义
│   ├── mock_client.py       # Mock 实现
│   └── real_client.py       # 真实实现
├── service/
│   ├── __init__.py          # 导出：UserService
│   └── user_service.py      # 业务逻辑
├── models/
│   ├── __init__.py          # 导出：User
│   └── user.py              # 数据模型
└── main.py                  # 入口脚本
```

### 相对导入语法

```python
# 在 client/__init__.py 中
from .protocol import UserClient      # . = 当前包
from .mock_client import MockUserClient
```

### 跨包导入语法

```python
# 在 service/user_service.py 中
from week2_skeleton.client import UserClient    # 绝对导入
from week2_skeleton.models import User
```

------

## Pitfall：真实踩坑

### 坑 1：文件命名用 PascalCase

```python
# ❌ Java 习惯：AdminClient.py
# ✅ Python 规范：admin_client.py（文件名 snake_case，类名 PascalCase）
```

### 坑 2：忘记 `__init__.py`

```python
# 新建了 utils/ 目录，忘记加 __init__.py
from week2_skeleton.utils import helper  # → ModuleNotFoundError
```

### 坑 3：直接运行包内脚本

```bash
# ❌ 这样跑，from week2_skeleton.xxx 会失败
python week2_skeleton/main.py

# ✅ 用 -m 方式
python -m week2_skeleton.main
```

------

## Application：在 RAG/Agent/架构中的位置

```
LLM 应用项目结构（预览）
├── clients/           # 各种外部 API 客户端
│   ├── llm_client.py      # LLM API
│   ├── embedding_client.py # Embedding API
│   └── vector_db_client.py # 向量数据库
├── services/          # 业务逻辑
│   ├── rag_service.py     # RAG 检索+生成
│   └── agent_service.py   # Agent 调度
├── models/            # 数据结构
│   ├── document.py        # 文档
│   └── message.py         # 消息
└── main.py            # 入口
```

模块化是**所有后续项目的基础骨架**，Month 2 开始的 LLMClient、RAG 系统都会用这个结构。

------

## 视觉闭环

```
代码组织演进
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

阶段 1：单文件
┌─────────────────────────────┐
│  main.py (500 行)           │
│  - User class               │
│  - MockClient               │
│  - RealClient               │
│  - UserService              │
│  - main()                   │
└─────────────────────────────┘
    ↓ 问题：混乱、难测试、协作冲突

阶段 2：模块化（今天学的）
┌─────────────────────────────┐
│  week2_skeleton/            │
│  ├── models/                │
│  │   └── user.py            │
│  ├── client/                │
│  │   ├── protocol.py        │
│  │   ├── mock_client.py     │
│  │   └── real_client.py     │
│  ├── service/               │
│  │   └── user_service.py    │
│  └── main.py                │
└─────────────────────────────┘
    ✅ 职责清晰、可独立测试、易协作
```

------

## 工程师记忆分层

### 🗑️ 垃圾区（查文档）

- `__all__` 的完整语法
- 相对导入的各种写法（`..` 上级包等）

### 🔍 索引区（记关键词）

- "运行包内脚本 → `python -m`"
- "导出控制 → `__init__.py` + `__all__`"
- "文件名 → snake_case"

### 💎 核心区（必须内化）

- **每个包目录必须有 `__init__.py`**
- **`python -m 包名.模块名` 是正确的运行方式**
- **按职责分包：client / service / models**

------

## 今日命令速查

```bash
# 运行包内脚本
python -m week2_skeleton.main

# 查看包结构
tree week2_skeleton/  # 或用 ls -la
```

------

## 关联回顾

| 昨天 (D2)                             | 今天 (D3)                       |
| ------------------------------------- | ------------------------------- |
| Type Hints + dataclass 定义接口和数据 | 把这些代码组织成包结构          |
| User、UserClient、UserService 的定义  | 放入 models/、client/、service/ |

**明天 (D4)**：给这个骨架加上 pytest 测试，验证 MockClient 注入是否能让 Service 独立测试。

---

#  M1-W2-D4

## Phase

Month 1 Week 2 Day 4 - pytest 基础

## 今日核心目标

用 pytest 验证"组合 + 依赖注入"架构的可测试性

------

## Why：不学会导致的工程死穴

**场景**：你改了 `MockClient` 的返回值格式，`demo.py` 跑一遍看起来没问题。三天后上线，发现 `UserService` 的某个逻辑被破坏了。

**死穴**：没有自动化测试 = 每次改动都靠人肉检查 = 迟早漏掉 bug

------

## What：第一性原理

**测试的本质**：用代码验证代码，把"人肉检查"变成"一条命令自动验证"。

**AAA 模式**（测试的标准结构）：

- **Arrange**：准备依赖和数据
- **Act**：执行被测方法
- **Assert**：验证结果

**类比**：AAA 就像做实验——准备材料 → 做实验 → 检查结果

------

## How：最小可运行范式



python

```python
from M1w2d4.base.service import UserService
from M1w2d4.base.client.mock_client import MockClient

def test_get_user_success():
    # Arrange: 准备 MockClient，注入 Service
    mock_client = MockClient()
    service = UserService(mock_client)
    
    # Act: 调用被测方法
    user = service.get_user("123")
    
    # Assert: 验证结果
    assert user.name == "123"
```

**运行测试**：



bash

```bash
python -m pytest tests/test_user_service.py -v
```

------

## Pitfall：真实踩坑

### 坑 1：用 print 而不是 assert



python

~~~python
# ❌ 需要人眼看
print(user.name)

# ✅ 自动判断对错
assert user.name == "123"
```

### 坑 2：Python 找不到模块
```
ModuleNotFoundError: No module named 'M1w2d4'
~~~

**原因**：Python 不知道去哪找你的包

**解法**：`pyproject.toml` + `pip install -e .`（W3 会系统学）

### 坑 3：import 路径写错



python

~~~python
# ❌ RealClient 不在 mock_client.py 里
from M1w2d4.base.client.mock_client import RealClient

# ✅ RealClient 在 real_client.py 里
from M1w2d4.base.client.real_client import RealClient
```

---

## Application：在 RAG/Agent/架构中的位置
```
┌─────────────────────────────────────────┐
│           测试金字塔                      │
├─────────────────────────────────────────┤
│         E2E 测试（少）                    │
│      ↑ 集成测试（中）                     │
│    ↑ 单元测试（多）  ← 今天学的           │
└─────────────────────────────────────────┘
```

- **Month 2**：测试 LLMClient（用 MockLLM 替代真实 API）
- **Month 4**：RAG 评测（用测试验证检索质量）
- **Month 5**：Agent 测试（用 MockTool 测试工具调用）

---

## 工程师记忆分层

### 🗑️ 垃圾区（查文档）
- pytest 命令参数
- assert 的各种写法

### 🔍 索引区（记关键词）
- `python -m pytest` 运行测试
- `pip install -e .` 安装本地包
- `-v` 显示详细输出

### 💎 核心区（必须内化）
- **AAA 模式**：Arrange → Act → Assert
- **为什么注入**：测试时换 Mock，生产时换 Real，Service 不用改
- **assert 不是 print**：自动验证，不是人眼看

---

## 视觉闭环
```
┌─────────────────────────────────────────────────┐
│              依赖注入 + 测试                      │
├─────────────────────────────────────────────────┤
│                                                 │
│   测试环境                    生产环境           │
│   ┌──────────┐              ┌──────────┐       │
│   │MockClient│              │RealClient│       │
│   └────┬─────┘              └────┬─────┘       │
│        │                         │             │
│        ▼                         ▼             │
│   ┌─────────────────────────────────────┐     │
│   │           UserService               │     │
│   │   （代码完全一样，一行不用改）         │     │
│   └─────────────────────────────────────┘     │
│                                                 │
└─────────────────────────────────────────────────┘
~~~

------

## 今日产出

- ```
  tests/test_user_service.py
  ```

  ：3 个测试

  - `test_get_user_success`：正常获取用户
  - `test_get_user_not_found`：用户不存在
  - `test_with_real_client`：验证可替换性

---

# M1-W2-D5: Logger 封装

------

## Phase

Month 1 Week 2 Day 5 - Python 工程基石 / OOP + 类型系统

## 今日核心目标

为 Service 层提供统一的日志能力，让程序运行过程可观测、可排查

------

## Why：不学会导致的工程死穴

没有日志的代码 = 黑盒：

- 请求发了吗？不知道
- 返回了什么？不知道
- 哪一步出错？猜
- 生产环境出问题？只能加日志重新部署

**print 调试法的致命问题**：

- 无法控制级别（生产环境还在打 debug？）
- 无法统一格式（排查时 grep 不到）
- 无法输出到文件（服务重启日志就没了）

------

## What：第一性原理 + 类比

### 核心概念：logging 三件套

| 组件          | 作用                      | Java 对应 |
| ------------- | ------------------------- | --------- |
| **Logger**    | 日志记录器，你调用的对象  | Logger    |
| **Handler**   | 输出目的地（控制台/文件） | Appender  |
| **Formatter** | 日志格式                  | Layout    |

### 级别从低到高



```
DEBUG < INFO < WARNING < ERROR < CRITICAL
  ↑                        ↑
开发调试用              生产环境只看这些
```

设成 INFO，DEBUG 就被过滤掉；设成 WARNING，INFO 也被过滤。

------

## How：最小可运行范式

### logger.py 封装



python

```python
import logging

def get_logger(name):
    logger = logging.getLogger(name)
    
    if not logger.handlers:  # 防止重复添加
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger
```

### Service 中使用



python

```python
from utils.logger import get_logger

logger = get_logger(__name__)  # 模块级，只初始化一次

class UserService:
    def get_user(self, user_id: str) -> User:
        logger.info(f'get user {user_id}')
        user = self.client.get_user(user_id)
        logger.info(f'get user {user_id} result: {user}')
        return user
```

### 格式化占位符速查

| 占位符          | 含义        | 示例                |
| --------------- | ----------- | ------------------- |
| `%(asctime)s`   | 时间        | 2026-01-18 15:09:07 |
| `%(name)s`      | logger 名称 | M1w2d5.service      |
| `%(levelname)s` | 级别        | INFO                |
| `%(message)s`   | 消息内容    | get user 1          |

------

## Pitfall：真实踩坑

### 坑 1：变量名覆盖模块名



python

```python
import logging
logging = logging.getLogger(name)  # ❌ logging 被覆盖，后面 logging.DEBUG 报错
logger = logging.getLogger(name)   # ✅ 用不同的变量名
```

### 坑 2：每次调用都 addHandler → 日志重复



python

```python
# ❌ 错误：每次打日志都获取
def get_user(self):
    get_logger(__name__).info("xxx")  # 每次都加 handler，日志越打越多

# ✅ 正确：模块级获取一次
logger = get_logger(__name__)
def get_user(self):
    logger.info("xxx")
```

### 坑 3：没检查 handlers 是否已存在



python

~~~python
# ✅ 健壮写法
if not logger.handlers:
    logger.addHandler(handler)
```

---

## Application：在 RAG/Agent/架构中的位置
```
┌─────────────────────────────────────────────┐
│                 API Gateway                  │
│            logger: 请求入口/出口             │
└─────────────────┬───────────────────────────┘
                  │
┌─────────────────▼───────────────────────────┐
│                 Service 层                   │
│     logger: 业务流程关键节点 (INFO)          │
└─────────────────┬───────────────────────────┘
                  │
┌─────────────────▼───────────────────────────┐
│              Client/LLM 层                   │
│     logger: 调用细节/耗时/重试 (DEBUG)       │
└─────────────────────────────────────────────┘
```

生产环境：设 INFO，只看业务流程
排查问题：改 DEBUG，看技术细节

---

## 视觉闭环：日志流向
```
代码调用                     输出目的地
─────────                   ───────────
logger.info("msg")
       │
       ▼
   ┌────────┐
   │ Logger │ ← 级别过滤（INFO 以上才通过）
   └───┬────┘
       │
       ▼
   ┌─────────┐
   │ Handler │ ← StreamHandler（控制台）
   └───┬─────┘   FileHandler（文件）
       │
       ▼
   ┌───────────┐
   │ Formatter │ ← 格式化输出
   └───────────┘
       │
       ▼
   控制台 / 日志文件
~~~

------

## 工程师记忆分层

### 🗑️ 垃圾区（查文档）

- Formatter 所有占位符
- Handler 的各种参数
- 日志文件轮转配置

### 🔍 索引区（记关键词）

- `logging.getLogger(name)` - 获取 logger
- `StreamHandler` / `FileHandler` - 两种输出
- `setLevel` / `setFormatter` / `addHandler` - 三步配置

### 💎 核心区（必须内化）

- **Logger 只获取一次**，放模块级或类属性
- **检查 handlers 防重复**：`if not logger.handlers`
- **级别控制是核心价值**：生产 INFO，调试 DEBUG

------

## 今日产出

- `utils/logger.py` - 统一 logger 封装
- `service/user_service.py` - 加入业务日志

---

# M1-W2-WE1

## A. 头部

**Phase**: Month 1 - Python 工程基石 > Week 2 - OOP + 类型系统 > WE1

**今日核心目标**: 实现 config 模块，解决敏感信息管理、类型转换、必填校验三大问题

------

## B. 正文

### Why：不学会导致的工程死穴

1. **密钥泄露** - 硬编码 API Key 提交到 Git，泄露后被恶意调用，账单爆炸
2. **新人懵逼** - 项目没有配置模板，新人 clone 下来不知道要配什么，跑不起来
3. **类型隐患** - `os.getenv("DEBUG")` 返回字符串 `"false"`，但 `if "false"` 是 truthy，逻辑全错
4. **延迟失败** - 关键配置缺失，程序启动时不报错，等到真正调 API 时才崩，排查困难

### What：第一性原理

**配置管理的本质**：把"会变的东西"从代码中分离出来，同时保证类型安全和启动校验。

**Python 社区通用模式**：`.env` + `.env.example`

| 文件           | 作用                         | 是否提交 Git |
| -------------- | ---------------------------- | ------------ |
| `.env`         | 存真实配置（含敏感信息）     | ❌ 忽略       |
| `.env.example` | 配置模板（告诉别人要配什么） | ✅ 提交       |

### How：最小可运行范式



python

~~~python
# config.py 核心结构
from dataclasses import dataclass
from dotenv import load_dotenv
import os

@dataclass
class Config:
    api_key: str                              # 必填，无默认值
    api_base: str = "https://api.example.com" # 有默认值
    timeout: int = 30
    debug: bool = False

    def __post_init__(self):
        if not self.api_key:                  # 快速失败
            raise ValueError("API_KEY is required")

def load_config() -> Config:
    load_dotenv()                             # 加载 .env 到环境变量
    return Config(
        api_key=os.getenv("API_KEY"),
        api_base=os.getenv("API_BASE", "https://api.example.com"),
        timeout=int(os.getenv("TIMEOUT", 30)),
        debug=str_to_bool(os.getenv("DEBUG", False))
    )

def str_to_bool(value) -> bool:
    if isinstance(value, bool):
        return value
    if value.lower() in ["true", "1", "yes"]:
        return True
    if value.lower() in ["false", "0", "no"]:
        return False
    raise ValueError(f"Cannot convert '{value}' to bool")
```

### Pitfall：真实踩坑

| 坑 | 现象 | 解决 |
|----|------|------|
| `os.getenv()` 返回 None | dataclass 默认值被 None 覆盖 | 用 `os.getenv("KEY", default)` |
| 字符串 `"false"` 是 truthy | `if os.getenv("DEBUG")` 永远为真 | 手写 `str_to_bool()` 转换 |
| `int("abc")` 报错 | 用户配置格式错误时程序崩溃 | 可以加 try-catch（今天未涉及） |
| 必填项缺失延迟报错 | API 调用时才发现 key 是 None | `__post_init__` 快速失败 |

### Application：在 RAG/Agent/架构中的位置
```
┌─────────────────────────────────────────┐
│              应用启动                    │
├─────────────────────────────────────────┤
│  1. load_config()                       │  ← 最先执行
│     - 读取 .env                         │
│     - 类型转换                          │
│     - 必填校验（快速失败）               │
├─────────────────────────────────────────┤
│  2. 初始化各模块                         │
│     - LLMClient(config.api_key, ...)    │
│     - Logger(config.debug)              │
│     - Service(client, logger)           │
├─────────────────────────────────────────┤
│  3. 启动服务                            │
└─────────────────────────────────────────┘
```

**实际场景**：
- RAG 系统：需要配置向量库地址、Embedding 模型 API Key、LLM API Key
- Agent 系统：需要配置工具权限开关、最大执行步数、超时时间
- 多环境部署：dev/staging/prod 用不同的 `.env` 文件

---

## C. 视觉闭环

### 配置加载流程
```
.env 文件                    代码
───────────                 ─────
API_KEY=sk-xxx              
DEBUG=true        ──────►   load_dotenv()
TIMEOUT=60                      │
                                ▼
                          os.getenv("API_KEY")     → "sk-xxx"
                          os.getenv("DEBUG")       → "true"
                          os.getenv("TIMEOUT")     → "60"
                                │
                                ▼
                          类型转换
                          ────────
                          api_key: str             → "sk-xxx"
                          debug: str_to_bool()     → True
                          timeout: int()           → 60
                                │
                                ▼
                          Config 实例
                          ───────────
                          __post_init__() 校验
                                │
                        ┌───────┴───────┐
                        ▼               ▼
                    校验通过         校验失败
                    返回 Config      raise ValueError
```

### 文件结构
```
project/
├── .env              ← 真实配置（不提交）
├── .env.example      ← 配置模板（提交）
├── .gitignore        ← 包含 .env
└── src/
    └── config.py     ← 加载逻辑
~~~

------

## D. 工程师记忆分层

### 🗑️ 垃圾区（查文档）

- `load_dotenv()` 的其他参数（override、dotenv_path 等）
- `os.environ` vs `os.getenv()` 的细节区别
- pydantic-settings 等更高级的配置库

### 🔍 索引区（记关键词）

- `python-dotenv` - 加载 .env 的库
- `os.getenv(key, default)` - 第二个参数是默认值
- `__post_init__` - dataclass 初始化后钩子
- `.env.example` - 配置模板文件

### 💎 核心区（必须内化）

1. **敏感信息永不硬编码**，用 `.env` + `.gitignore`
2. **字符串 `"false"` 是 truthy**，布尔值必须手动转换
3. **快速失败**：关键配置缺失时，启动阶段就报错，不要等到用的时候
4. **加新配置的步骤**：`.env.example` → `Config` 类 → `load_config()` 函数

---

# M1-W2-WE2

## Phase

Month 1 - Week 2 - Weekend 2 | Python 工程基石

## 今日核心目标

将分散的日练代码整合为一个**可交付的完整项目**，掌握 Python 包结构与导入机制。

------

## Why：不整合会怎样？

| 不整合的后果             | 工程死穴                           |
| ------------------------ | ---------------------------------- |
| 每天代码分散在不同文件夹 | pytest 跑不通（import 路径不统一） |
| 没有统一入口             | 别人拿到不知道怎么跑               |
| 没有 README              | 三个月后自己也忘了怎么用           |
| 模块之间不能互相调用     | 无法复用已写好的代码               |

**真实场景**：入职后接手的代码，不会是 `D1/`、`D2/`、`D3/` 分开的，而是一个完整、模块协作的项目。

------

## What：Python 包机制的本质

### 核心概念

**包（Package）**：带有 `__init__.py` 的文件夹，Python 把它当作可导入的模块。

**相对导入 vs 绝对导入**：



python

~~~python
# 绝对导入：从包的根开始
from week2_skeleton.models import User

# 相对导入：从当前位置出发
from ..models import User  # .. 表示上一级
from .protocol import UserClient  # . 表示当前目录
```

**`pip install -e .` 的作用**：
```
week2-skeleton/          ← 在这里执行 pip install -e .
├── src/
│   └── week2_skeleton/  ← Python 认识的包名
└── pyproject.toml       ← 告诉 pip：包在 src/ 下
```

执行后，Python 全局认识 `week2_skeleton`，不用再纠结路径。

---

## How：最小可运行范式

### 项目结构模板
```
project-name/
├── src/
│   └── package_name/
│       ├── __init__.py
│       ├── clients/
│       │   ├── __init__.py      ← 导出模块内容
│       │   ├── protocol.py      ← 接口定义
│       │   ├── mock_client.py
│       │   └── real_client.py
│       ├── service/
│       ├── models/
│       ├── utils/
│       └── config.py
├── tests/
├── .env.example
├── pyproject.toml
├── demo.py
└── README.md
~~~

### `__init__.py` 导出模式



python

```python
# clients/__init__.py
from .protocol import UserClient
from .mock_client import MockUserClient
from .real_client import RealUserClient

__all__ = ["UserClient", "MockUserClient", "RealUserClient"]
```

外部就能简洁导入：`from week2_skeleton.clients import MockUserClient`

------

## Pitfall：今天踩过的坑

### 坑 1：requests 异常处理不完整



python

```python
# ❌ 只检查状态码
result = requests.get(url)
if result.status_code != 200:
    return default_user

# ✅ 网络异常也要兜住
try:
    result = requests.get(url, timeout=5)
    if result.status_code != 200:
        return default_user
    ...
except Exception:
    return default_user  # 超时、断网都走这里
```

### 坑 2：dict 取值方式



python

```python
data = {"name": "Tom"}

# ❌ 直接取不存在的 key
data["age"]  # KeyError!

# ✅ 用 get() 给默认值
data.get("age", 0)  # 不存在返回 0
```

### 坑 3：测试断言与实际返回不匹配



python

~~~python
# MockUserClient 返回固定值
return User(user_id, "mock_name", ...)

# ❌ 测试断言期望动态值
assert user.name == "123"  # 永远失败

# ✅ 断言要匹配 Mock 的可预测返回
assert user.name == "mock_name"
```

### 坑 4：VSCode Run Code vs 终端

`pip install -e .` 安装的包，**只在当前 Python 环境生效**。VSCode 的 Run Code 插件可能用了不同环境，导致 `ModuleNotFoundError`。

**解决**：用终端运行，或者配置 VSCode 使用正确的解释器。

---

## Application：在 RAG/Agent 中的位置
```
┌─────────────────────────────────────────────────────────┐
│                    AI 应用架构                           │
├─────────────────────────────────────────────────────────┤
│  ┌─────────┐   ┌─────────┐   ┌─────────┐               │
│  │ Config  │──▶│ Client  │──▶│ Service │               │
│  │ (.env)  │   │(可替换) │   │(业务)   │               │
│  └─────────┘   └─────────┘   └─────────┘               │
│       │              │              │                   │
│       │         Protocol        依赖注入                │
│       │        ┌────┴────┐                             │
│       │        │         │                             │
│       │   MockClient  RealClient                       │
│       │   (测试用)    (调LLM API)  ← Month2 会用到      │
└─────────────────────────────────────────────────────────┘
```

今天搭建的骨架，就是 **Month2 LLMClient 的基础**。到时候只需要：
- 把 `RealUserClient` 换成 `OpenAIClient`
- 把 `User` 换成 `ChatResponse`

结构完全一样。

---

## 视觉闭环：项目整合流程
```
分散代码                    整合后
─────────                  ─────────
M1w2d1/                    week2-skeleton/
M1w2d2/     ──整合──▶      ├── src/week2_skeleton/
M1w2d3/                    │   ├── clients/
M1w2d4/                    │   ├── service/
M1w2d5/                    │   ├── models/
M1w2we1/                   │   └── utils/
                           ├── tests/
    ❌ import 互相找不到    └── README.md
    ❌ pytest 跑不通        
    ❌ 别人看不懂            ✅ pip install -e .
                           ✅ pytest 全绿
                           ✅ python demo.py 可演示
~~~

------

## 工程师记忆分层

### 🗑️ 垃圾区（查文档）

- pyproject.toml 的完整语法
- setuptools 配置细节
- requests 库的所有参数

### 🔍 索引区（记关键词）

- `pip install -e .` — 可编辑安装
- `..` 相对导入 — 上一级目录
- `__all__` — 控制导出内容
- `dict.get(key, default)` — 安全取值

### 💎 核心区（必须内化）

- **Mock 的价值**：快、免费、稳定、不依赖外部
- **测试断言要匹配实际返回**，不是你期望的返回
- **requests 必须 try-except**：网络不可靠
- **项目要能一键跑通**：README + demo.py + pip install -e .

------

## Week 2 总结

| Day  | 主题                   | 核心收获                         |
| ---- | ---------------------- | -------------------------------- |
| D1   | 组合优于继承           | Service 依赖接口，不依赖具体实现 |
| D2   | Type Hints + dataclass | 类型安全 + 数据结构定义          |
| D3   | 模块化                 | 包结构 + `__init__.py`           |
| D4   | pytest                 | MockClient 注入测试              |
| D5   | logger                 | 统一日志格式                     |
| WE1  | config                 | .env + 敏感信息管理              |
| WE2  | 整合                   | 可交付的完整项目                 |

---

# M1-W3-D1

## Phase

Month 1 Week 3 - 工程模板化

## 今日核心目标

掌握 uv + src 布局，让项目**可复现、可维护**

------

## Why：不学会导致的工程死穴

- 同事 clone 代码跑不起来（依赖没记录）
- 项目大了文件乱成一团（代码/测试/配置混在一起）
- 换台电脑环境就崩（依赖版本不一致）

------

## What：第一性原理

**依赖管理**：让任何人在任何机器上，一条命令还原你的运行环境

**src 布局**：源代码与其他文件（测试、配置、文档）物理隔离

| Python         | Java 类比          |
| -------------- | ------------------ |
| uv             | Maven / Gradle     |
| pyproject.toml | pom.xml            |
| uv.lock        | 锁定的版本号       |
| .venv/         | 项目本地的依赖目录 |

------

## How：最小可运行范式



bash

```bash
# 创建项目
uv init python-app-template
cd python-app-template

# 添加依赖（自动记录）
uv add python-dotenv

# 同步环境
uv sync

# 运行代码
uv run python -m python_app_template.main
```

**pyproject.toml 关键配置**：



toml

~~~toml
[tool.uv]
package = true

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/python_app_template"]
```

---

## Pitfall：真实踩坑

| 坑 | 原因 | 解法 |
|----|------|------|
| `uv: command not found` | PATH 没生效 | `source $HOME/.local/bin/env` |
| import 写 `from src.xxx` | 多了 `src.` 前缀 | 直接 `from python_app_template.xxx` |
| 改代码要重新打包？ | 不需要，可编辑模式安装 | 直接跑，热生效 |

---

## Application：在 RAG/Agent/架构中的位置

- **现在**：所有后续项目的起点模板
- **Month 2+**：LLMClient、RAG、Agent 都基于这个结构
- **生产环境**：标准 src 布局是开源项目和企业项目的通用规范

---

## 视觉闭环
```
┌─────────────────────────────────────────┐
│           python-app-template/          │
├─────────────────────────────────────────┤
│  pyproject.toml    ← 依赖 + 配置中心    │
│  uv.lock           ← 版本锁定           │
│  .venv/            ← 隔离环境           │
├─────────────────────────────────────────┤
│  src/                                   │
│   └── python_app_template/              │
│        ├── main.py     ← 入口           │
│        ├── client/     ← 外部调用       │
│        ├── service/    ← 业务逻辑       │
│        └── utils/      ← 工具函数       │
├─────────────────────────────────────────┤
│  tests/              ← 测试（与 src 分离）│
└─────────────────────────────────────────┘
~~~

------

## 工程师记忆分层

🗑️ **垃圾区（查文档）**

- hatchling 具体配置语法
- uv 的所有子命令

🔍 **索引区（记关键词）**

- `uv init` / `uv add` / `uv sync` / `uv run`
- pyproject.toml 三段配置（tool.uv / build-system / tool.hatch）

💎 **核心区（必须内化）**

- **uv add 自动记录依赖，不再手动管 requirements.txt**
- **src 布局：源代码统一放 src/ 下**
- **import 路径不含 src.，从包名开始**

---

# M1-W3-D2

## A. 头部

**Phase**: M1-W3-D2 | Python 工程基石 · 工程模板化

**今日核心目标**: 用 Fixture 消除测试代码的重复，用 AAA 模式让测试结构清晰可读

------

## B. 正文

### Why：不学会导致的工程死穴

**没有 Fixture 的痛苦**：

- 20 个测试函数，每个都写 `service = UserService(MockClient())`
- 构造函数改了（加个 logger 参数）→ **改 20 处**
- 违反 DRY 原则，维护成本指数级上升

**没有 AAA 的痛苦**：

- 测试代码一坨，不知道哪里是准备、哪里是执行、哪里是验证
- 别人（包括未来的自己）看不懂测试意图
- Debug 时找不到问题出在哪个阶段

------

### What：第一性原理 + 类比

**Fixture 本质**：依赖注入的测试版

| Java (JUnit)  | Python (pytest)   |
| ------------- | ----------------- |
| `@BeforeEach` | `@pytest.fixture` |
| 成员变量      | fixture 返回值    |
| 手动调用      | pytest 自动注入   |

**AAA 本质**：测试的三段式结构



```
Arrange → 准备弹药
Act     → 开枪
Assert  → 检查靶子
```

------

### How：最小可运行范式

**单层 Fixture**：



python

```python
@pytest.fixture
def user_service():
    return UserService(MockClient())

def test_get_user(user_service):  # 参数名 = fixture 名
    user = user_service.get_user(1)
    assert user.id == 1
```

**两层 Fixture（依赖链）**：



python

```python
@pytest.fixture
def mock_client():
    return MockUserClient()

@pytest.fixture
def user_service(mock_client):  # fixture 依赖 fixture
    return UserService(mock_client)
```

**AAA 模式**：



python

~~~python
def test_get_user(user_service):       # Arrange - fixture 注入
    user = user_service.get_user(1)    # Act - 执行
    assert user.id == 1                # Assert - 验证
```

---

### Pitfall：真实踩坑

| 坑 | 现象 | 原因 |
|----|------|------|
| 参数名不匹配 | fixture 没被调用 | pytest 靠**参数名**找 fixture |
| Act 和 Assert 混淆 | 写成 `assert service.get_user(1).id == 1` | 一行塞太多，出错难定位 |
| fixture 里写断言 | 测试逻辑混乱 | fixture 只负责**准备**，不负责验证 |

---

### Application：在 RAG/Agent/架构中的位置
```
Month 2: LLMClient 测试 → mock LLM 响应
Month 3: RAG 测试 → mock 向量库、mock 检索结果  
Month 5: Agent 测试 → mock 工具执行、mock LLM 决策
```

Fixture + AAA 是所有测试的骨架，后面只是被测对象变复杂了。

---

## C. 视觉闭环
```
┌─────────────────────────────────────────────────────┐
│                    pytest 执行流程                    │
└─────────────────────────────────────────────────────┘

  test_get_user(user_service)
         │
         ▼ pytest 发现参数名 "user_service"
  ┌──────────────┐
  │ user_service │ fixture
  │   (mock_client) ◄─── pytest 发现参数名 "mock_client"
  └──────┬───────┘
         │              ┌─────────────┐
         │              │ mock_client │ fixture
         │              └──────┬──────┘
         ▼                     ▼
  ┌──────────────────────────────────────┐
  │  返回 UserService(MockUserClient())  │
  └──────────────────────────────────────┘
         │
         ▼ 注入到测试函数
  ┌──────────────────────────────────────┐
  │  def test_get_user(user_service):    │
  │      user = user_service.get_user(1) │  ← Act
  │      assert user.id == 1             │  ← Assert
  └──────────────────────────────────────┘
~~~

------

## D. 工程师记忆分层

### 🗑️ 垃圾区（查文档）

- fixture 的 scope 参数（function/class/module/session）
- pytest 的其他高级特性（parametrize、mark 等）

### 🔍 索引区（记关键词）

- `@pytest.fixture` — 定义 fixture 的装饰器
- fixture 可以依赖 fixture — 通过参数名注入
- `uv run pytest -v` — 运行测试

### 💎 核心区（必须内化）

- **Fixture 解决重复**：改一处 vs 改 N 处
- **参数名匹配**：pytest 靠参数名找 fixture
- **AAA 三段式**：Arrange（准备）→ Act（执行）→ Assert（验证）

---

# 全栈宗师笔记：M1

## Phase

Month 1 · Week 3 · Day 4 —— Python 工程基石 / 工程模板化

## 今日核心目标

用 pyright 在运行前发现类型错误，把 type hints 从"注释"变成"约束"

------

## Why：不学会导致的工程死穴



python

~~~python
def greet(name: str) -> str:
    return f"Hello, {name}"

result = greet(123)  # Python 照跑不误！
```

type hints 是**弱约束**，Python 解释器完全忽略。

后果：
- 辛苦写的类型标注形同虚设
- 类型错误直到线上才暴露
- 团队协作时接口约定无法强制执行

---

## What：第一性原理
```
┌─────────────────────────────────────────┐
│  Python = 动态类型语言                   │
│  type hints = 给人/工具看的"注释"        │
│  pyright = 把注释变成强制检查的工具      │
└─────────────────────────────────────────┘
~~~

**类比**：

- type hints = 交通标志（告诉你限速60）
- Python 解释器 = 不装摄像头的路（超速也没人管）
- pyright = 测速摄像头（超速立刻报警）

------

## How：最小可运行范式

### 1. 安装配置



bash

```bash
uv add --dev pyright
```



json

```json
// pyrightconfig.json
{
  "include": ["src"],
  "pythonVersion": "3.13",
  "typeCheckingMode": "basic"
}
```

### 2. 运行检查



bash

```bash
uv run pyright src
```

### 3. 常见类型标注速查



python

```python
# 基本类型
name: str = "十香"
age: int = 29

# 容器类型
names: list[str] = ["A", "B"]
scores: dict[str, int] = {"A": 90}

# 可选类型（允许 None）
email: str | None = None          # 新写法
email: Optional[str] = None       # 旧写法，需 from typing import Optional

# 函数无返回值
def log(msg: str) -> None:
    print(msg)
```

### 4. Optional vs 默认值（易混淆）



python

~~~python
# 必须传，允许 str 或 None
name: Optional[str]

# 可不传，默认 None，允许 str 或 None  
name: Optional[str] = None

# 可不传，默认 None，但 pyright 报错（str 不接受 None）
name: str = None  # ❌
```

---

## Pitfall：真实踩坑

| 坑 | 表现 | 解法 |
|---|---|---|
| pyproject.toml 解析警告 | 一堆 parse error 输出 | 用 pyrightconfig.json 替代 |
| Optional 和默认值混淆 | 以为 Optional 控制"是否必传" | Optional 控制"允许什么值"，`=` 控制"是否必传" |
| 忘记跑检查 | type hints 写了但没检查 | CI 集成（明天学） |

---

## Application：在 RAG/Agent/架构中的位置
```
┌─────────────────────────────────────────────┐
│              LLM 应用项目                    │
├─────────────────────────────────────────────┤
│  models.py    → dataclass + 类型标注        │
│  client.py    → Protocol 接口定义           │
│  services.py  → 返回值 User | None          │
├─────────────────────────────────────────────┤
│  pyright      → CI 前置检查，类型不对不合并  │
└─────────────────────────────────────────────┘
```

真实场景：
- LLMClient 返回 `ChatResponse | None`
- RAG 检索返回 `list[Document]`
- Agent 工具调用参数必须类型正确

---

## 视觉闭环：类型检查工作流
```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  写代码      │ → │  pyright     │ → │  运行代码    │
│  + type hints│    │  静态检查    │    │              │
└──────────────┘    └──────────────┘    └──────────────┘
                          │
                          ▼
                    ┌──────────────┐
                    │  类型错误？   │
                    │  立刻报警！   │
                    └──────────────┘
~~~

------

## 工程师记忆分层

### 🗑️ 垃圾区（查文档）

- pyrightconfig.json 的所有配置项
- typing 模块的全部类型（Callable、TypeVar 等）

### 🔍 索引区（记关键词）

- `typeCheckingMode`: basic / strict
- `Union[A, B]` = `A | B`
- `from typing import Optional, Protocol`

### 💎 核心区（必须内化）

- **type hints 是弱约束，pyright 是强约束**
- **Optional[str] = str | None（控制允许什么值）**
- **= 默认值（控制是否必须传）**
- **这两个是独立的，别混淆**

------

## 今日命令速查



bash

```bash
# 安装
uv add --dev pyright

# 检查
uv run pyright src

# 预期输出
0 errors, 0 warnings, 0 informations
```

---

