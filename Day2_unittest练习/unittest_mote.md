# Day2｜Python 单元测试框架 unittest 学习总结

## 1. 基本概念

- **unittest**：Python标准单元测试框架，用来测试代码功能是否正确。
- **测试用例（TestCase）**：每个测试方法以`test_`开头，验证一个功能点。

## 2. 测试生命周期

| 方法                 | 作用                   | 特点                                 |
| :------------------- | :--------------------- | :----------------------------------- |
| `setUp(self)`        | 每个测试方法执行前执行 | 准备测试数据，每次都会重新执行       |
| `tearDown(self)`     | 每个测试方法执行后执行 | 清理测试数据，释放资源               |
| `setUpClass(cls)`    | 测试类开始前执行一次   | 类级别资源初始化，使用`@classmethod` |
| `tearDownClass(cls)` | 测试类结束后执行一次   | 类级别资源回收，使用`@classmethod`   |

## 3. 常用断言方法

- `assertEqual(a, b)`：判断a和b是否相等
- `assertTrue(x)`：判断x是否为True
- `assertRaises(ExceptionType)`：验证代码是否抛出指定异常

## 4. mock机制

- **mock**：用来**模拟外部依赖**（如网络请求、数据库查询），防止测试依赖外部环境。
- 使用`unittest.mock.patch`进行mock替换，常配合`with`语句管理mock生命周期。

示例：

```python
with patch('BankAccount.requests.get') as mock_get:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'rate': 0.5}
    result = account.get_interest_rate()
    self.assertEqual(result, 0.5)
```

## 5. with语句理解

- `with`语句用于**自动管理资源**（打开时做初始化，退出时做清理），提高安全性和代码简洁性。
- 应用场景：文件操作、mock、数据库连接、线程锁等。



---

# 单元测试学习过程中的错误归纳

## 1. 文件命名错误导致模块冲突

- **问题现象**：项目里有一个 `requests.py` 文件，导致Python导入的是自己的文件，而不是标准库 `requests`。
- **错误提示**：
  ```
  AttributeError: module 'requests' has no attribute 'get'
  ```
- **根本原因**：
  - Python的import机制优先加载当前目录下的文件。
  - 文件名与标准库重名，导致import冲突。

- **解决方法**：
  - 改文件名，避免和标准库（requests、json、random等）重名。
  - 删除旧的 `.pyc` 缓存文件（pycache文件夹）。

---

## 2. patch路径写错

- **错误写法**：
  ```python
  patch('requests.get')
  ```
- **正确理解**：
  - patch的路径是 **模块名 + 模块内部访问的名字**。
  - 应该写成：
    ```python
    patch('WeatherService.requests.get')
    ```
    （WeatherService是你的模块名）

- **核心思路**：
  > patch的对象必须是“测试模块里引用的名字”，不是官方库的名字！

---

## 3. mock对象与返回值搞混

- **错误写法**：
  ```python
  mock_get.status_code = 200
  ```
- **正确写法**：
  ```python
  mock_get.return_value.status_code = 200
  ```
- **本质理解**：
  - `mock_get`是mock了`requests.get`这个**函数**，不是返回的response对象。
  - 正确的模拟流程是：
    - `mock_get()` 生成 `mock_get.return_value`
    - 你需要配置的是 `mock_get.return_value` 上的属性，比如`status_code`、`json()`等。

- **核心记忆**：
  > mock的是函数，return_value才是调用后得到的返回对象！

---

## 4. 模块名大小写敏感问题

- **注意点**：
  - Python模块名严格区分大小写。
  - 你模块叫`WeatherService.py`，那patch路径也必须是`WeatherService.requests.get`，大小写一模一样。

- **坑点**：
  - 如果写成`weatherservice.requests.get`，或者大小写不匹配，会找不到对象

---

# 🌟 总结思考

- 写测试时，一定先搞清楚**模块导入路径**和**模块内部调用路径**。
- patch对象时，先搞清楚自己要mock的是**函数本身**，还是**函数返回的对象**。
- 项目文件命名要小心，避免和标准库重名，保持环境干净。
