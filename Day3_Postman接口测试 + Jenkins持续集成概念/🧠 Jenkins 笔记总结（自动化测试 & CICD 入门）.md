# 🧠 Jenkins 笔记总结（自动化测试 & CI/CD 入门）

---

## 1. Jenkins 是什么？

- Jenkins 是一个开源的持续集成（CI）工具。
- 用于自动执行：拉取代码、安装依赖、运行测试、生成报告、部署应用等流程。
- 是整个自动化流程的中控器，提升开发测试效率、减少人为操作。

---

## 2. Jenkins 的核心概念

- **Job**：最基本的构建任务单元，一个 Job 就是一条流水线任务。
- **Workspace**：每个 Job 执行时的工作目录，用于存放临时代码、依赖、输出结果等。
- **Pipeline**：使用 Groovy DSL 编写的构建流程脚本，可定义多阶段任务，灵活可控。

---

## 3. Jenkins 的典型流水线流程

**开发者提交代码 ➜ Jenkins 监听触发 ➜ 自动执行以下步骤：**

- 拉取代码
- 安装依赖
- 编译/构建项目
- 执行自动化测试
- 生成测试报告
- 部署到测试/生产环境
- 通知相关人员

---

## 4. Jenkins 的构建触发方式（Build Triggers）

- 定时触发（如每天凌晨构建一次）
- Git 代码变更（推荐使用 Webhook）
- 手动点击构建（Build Now）
- 其他 Job 执行完成后触发
- 调用 Jenkins 的 REST API 接口远程触发

---

## 5. Jenkinsfile 的基本结构（Pipeline 脚本）

- `pipeline`：定义整条流水线
- `agent`：指定构建在哪运行（本地、Docker、远程节点）
- `stages`：定义多个阶段（如 Checkout、Build、Test、Deploy）
- `steps`：阶段中要执行的具体命令（如 `sh`, `git`, `pytest`）

常见步骤包括：
- 拉代码：`git`
- 安装依赖：`pip install -r requirements.txt`
- 运行测试：`pytest`
- 上传部署：`scp` 或用插件传输到目标服务器

```
pipeline {
  agent any
  stages {
    stage('拉代码') {
      steps {
        git 'https://github.com/xxx/repo.git'
      }
    }
    stage('安装依赖') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('测试') {
      steps {
        sh 'pytest'
      }
    }
  }
}
```



---

## 6. 什么是“部署”？

- 部署（Deploy）指将构建好的代码或系统发布到目标环境，让它“上线可用”。
- 通常包括上传文件、重启服务、设置配置等。
- Jenkins 只是自动化执行部署命令的工具，“部署”是项目生命周期中的一个阶段。

---

## 7. Jenkins 和 Docker 的关系

- Jenkins 本身可以通过 Docker 快速部署。
- Jenkins 的 Job 或 Pipeline 可以运行在 Docker 容器中，以保证环境一致、构建隔离。
- 比如使用 `python:3.10` 镜像运行测试环境，避免本地依赖冲突。

你可以将 Docker 理解为“容器级的 Anaconda”，不仅能隔离 Python 包，还能隔离系统级依赖和操作系统行为。

---

## 8. Docker 和操作系统内核的关系

- Docker 容器运行时共享的是**宿主机的内核**。
- 容器具有系统级别的文件系统、网络、进程空间隔离。
- **不能**跨内核运行（Linux 容器必须用 Linux 内核）。
- 因此，在 Mac/Windows 上运行 Docker 时，会自动创建一个**隐藏的 Linux 虚拟机（Linux VM）**，容器实际运行在这个 VM 中。

---

## 9. SSH 是什么？与 Jenkins 的关系？

- SSH（Secure Shell）是远程安全登录协议。
- Jenkins 可以通过 SSH 远程连接目标服务器，用于：
  - 上传构建产物（如 `scp` 命令）
  - 执行远程部署命令
- 常见方式是配置免密 SSH key 实现自动化传输与控制。

---

## 10. 在 Jenkins 中指定 Python 运行环境的方式

- 在 Pipeline 的 Shell 脚本中，显式指定 Python 路径：
  - 例如：`/opt/py310/bin/python main.py`
- 使用虚拟环境（venv）：
  - `python -m venv venv && source venv/bin/activate`
- 或使用 Docker 容器提供标准环境：
  - 指定 `python:3.10` 镜像，在其中执行脚本

---

## 11. Jenkins 常见面试八股题汇总

1. Jenkins 是什么？—— 持续集成工具，用于自动化构建测试流程。
2. CI/CD 是什么？—— 持续集成/持续部署，提升开发效率与质量。
3. Jenkins 的工作流程？—— 监听代码变更 ➜ 构建 ➜ 测试 ➜ 部署 ➜ 通知。
4. 什么是 Pipeline？—— 可编程构建流程脚本，更灵活可复用。
5. 如何触发构建？—— Webhook、定时、手动、API。
6. Jenkins 和 Docker 有何关系？—— Docker 提供环境隔离，Jenkins 调用它执行构建。
7. 如何部署到远程服务器？—— 配置 SSH 密钥，使用 `scp` 或插件传输文件。
8. 什么是 Workspace？—— Job 执行时的临时目录，保存中间文件与输出。
9. 如何查看构建是否成功？—— Jenkins UI 显示构建状态，可点开日志 Console Output。
