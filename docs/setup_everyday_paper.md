# arXiv 论文每日监控设置指南

本指南介绍如何配置和运行 arXiv 机器人学论文每日监控系统。

---

## 📋 目录

1. [环境准备](#1-环境准备)
2. [配置文件](#2-配置文件)
3. [API 配置](#3-api-配置)
4. [GitHub 配置](#4-github-配置)
5. [配置关键词](#5-配置关键词)
6. [运行脚本](#6-运行脚本)
7. [验证与调试](#7-验证与调试)
8. [附录：完整配置示例](#附录完整配置示例)

---

## 1. 环境准备

### 系统要求

| 项目 | 要求 |
|------|------|
| **Python** | 3.8+ |
| **操作系统** | Linux / macOS / Windows |
| **网络** | 可访问 arXiv API 和 DeepSeek API |

### 安装依赖

```bash
pip install arxiv requests python-dotenv
```

### 目录结构

```
arxiv_monitor/
├── arxiv_robotics_daily.py    # 主脚本
├── config.json                 # 配置文件（敏感，不上传）
├── config.json.example         # 配置模板（可上传）
├── reports/                    # 生成的报告
├── papers_pdf/                 # 下载的 PDF（不上传）
└── everyday_paper_news_clawbot/ # GitHub 仓库
    ├── README.md
    └── docs/
```

---

## 2. 配置文件

### 创建配置文件

```bash
# 复制模板
cp docs/config.json.example config.json

# 编辑配置
vim config.json
```

### 配置结构

| 配置项 | 说明 | 必填 |
|--------|------|------|
| `arxiv_categories` | arXiv 分类代码 | ✅ |
| `search_queries` | 搜索查询列表 | ✅ |
| `keywords` | 关键词分类 | ✅ |
| `highlight_keywords` | 高亮关键词 | ✅ |
| `highlight_authors` | 高亮作者列表 | ✅ |
| `paths` | 路径配置 | ✅ |
| `filters` | 过滤规则 | ✅ |
| `github` | GitHub 配置 | ✅ |
| `translation` | 翻译配置 | ✅ |

---

## 3. API 配置

### DeepSeek API

1. 访问 https://platform.deepseek.com
2. 注册账号并获取 API Key
3. 在 `config.json` 中配置：

```json
{
  "deepseek": {
    "api_key": "sk-your-api-key-here",
    "base_url": "https://api.deepseek.com",
    "model": "deepseek-chat"
  }
}
```

### 测试 API

```bash
curl https://api.deepseek.com/v1/models \
  -H "Authorization: Bearer sk-your-api-key-here"
```

---

## 4. GitHub 配置

### 生成 Token

1. 访问 https://github.com/settings/tokens
2. 点击 **Generate new token (classic)**
3. 选择权限：`repo` (完整仓库权限)
4. 复制 Token 并保存

### 配置 Token

**方法 1：环境变量（推荐）**
```bash
export GITHUB_TOKEN="ghp_your-token-here"
```

**方法 2：配置文件**
```json
{
  "github": {
    "token": "ghp_your-token-here",
    "repo_url": "https://github.com/your-username/your-repo.git",
    "branch": "main"
  }
}
```

### 测试 Git 访问

```bash
git clone https://github.com/your-username/your-repo.git
```

---

## 5. 配置关键词

### 搜索查询示例

```json
"search_queries": [
  "robotics AND manipulation",
  "vision-language-action OR VLA",
  "diffusion policy AND robot",
  "NeRF OR Gaussian Splatting AND robot",
  "image-goal OR point-goal OR object-goal navigation"
]
```

### 关键词分类

```json
"keywords": {
  "vla": ["vision-language-action", "VLA", "VLA model"],
  "diffusion_policy": ["diffusion policy", "diffusion-based policy"],
  "3d_reconstruction": ["NeRF", "Gaussian Splatting", "3D gaussian"],
  "visual_navigation": ["image-goal", "point-goal", "object-goal"]
}
```

### 高亮规则

匹配以下关键词的论文将被标记为 **Highlight** 并自动下载 PDF：

```json
"highlight_keywords": [
  "humanoid",
  "legged robot",
  "VLA",
  "diffusion policy",
  "NeRF",
  "gaussian splatting",
  "image-goal",
  "point-goal",
  "object-goal"
]
```

### 高亮作者

```json
"highlight_authors": [
  "Chelsea Finn",
  "Sergey Levine",
  "Andrew Davison",
  "Daniel Cremers",
  "Fei Gao"
]
```

---

## 6. 运行脚本

### 手动运行

```bash
cd /home/jjiao/.nanobot/workspace/arxiv_monitor
python arxiv_robotics_daily.py
```

### 定时任务（cron）

每天 8:00 自动运行：

```bash
# 编辑 crontab
crontab -e

# 添加任务
0 8 * * * cd /home/jjiao/.nanobot/workspace/arxiv_monitor && python arxiv_robotics_daily.py >> logs/arxiv.log 2>&1
```

### cron 表达式参考

| 表达式 | 说明 |
|--------|------|
| `0 8 * * *` | 每天 8:00 |
| `0 9 * * 1-5` | 工作日 9:00 |
| `*/30 * * * *` | 每 30 分钟 |

---

## 7. 验证与调试

### 检查日志

```bash
# 查看最新日志
tail -f logs/arxiv.log

# 查看错误
grep ERROR logs/arxiv.log
```

### 常见问题

| 问题 | 解决方案 |
|------|----------|
| API Key 无效 | 检查 DeepSeek API Key 是否正确 |
| Git 推送失败 | 检查 Token 权限和网络连接 |
| PDF 下载失败 | 检查网络连接和存储路径权限 |
| 中文翻译失败 | 检查 DeepSeek API 配额 |

### 测试配置

```bash
python -c "import json; json.load(open('config.json'))"
# 无输出表示配置格式正确
```

---

## 附录：完整配置示例

```json
{
  "arxiv_categories": ["cs.RO", "cs.AI", "cs.CV"],
  "search_queries": [
    "robotics AND manipulation",
    "vision-language-action OR VLA",
    "diffusion policy AND robot",
    "NeRF OR Gaussian Splatting AND robot",
    "image-goal OR point-goal OR object-goal navigation"
  ],
  "keywords": {
    "lifelong_slam": ["lifelong SLAM", "long-term SLAM", "continuous SLAM"],
    "navigation": ["visual navigation", "autonomous navigation", "path planning"],
    "articulated_manipulation": ["articulated object", "affordance", "grasp detection"],
    "scene_graph": ["scene graph", "semantic scene"],
    "interactive_perception": ["interactive perception", "active perception"],
    "mobile_manipulation": ["mobile manipulation", "whole-body control"],
    "vla": ["vision-language-action", "VLA", "VLA model"],
    "diffusion_policy": ["diffusion policy", "diffusion-based policy"],
    "visual_navigation": ["image-goal", "point-goal", "object-goal"],
    "3d_reconstruction": ["NeRF", "Gaussian Splatting", "3D gaussian"]
  },
  "highlight_keywords": [
    "humanoid", "legged robot", "VLA", "diffusion policy",
    "NeRF", "gaussian splatting", "image-goal", "point-goal", "object-goal"
  ],
  "highlight_authors": [
    "Chelsea Finn", "Sergey Levine", "Andrew Davison", "Daniel Cremers",
    "Timothy D Barfoot", "Xiaolong Wang", "Fei Gao", "Wolfram Burgard",
    "Davide Scaramuzza", "Michael Kaess", "Lu Fan", "Chen Wang"
  ],
  "paths": {
    "workspace": "/home/jjiao/.nanobot/workspace/arxiv_monitor",
    "pdf_storage": "papers_pdf",
    "report_dir": "reports",
    "github_repo": "everyday_paper_news_clawbot"
  },
  "filters": {
    "max_days_back": 2,
    "max_papers_per_report": 50,
    "exclude_crosslist": true
  },
  "github": {
    "repo_url": "https://github.com/gogojjh/everyday_paper_news_clawbot.git",
    "branch": "main",
    "token_env": "GITHUB_TOKEN"
  },
  "translation": {
    "enabled": true,
    "model": "deepseek-chat",
    "max_tokens": 500
  },
  "deepseek": {
    "api_key": "sk-your-api-key-here",
    "base_url": "https://api.deepseek.com",
    "model": "deepseek-chat"
  }
}
```

---

## 📚 相关文档

- [nanobot 安装配置指南](setup_nanobot.md)
- [监控脚本源码](arxiv_robotics_daily.py)
- [配置模板](config.json.example)

---

**最后更新**: 2026-02-26
