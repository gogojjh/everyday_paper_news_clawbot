# nanobot 安装配置指南

> 快速搭建 nanobot AI 助手环境

---

## 📋 目录

1. [环境准备](#1-环境准备)
2. [安装 nanobot](#2-安装-nanobot)
3. [配置 API](#3-配置-api)
4. [安装技能](#4-安装技能)
5. [配置定时任务](#5-配置定时任务)
6. [验证安装](#6-验证安装)

---

## 1. 环境准备

### 系统要求
- **操作系统**: Linux / macOS / Windows (WSL)
- **Python**: 3.11+
- **Git**: 已安装
- **内存**: 至少 2GB 可用

### 检查 Python 版本
```bash
python3 --version
# 应显示 Python 3.11.x 或更高
```

### 创建虚拟环境（推荐）
```bash
python3 -m venv nanobot_env
source nanobot_env/bin/activate  # Linux/macOS
# 或
nanobot_env\Scripts\activate     # Windows
```

---

## 2. 安装 nanobot

### 方法 A: 从源码安装
```bash
git clone https://github.com/gogojjh/nanobot.git
cd nanobot
pip install -e .
```

### 方法 B: 从 PyPI 安装
```bash
pip install nanobot
```

### 验证安装
```bash
nanobot --version
```

---

## 3. 配置 API

### 创建配置文件
```bash
mkdir -p ~/.nanobot/config
nano ~/.nanobot/config/config.json
```

### 配置文件模板
```json
{
  "llm": {
    "default_provider": "dashscope",
    "default_model": "qwen3.5-plus",
    "max_tokens": 8192,
    "temperature": 0.7,
    "max_tool_calls": 20
  },
  "api_keys": {
    "dashscope": "sk-your-api-key-here",
    "deepseek": "sk-your-api-key-here",
    "openrouter": "your-api-key-here",
    "minimax": "your-api-key-here"
  },
  "fallback_chain": [
    "qwen3.5-plus",
    "openrouter/qwen/qwen-2.5-72b-instruct",
    "deepseek-chat",
    "minimax/minimax-01"
  ]
}
```

### 故障转移策略
| 优先级 | 模型 | 用途 |
|--------|------|------|
| 1 | qwen3.5-plus | 主模型 |
| 2 | openrouter/qwen-2.5-72b-instruct | 备用 1 |
| 3 | deepseek-chat | 备用 2 |
| 4 | minimax/minimax-01 | 备用 3 |

---

## 4. 安装技能

### 方法 A: 使用 ClawHub（推荐）
```bash
# 搜索技能
nanobot skill search <keyword>

# 安装技能
nanobot skill install <skill-name>
```

### 方法 B: 手动安装
```bash
# 克隆技能到 skills 目录
git clone <skill-repo-url> ~/.nanobot/workspace/skills/<skill-name>

# 或手动创建技能文件
mkdir -p ~/.nanobot/workspace/skills/<skill-name>
nano ~/.nanobot/workspace/skills/<skill-name>/SKILL.md
```

### 常用技能推荐
| 技能 | 用途 |
|------|------|
| `memory` | 记忆管理 |
| `cron` | 定时任务 |
| `weather` | 天气查询 |
| `jina-reader` | 网页内容提取 |
| `tavily-search` | 网络搜索 |
| `browser-use` | 浏览器自动化 |
| `tmux` | 远程终端管理 |

### 验证技能
```bash
nanobot skill list
```

---

## 5. 配置定时任务

### 添加定时任务
```bash
# 使用 cron 表达式
nanobot cron add --cron "0 8 * * *" --message "每日 arXiv 监控"

# 或使用间隔（秒）
nanobot cron add --every-seconds 86400 --message "每日任务"
```

### 常用 cron 表达式
| 表达式 | 含义 |
|--------|------|
| `0 8 * * *` | 每天 8:00 |
| `0 22 * * *` | 每天 22:00 |
| `*/30 * * * *` | 每 30 分钟 |
| `0 * * * *` | 每小时 |

### 查看任务列表
```bash
nanobot cron list
```

### 移除任务
```bash
nanobot cron remove --job-id <task-id>
```

### 示例：arXiv 监控任务
```bash
nanobot cron add \
  --cron "0 8 * * *" \
  --message "arXiv Robotics 论文监控" \
  --tz "Asia/Shanghai"
```

---

## 6. 验证安装

### 检查进程状态
```bash
ps aux | grep nanobot
```

### 运行状态检查
```bash
nanobot status
```

### 测试技能
```bash
# 测试天气技能
nanobot ask "今天天气怎么样？"

# 测试搜索技能
nanobot ask "搜索最新的机器人论文"
```

### 检查日志
```bash
tail -f ~/.nanobot/logs/nanobot.log
```

---

## 🔧 故障排除

### 常见问题

#### 1. API 密钥无效
```bash
# 检查配置文件
cat ~/.nanobot/config/config.json
# 确认 API key 格式正确且未过期
```

#### 2. 技能无法加载
```bash
# 检查技能目录结构
ls -la ~/.nanobot/workspace/skills/
# 确保每个技能都有 SKILL.md 文件
```

#### 3. 定时任务不执行
```bash
# 检查 cron 任务列表
nanobot cron list
# 确认 nanobot 进程正在运行
ps aux | grep nanobot
```

#### 4. 内存不足
```bash
# 清理旧日志
rm ~/.nanobot/logs/*.log.*
# 重启 nanobot
nanobot restart
```

---

## 📚 进阶配置

### 自定义工作空间
```bash
export NANOBOT_WORKSPACE=/path/to/your/workspace
```

### 配置代理
```bash
export HTTP_PROXY=http://proxy-server:port
export HTTPS_PROXY=http://proxy-server:port
```

### 启用调试模式
```bash
export NANOBOT_DEBUG=1
nanobot run --debug
```

---

## 📞 支持

- **GitHub**: https://github.com/gogojjh/nanobot
- **文档**: ~/.nanobot/workspace/docs/
- **技能市场**: https://clawhub.io

---

*最后更新: 2026-02-25*
