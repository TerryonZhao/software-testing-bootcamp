# 📚 Day3｜Postman学习总结笔记

---

## 1. Postman构造Request的四个重要模块

| 模块        | 作用说明                                         |
| ----------- | ------------------------------------------------ |
| **Method**  | 请求方法（GET、POST、PUT、DELETE等）             |
| **URL**     | 请求地址，决定访问的资源或服务                   |
| **Headers** | 请求头，用于描述请求的元信息（如数据格式、认证） |
| **Body**    | 请求体，提交给服务器的数据（主要用于POST/PUT）   |

---

## 2. URL的基本结构

```
协议://主机:端口/路径?查询参数
```

**举例：**
```
https://api.example.com/v1/users?id=123&active=true
```

| 部分     | 说明                |
| -------- | ------------------- |
| 协议     | http / https        |
| 主机     | api.example.com     |
| 路径     | /v1/users           |
| 查询参数 | id=123，active=true |

**注意：**
- GET请求时，查询参数（Params）会拼接在URL后面。
- POST请求时，参数通常放在Body中，不在URL里。

---

## 3. Headers（请求头）知识点

- **作用**：用于描述请求本身，比如告诉服务器"我发送的数据是什么格式"，或者"我有权限访问这个接口"。
- **常见Headers举例**：
  | Header 名称   | Value 示例             | 用途说明            |
  | ------------- | ---------------------- | ------------------- |
  | Content-Type  | application/json       | 请求体是JSON格式    |
  | Authorization | Bearer eyJhbGciOiJI... | 认证Token，验证身份 |

**总结：**
> Header 是"控制信息"，不是"业务参数"。通常根据接口文档要求设置。

---

## 4. Body（请求体）知识点

- **作用**：用于提交实际数据给服务器，常见于 POST / PUT 请求。
- **Postman中Body的常用类型**：
  | 类型                  | 说明                                   | 场景                      |
  | --------------------- | -------------------------------------- | ------------------------- |
  | raw（+ JSON格式）     | 直接发送结构化数据（如 JSON）          | 注册、登录、提交表单数据  |
  | x-www-form-urlencoded | 类似传统表单提交，键值对格式           | 老系统表单接口，如PHP后台 |
  | form-data             | 上传文件 + 字段（multipart/form-data） | 文件上传接口              |

- **JSON 示例（raw）**：
```json
{
  "username": "test123",
  "password": "abc123"
}
```

**总结：**
> Body 是"具体提交的数据"，内容结构和字段，必须严格按照接口文档定义来写。

---

## 5. 今日实操总结

- 成功在Postman中构造并发送了一个**POST请求**到 [JSONPlaceholder API](https://jsonplaceholder.typicode.com/posts)。

  <img src="/Users/macbook/Library/Application Support/typora-user-images/image-20250429215246167.png" alt="image-20250429215246167" style="zoom:3%0;" />
- 理解了 Method、URL、Headers、Body 四个核心组成。
- 掌握了GET和POST请求在参数传递方式上的区别。

---

# ✅ 小结

> Postman构造请求，不是靠猜，是根据接口文档精确配置。  
> 抓住四大模块（Method+URL+Headers+Body），理解数据流向，就能发出正确的接口请求！
