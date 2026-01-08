## Day 1 - 列表推导式基础（2026-01-05）

### 核心目标

理解列表推导式的本质：表达意图而非描述过程

------

### Why（不学会导致的工程死穴）

如果不理解列表推导式的本质，你会：

- ❌ 把它当作"代码简化技巧"，只是背模板
- ❌ 写出冗长的循环代码，降低代码可读性
- ❌ 无法快速理解他人的 Python 代码（列表推导式在 Python 中极其常见）
- ❌ 在面试和 Code Review 时显得不够 Pythonic

------

### What（第一性原理 + 类比）

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

### How（最小可运行范式）

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

### Pitfall（真实踩坑）

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

### 工程师记忆分层

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

## Day 2 - 列表推导式进阶（2026-01-06）

### 核心目标

理解列表推导式的适用边界，建立"可读性 > 简洁性"的工程思维

------

### Why（不学会导致的工程死穴）

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

### What（第一性原理 + 类比）

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

### How（最小可运行范式）

#### **应该用列表推导式的场景：**

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

#### **不应该用列表推导式的场景：**

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

### Pitfall（真实踩坑）

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

### Application（在哪里用）

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

### 工程师记忆分层

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

## Day 3 - 生成器入门（2026-01-07）

### 核心目标

理解生成器的惰性计算本质，建立内存效率的工程意识

------

### Why（不学会导致的工程死穴）

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

### What（第一性原理 + 类比）

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

### How（最小可运行范式）

#### **生成器的两种语法（独立，不混用）**

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

#### **yield 的工作机制**

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

#### **内存对比（实际测试）**



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

#### **使用生成器**



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

### Pitfall（真实踩坑）

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

### Application（在哪里用）

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

### 工程师记忆分层

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

## Day 4 - 装饰器基础（2026-01-08）

### 核心目标

理解装饰器的本质，掌握函数式编程的核心思维

------

### Why（不学会导致的工程死穴）

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

### What（第一性原理 + 类比）

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

### How（最小可运行范式）

#### **基础装饰器**



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

#### **处理参数的装饰器**



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

#### **实用装饰器示例**

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

### Pitfall（真实踩坑）

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

### Application（在哪里用）

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

### 工程师记忆分层

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

## Day 5 - 装饰器进阶（2026-01-09）

### 核心目标

掌握带参数的装饰器、装饰器叠加和 functools.wraps

------

### Why（不学会导致的工程死穴）

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

### What（第一性原理 + 类比）

#### **带参数的装饰器**

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

#### **装饰器叠加**

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

#### **functools.wraps**

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

### How（最小可运行范式）

#### **1. 带参数的装饰器（三层结构）**

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

#### **2. 装饰器叠加**

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

#### **3. functools.wraps 的使用**

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

### Pitfall（真实踩坑）

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

### Application（在哪里用）

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

### 工程师记忆分层

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
