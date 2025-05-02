# 📘 Day 4｜Wireshark 抓包学习笔记

---

## 一、Wireshark 简介

* Wireshark 是一款开源网络抓包工具，能捕获并分析网络通信中的数据包。
* 主要用于：网络排障、协议学习、接口调试、安全分析等。
* 常见抓取内容包括：HTTP、DNS、TCP、ARP、ICMP 等协议流量。

---

## 二、网卡识别

### 使用命令：

```bash
ifconfig
```

找出 `status: active` 且有 `inet` 的接口（如 `en0`）。

<img src="/Users/macbook/Library/Application Support/typora-user-images/image-20250502000755831.png" align="left" width="800">

### 接口混杂模式：

看是否直接收发送到本机mac地址的数据包

---

## 三、核心协议学习

### 1. ARP（地址解析协议）

* 所属层：链路层（OSI 第2层）
* 功能：将 IP 地址解析为 MAC 地址
* 工作方式：

  * 广播 `Who has 192.168.2.4?`
  * 对方回应 `192.168.2.4 is at xx:xx:xx`

### 2. ICMP（互联网控制消息协议）

* 所属层：网络层（OSI 第3层）
* 功能：网络测试与错误报告（如 ping）
* 常见类型：

  * Type 8：Echo Request
  * Type 0：Echo Reply
  * Type 3：Destination Unreachable

### 3. DNS（域名系统）

* 所属层：应用层
* 功能：将域名解析为 IP 地址
* 查询类型：A（IPv4）、AAAA（IPv6）、MX、CNAME 等
* 常用命令：

  * `nslookup www.baidu.com`
  * `dig example.com`
* 在 Wireshark 中可使用过滤器：`dns`

### 4. TCP（Transmission Control Protocol）

* 所属层：传输层

* 特点：有连接（3次握手），可靠传输，顺序保证

* 三次握手：SYN → SYN+ACK → ACK

  <img src="https://networkwalks.com/wp-content/uploads/2020/10/TCP-three-way-handshake-process-dp.png" align="left" width="600">

* 四次挥手：FIN → ACK → FIN → ACK

  [![TCP-Establish and Terminate the connection](https://learningnetwork.cisco.com/sfc/servlet.shepherd/version/renditionDownload?rendition=THUMB720BY480&versionId=0683i000001rpqJ&operationContext=CHATTER&contentId=05T3i00000ACRDR&page=0)

### 5. HTTP（超文本传输协议）

* 所属层：应用层
* 基于 TCP 端口 80
* 无状态，请求-响应结构

#### 常见 HTTP 请求方法对比：

| 方法  | 含义     | 是否幂等 | 是否带请求体 |
| ----- | -------- | -------- | ------------ |
| GET   | 获取资源 | ✅ 是     | ❌ 否         |
| POST  | 提交资源 | ❌ 否     | ✅ 是         |
| PUT   | 整体更新 | ✅ 是     | ✅ 是         |
| PATCH | 局部更新 | ✅/❌      | ✅ 是         |

---

## 四、Wireshark 抓包实操记录

### ARP抓取：

过滤source/destination：ip.src/ ip.dst/ ip.addr == xxx

![image-20250502162341448](/Users/macbook/Library/Application Support/typora-user-images/image-20250502162341448.png)

![image-20250502164114276](/Users/macbook/Library/Application Support/typora-user-images/image-20250502164114276.png)

![image-20250502164150378](/Users/macbook/Library/Application Support/typora-user-images/image-20250502164150378.png)

### TCP抓取过程：

![image-20250502175028746](/Users/macbook/Library/Application Support/typora-user-images/image-20250502175028746.png" align="left" width="800")

### http抓取过程：

* 访问网址：`http://example.com`（HTTP 明文）

* 抓到的典型数据包：

  * GET 请求包
  * 200 OK 响应包（包含 HTML 内容）
  * favicon.ico 请求 + 404 响应
  
  ![image-20250502190749265](/Users/macbook/Library/Application Support/typora-user-images/image-20250502190749265.png)

#### 🧾 报文简析

##### 🟢 No. 172 - `GET / HTTP/1.1`

- 来源：你的本机（192.168.2.4）
- 目标：23.215.0.138（服务器）
- 请求方法：GET
- 请求内容：网页主页 `/`

##### 🟢 No. 178 - `HTTP/1.1 200 OK (text/html)`

- 来源：23.215.0.138（服务器）
- 返回给：你的本机（192.168.2.4）
- 状态码：`200 OK`，表示请求成功
- 内容类型：`text/html`
- **这就是请求主页后返回的网页正文内容！**

### Display Filter 使用示例：

```plaintext
http
tcp
icmp
arp
dns
ip.addr == 192.168.2.4
http.request.method == "GET"
```

---

## 五、协议封装关系总结（从外到内）

```
HTTP ⬅ 应用层协议
└── TCP ⬅ 传输层（可靠通道）
    └── IP ⬅ 网络层（寻址与路由）
        └── Ethernet/Wi-Fi ⬅ 数据链路层（物理传输）
```

> 记忆口诀：HTTP 说话，TCP 送达，IP 找路，以太网搬运

---

## 六、总结

* 成功使用 Wireshark 抓到了 HTTP、DNS、ARP、ICMP 报文。
* 理解了 TCP 三次握手、DNS 域名解析过程和 HTTP 请求头结构。
* 学会了用过滤器查看感兴趣的协议流量，能读懂 GET/200 OK 报文。
* 明白了“有连接”和“无连接”的真正含义。
* 建立了对协议分层结构的清晰理解。
