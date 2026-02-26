#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
arXiv Robotics 论文每日监控
筛选方向：Lifelong/Long-term SLAM, Navigation, 铰接式物体操作
使用 DeepSeek 进行中文摘要翻译

用户要求：
1. 报告命名：daily_report_{YYYY-MM-DD}.md（不覆盖历史数据）
2. 完整作者列表 + 附属单位
3. 分析是否提供开源模型/代码
4. 回复当前搜索关键词

配置说明：
- 所有配置项存储在 config.json 中
- 修改配置请编辑 config.json 文件
"""

import json
import urllib.request
import urllib.parse
from datetime import datetime, timedelta
from pathlib import Path
import http.client
import ssl
import subprocess
import shutil
import os
import re

# ============================================================================
# 配置加载
# ============================================================================

CONFIG_PATH = Path(__file__).parent / 'config.json'

def load_config():
    """从 config.json 加载配置"""
    try:
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config
    except Exception as e:
        print(f"⚠️ 读取 config.json 失败：{e}")
        return {}

def load_deepseek_config(config):
    """从 config.json 加载 DeepSeek 配置"""
    nanobot_config_path = Path('/home/jjiao/.nanobot/config.json')
    try:
        with open(nanobot_config_path, 'r', encoding='utf-8') as f:
            nanobot_config = json.load(f)
        providers = nanobot_config.get('providers', {})
        deepseek = providers.get('deepseek', {})
        return {
            'api_key': deepseek.get('apiKey', ''),
            'api_base': deepseek.get('apiBase', 'https://api.deepseek.com'),
            'model': deepseek.get('model', 'deepseek-chat')
        }
    except Exception as e:
        print(f"⚠️ 读取 nanobot config.json 失败：{e}")
        return {
            'api_key': '',
            'api_base': 'https://api.deepseek.com',
            'model': 'deepseek-chat'
        }

# 加载全局配置
CONFIG = load_config()

# DeepSeek 配置
deepseek_config = load_deepseek_config(CONFIG)
DEEPSEEK_API_KEY = deepseek_config['api_key']
DEEPSEEK_API_BASE = deepseek_config['api_base'] if deepseek_config['api_base'] else 'https://api.deepseek.com'
DEEPSEEK_MODEL = deepseek_config.get('model', 'deepseek-chat')

# arXiv 分类
ARXIV_CATEGORIES = CONFIG.get('arxiv_categories', ['cs.RO', 'cs.AI', 'cs.CV'])

# 搜索关键词
KEYWORDS = CONFIG.get('keywords', {})

# Highlight 关键词（高优先级）
HIGHLIGHT_KEYWORDS = CONFIG.get('highlight_keywords', [])

# Highlight 作者列表
HIGHLIGHT_AUTHORS = CONFIG.get('highlight_authors', [])

# 路径配置
PATHS = CONFIG.get('paths', {})
WORKSPACE_DIR = Path(PATHS.get('workspace', '/home/jjiao/.nanobot/workspace'))
ARXIV_MONITOR_DIR = Path(PATHS.get('arxiv_monitor', '/home/jjiao/.nanobot/workspace/arxiv_monitor'))
PDF_STORAGE_DIR = Path(PATHS.get('pdf_storage', ARXIV_MONITOR_DIR / 'papers_pdf'))
GITIGNORE_PATH = Path(PATHS.get('gitignore', ARXIV_MONITOR_DIR / '.gitignore'))

# 确保目录存在
PDF_STORAGE_DIR.mkdir(parents=True, exist_ok=True)

# 创建 .gitignore 文件
if not GITIGNORE_PATH.exists():
    with open(GITIGNORE_PATH, 'w') as f:
        f.write("# PDF 文件不推送到 GitHub\npapers_pdf/\n*.pdf\n")

# 过滤配置
FILTERS = CONFIG.get('filters', {})
MAX_DAYS_OLD = FILTERS.get('max_days_old', 3)
MIN_PAPERS = FILTERS.get('min_papers', 13)
MAX_PAPERS = FILTERS.get('max_papers', 20)

# GitHub 配置
GITHUB_CONFIG = CONFIG.get('github', {})
GITHUB_USERNAME = GITHUB_CONFIG.get('username', 'gogojjh')
GITHUB_REPO = GITHUB_CONFIG.get('repo_name', 'everyday_paper_news_clawbot')
GITHUB_BRANCH = GITHUB_CONFIG.get('branch', 'main')
GITHUB_TAG_PREFIX = GITHUB_CONFIG.get('tag_prefix', 'arxiv-daily-')

# 翻译配置
TRANSLATION_CONFIG = CONFIG.get('translation', {})
TRANSLATION_MAX_LENGTH = TRANSLATION_CONFIG.get('max_abstract_length', 2000)
TRANSLATION_TEMPERATURE = TRANSLATION_CONFIG.get('temperature', 0.3)
TRANSLATION_MAX_TOKENS = TRANSLATION_CONFIG.get('max_tokens', 1024)

# ============================================================================
# 核心功能函数
# ============================================================================

def translate_to_chinese(text, max_length=TRANSLATION_MAX_LENGTH):
    """使用 DeepSeek 翻译摘要为中文"""
    if not text or len(text.strip()) == 0:
        return "无摘要"
    
    if len(text) > max_length:
        text = text[:max_length] + "..."
    
    try:
        url = f"{DEEPSEEK_API_BASE}/v1/chat/completions"
        
        payload = {
            "model": DEEPSEEK_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": "你是一位专业的学术论文翻译助手。请将英文摘要翻译成流畅、准确的中文，保持专业术语的准确性。只输出翻译结果，不要添加任何解释。"
                },
                {
                    "role": "user",
                    "content": f"请将以下论文摘要翻译成中文：\n\n{text}"
                }
            ],
            "temperature": TRANSLATION_TEMPERATURE,
            "max_tokens": TRANSLATION_MAX_TOKENS
        }
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
        }
        
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(url, data=data, headers=headers, method='POST')
        
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        
        with urllib.request.urlopen(req, timeout=60, context=context) as response:
            result = json.loads(response.read().decode('utf-8'))
        
        translation = result.get('choices', [{}])[0].get('message', {}).get('content', '')
        return translation.strip() if translation else "翻译失败"
        
    except Exception as e:
        print(f"  ⚠️ 翻译失败：{e}")
        return f"[翻译失败：{str(e)[:50]}...]"

def parse_arxiv_response(xml_data):
    """解析 arXiv API 的 XML 响应（包含作者单位）"""
    import xml.etree.ElementTree as ET
    
    papers = []
    try:
        root = ET.fromstring(xml_data)
        ns = {'atom': 'http://www.w3.org/2005/Atom',
              'arxiv': 'http://arxiv.org/schemas/atom'}
        
        for entry in root.findall('atom:entry', ns):
            title_elem = entry.find('atom:title', ns)
            summary_elem = entry.find('atom:summary', ns)
            published_elem = entry.find('atom:published', ns)
            id_elem = entry.find('atom:id', ns)
            
            authors = []
            affiliations = []
            for author in entry.findall('atom:author', ns):
                name_elem = author.find('atom:name', ns)
                if name_elem is not None and name_elem.text:
                    authors.append(name_elem.text.strip())
                aff_elem = author.find('arxiv:affiliation', ns)
                if aff_elem is not None and aff_elem.text:
                    affiliations.append(aff_elem.text.strip())
            
            if title_elem is not None and summary_elem is not None:
                paper = {
                    'title': title_elem.text.strip() if title_elem.text else '',
                    'summary': summary_elem.text.strip() if summary_elem.text else '',
                    'published': published_elem.text if published_elem is not None else '',
                    'arxiv_id': id_elem.text if id_elem is not None else '',
                    'authors': authors,
                    'affiliations': affiliations if affiliations else ["附属单位未提供"]
                }
                papers.append(paper)
    except Exception as e:
        print(f"  ⚠️ XML 解析失败：{e}")
    
    return papers

def search_arxiv(query, max_results=50):
    """搜索 arXiv API"""
    base_url = "http://export.arxiv.org/api/query?"
    
    search_query = urllib.parse.quote(f"(cat:{' OR cat:'.join(ARXIV_CATEGORIES)}) AND ({query})")
    url = f"{base_url}search_query={search_query}&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            data = response.read().decode('utf-8')
        return parse_arxiv_response(data)
    except Exception as e:
        print(f"搜索失败：{e}")
        return []

def detect_open_source(paper):
    """检测论文是否提供开源代码/模型"""
    title = paper.get('title', '').lower()
    summary = paper.get('summary', '').lower()
    text = title + ' ' + summary
    
    open_source_indicators = {
        'github': ['github.com', 'github repo', 'github repository', 'our github'],
        'gitlab': ['gitlab.com', 'gitlab repo'],
        'code': ['code available', 'source code', 'open source', 'opensource', 
                 'open-source', 'publicly available', 'code repository'],
        'model': ['pre-trained model', 'model weights', 'checkpoints available', 
                  'model available', 'download model'],
        'project_page': ['project page', 'project website', 'demo page'],
        'huggingface': ['huggingface', 'hugging face', 'hf.co']
    }
    
    found = []
    for category, keywords in open_source_indicators.items():
        for kw in keywords:
            if kw in text:
                found.append(category.upper())
                break
    
    urls = []
    url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
    matches = re.findall(url_pattern, paper.get('summary', ''))
    for url in matches:
        if any(domain in url.lower() for domain in ['github', 'gitlab', 'huggingface']):
            urls.append(url)
    
    return {
        'has_open_source': len(found) > 0,
        'categories': list(set(found)),
        'urls': urls[:3]
    }

def download_pdf(paper, storage_dir=PDF_STORAGE_DIR):
    """下载高亮论文的 PDF 文件"""
    arxiv_id = paper.get('arxiv_id', '')
    title = paper.get('title', '')
    
    if not arxiv_id:
        print(f"  ⚠️ 缺少 arxiv_id，跳过下载")
        return None
    
    arxiv_id_clean = arxiv_id.split('/')[-1]
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id_clean}.pdf"
    
    safe_title = re.sub(r'[<>:"/\\|？*]', '', title)
    safe_title = safe_title.replace(' ', '_')
    if len(safe_title) > 100:
        safe_title = safe_title[:100]
    
    filename = f"{arxiv_id_clean}_{safe_title}.pdf"
    pdf_path = storage_dir / filename
    
    if pdf_path.exists():
        print(f"  ✅ PDF 已存在：{filename}")
        return str(pdf_path)
    
    try:
        print(f"  📥 下载：{pdf_url}")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        req = urllib.request.Request(pdf_url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=60) as response:
            with open(pdf_path, 'wb') as out_file:
                out_file.write(response.read())
        
        print(f"  ✅ 下载成功：{filename}")
        return str(pdf_path)
        
    except Exception as e:
        print(f"  ❌ 下载失败：{e}")
        return None

def filter_papers(papers, keywords):
    """筛选相关论文"""
    filtered = []
    
    for paper in papers:
        title_lower = paper['title'].lower()
        summary_lower = paper['summary'].lower()
        text = title_lower + ' ' + summary_lower
        
        match_category = None
        match_keywords = []
        
        for category, kw_list in keywords.items():
            for kw in kw_list:
                if kw.lower() in text:
                    if match_category is None:
                        match_category = category
                    match_keywords.append(kw)
        
        if match_category:
            paper['match_category'] = match_category
            paper['match_keywords'] = list(set(match_keywords))
            filtered.append(paper)
    
    return filtered

def save_results(papers, output_path):
    """保存结果到 JSON 文件"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    existing_data = []
    if output_path.exists():
        try:
            with open(output_path, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
        except:
            existing_data = []
    
    existing_ids = {p.get('arxiv_id', '') for p in existing_data}
    new_papers = [p for p in papers if p.get('arxiv_id', '') not in existing_ids]
    
    all_papers = new_papers + existing_data
    all_papers.sort(key=lambda x: x.get('published', ''), reverse=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_papers, f, ensure_ascii=False, indent=2)
    
    return len(new_papers)

def is_highlight_paper(paper):
    """检查论文是否属于 Highlight 类别"""
    title = paper.get('title', '').lower()
    summary = paper.get('summary', '').lower()
    text = title + ' ' + summary
    
    for kw in HIGHLIGHT_KEYWORDS:
        if kw.lower() in text:
            return True
    
    authors = paper.get('authors', [])
    for author in authors:
        if author in HIGHLIGHT_AUTHORS:
            return True
    
    return False

def generate_markdown_report(papers, report_path, search_keywords):
    """生成 Markdown 报告"""
    report_path.parent.mkdir(parents=True, exist_ok=True)
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    highlight_papers = [p for p in papers if is_highlight_paper(p)]
    poster_papers = [p for p in papers if not is_highlight_paper(p)]
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(f"# 📚 arXiv Robotics 论文日报\n\n")
        f.write(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(f"**今日新增**: {len(papers)} 篇\n\n")
        f.write(f"**搜索关键词**: `{' | '.join(search_keywords)}`\n\n")
        f.write("---\n\n")
        
        open_source_count = sum(1 for p in papers if p.get('open_source', {}).get('has_open_source', False))
        f.write(f"**🔓 开源代码/模型**: {open_source_count}/{len(papers)} 篇提供\n\n")
        f.write(f"**🌟 Highlight**: {len(highlight_papers)} 篇 | **📌 Poster**: {len(poster_papers)} 篇\n\n")
        f.write("---\n\n")
        
        if highlight_papers:
            f.write(f"## 🌟 Highlight\n\n")
            f.write(f"*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*\n\n")
            f.write("---\n\n")
            
            for i, paper in enumerate(highlight_papers, 1):
                f.write(f"### {i}. {paper['title']}\n\n")
                
                all_authors = ', '.join(paper['authors'])
                highlighted_author_names = [a for a in paper['authors'] if a in HIGHLIGHT_AUTHORS]
                
                if highlighted_author_names:
                    f.write(f"- **作者**: {all_authors} ⭐\n")
                    f.write(f"  - **高亮作者**: {', '.join(highlighted_author_names)}\n")
                else:
                    f.write(f"- **作者**: {all_authors}\n")
                
                affiliations = paper.get('affiliations', [])
                if affiliations and affiliations[0] != "附属单位未提供" and not affiliations[0].startswith("获取失败"):
                    f.write(f"- **单位**: {'; '.join(affiliations[:3])}{'...' if len(affiliations) > 3 else ''}\n")
                else:
                    f.write(f"- **单位**: 详见 [arXiv 页面]({paper['arxiv_id']})\n")
                
                f.write(f"- **发表日期**: {paper['published'][:10]}\n")
                f.write(f"- **匹配关键词**: {', '.join(paper.get('match_keywords', []))}\n")
                f.write(f"- **arXiv**: [{paper['arxiv_id'].split('/')[-1]}]({paper['arxiv_id']})\n")
                
                if paper.get('pdf_path'):
                    pdf_name = Path(paper['pdf_path']).name
                    f.write(f"- **📥 PDF**: 已下载至本地 (`{pdf_name}`)\n")
                
                open_source = paper.get('open_source', {})
                if open_source.get('has_open_source', False):
                    f.write(f"- **🔓 开源**: {', '.join(open_source.get('categories', []))}\n")
                    if open_source.get('urls'):
                        f.write(f"  - 链接：{', '.join(open_source['urls'])}\n")
                else:
                    f.write(f"- **🔒 开源**: 未提及\n")
                
                chinese_summary = paper.get('chinese_summary', '')
                if chinese_summary:
                    f.write(f"- **中文摘要**: {chinese_summary}\n\n")
                else:
                    f.write(f"- **摘要**: {paper['summary'][:500]}{'...' if len(paper['summary']) > 500 else ''}\n\n")
                
                f.write("---\n\n")
        
        if poster_papers:
            f.write(f"## 📌 Poster\n\n")
            f.write(f"*其他相关研究*\n\n")
            f.write("---\n\n")
            
            for i, paper in enumerate(poster_papers, 1):
                f.write(f"### {i}. {paper['title']}\n\n")
                
                all_authors = ', '.join(paper['authors'])
                highlighted_author_names = [a for a in paper['authors'] if a in HIGHLIGHT_AUTHORS]
                
                if highlighted_author_names:
                    f.write(f"- **作者**: {all_authors} ⭐\n")
                    f.write(f"  - **高亮作者**: {', '.join(highlighted_author_names)}\n")
                else:
                    f.write(f"- **作者**: {all_authors}\n")
                
                affiliations = paper.get('affiliations', [])
                if affiliations and affiliations[0] != "附属单位未提供" and not affiliations[0].startswith("获取失败"):
                    f.write(f"- **单位**: {'; '.join(affiliations[:3])}{'...' if len(affiliations) > 3 else ''}\n")
                else:
                    f.write(f"- **单位**: 详见 [arXiv 页面]({paper['arxiv_id']})\n")
                
                f.write(f"- **发表日期**: {paper['published'][:10]}\n")
                f.write(f"- **匹配关键词**: {', '.join(paper.get('match_keywords', []))}\n")
                f.write(f"- **arXiv**: [{paper['arxiv_id'].split('/')[-1]}]({paper['arxiv_id']})\n")
                
                if paper.get('pdf_path'):
                    pdf_name = Path(paper['pdf_path']).name
                    f.write(f"- **📥 PDF**: 已下载至本地 (`{pdf_name}`)\n")
                else:
                    f.write(f"- **📥 PDF**: 未下载（仅高亮论文自动下载）\n")
                
                open_source = paper.get('open_source', {})
                if open_source.get('has_open_source', False):
                    f.write(f"- **🔓 开源**: {', '.join(open_source.get('categories', []))}\n")
                    if open_source.get('urls'):
                        f.write(f"  - 链接：{', '.join(open_source['urls'])}\n")
                else:
                    f.write(f"- **🔒 开源**: 未提及\n")
                
                chinese_summary = paper.get('chinese_summary', '')
                if chinese_summary:
                    f.write(f"- **中文摘要**: {chinese_summary}\n\n")
                else:
                    f.write(f"- **摘要**: {paper['summary'][:500]}{'...' if len(paper['summary']) > 500 else ''}\n\n")
                
                f.write("---\n\n")
    
    return report_path

def update_readme(repo_local_path: str, papers_count: int):
    """更新 README.md"""
    import re
    
    today = datetime.now().strftime('%Y-%m-%d')
    report_filename = f'arxiv_daily_report_{today}.md'
    readme_path = Path(repo_local_path) / 'README.md'
    
    if readme_path.exists():
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        content = f"""# 📚 arXiv Robotics Daily Report

每日自动推送 arXiv 机器人学相关论文摘要和翻译。

---

## 📄 历史报告

| 日期 | 报告链接 | 论文数量 |
|------|----------|----------|

---

## 📋 搜索范围

| 分类 | 说明 |
|------|------|
| **cs.RO** | Robotics |
| **cs.AI** | Artificial Intelligence |
| **cs.CV** | Computer Vision |

---

*最后更新：{today}*
"""
    
    if f'[{report_filename}]' in content:
        print(f"⚠️ 今日报告已在 README 中，跳过更新")
        return
    
    new_row = f"| {today} | [{report_filename}](./{report_filename}) | {papers_count} 篇 |\n"
    
    table_header = "| 日期 | 报告链接 | 论文数量 |\n|------|----------|----------|"
    if table_header in content:
        if table_header + "\n" in content:
            content = content.replace(table_header + "\n", table_header + "\n" + new_row, 1)
        else:
            content = content.replace(table_header, table_header + "\n" + new_row, 1)
    else:
        section_header = "## 📄 历史报告"
        if section_header in content:
            idx = content.find(section_header) + len(section_header)
            content = content[:idx] + "\n\n| 日期 | 报告链接 | 论文数量 |\n|------|----------|----------|\n" + new_row + content[idx:]
    
    content = re.sub(r'\*最后更新：[^*]+\*', f'*最后更新：{today}*', content)
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"📝 README.md 已更新")


def push_to_github(report_path: str, papers_count: int):
    """推送日报到 GitHub 并创建日期 Tag"""
    
    config_path = Path('/home/jjiao/.nanobot/config.json')
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        github_config = config.get('integrations', {}).get('github', {})
        username = github_config.get('username', GITHUB_USERNAME)
        token = github_config.get('token', '')
        repo_name = github_config.get('defaultRepo', GITHUB_REPO)
        repo_url = github_config.get('repoUrl', f'https://github.com/{username}/{repo_name}.git')
    except Exception as e:
        print(f"⚠️ 读取 GitHub 配置失败：{e}")
        return False
    
    today = datetime.now().strftime('%Y-%m-%d')
    tag_name = f'{GITHUB_TAG_PREFIX}{today}'
    repo_local_path = Path(f'/home/jjiao/.nanobot/workspace/{repo_name}')
    
    try:
        if not repo_local_path.exists():
            print(f"📥 克隆仓库：{repo_url}")
            auth_url = repo_url.replace('https://', f'https://{username}:{token}@')
            subprocess.run(['git', 'clone', auth_url, str(repo_local_path)], check=True, timeout=60)
        else:
            print(f"🔄 拉取最新代码：{repo_local_path}")
            subprocess.run(['git', '-C', str(repo_local_path), 'pull'], check=True, timeout=30)
        
        report_filename = report_path.name
        dest_path = repo_local_path / report_filename
        shutil.copy(report_path, dest_path)
        print(f"📄 复制报告：{report_filename}")
        
        update_readme(str(repo_local_path), papers_count)
        
        gitignore_src = GITIGNORE_PATH
        gitignore_dest = repo_local_path / '.gitignore'
        if gitignore_src.exists() and not gitignore_dest.exists():
            shutil.copy(gitignore_src, gitignore_dest)
            print(f"📄 复制 .gitignore 到仓库")
        
        subprocess.run(['git', '-C', str(repo_local_path), 'config', 'user.name', 'nanobot'], check=True)
        subprocess.run(['git', '-C', str(repo_local_path), 'config', 'user.email', 'nanobot@local'], check=True)
        subprocess.run(['git', '-C', str(repo_local_path), 'add', report_filename, 'README.md', '.gitignore'], check=True)
        subprocess.run(['git', '-C', str(repo_local_path), 'commit', '-m', f'📚 arXiv daily report {today}'], check=True)
        
        auth_url = repo_url.replace('https://', f'https://{username}:{token}@')
        subprocess.run(['git', '-C', str(repo_local_path), 'push', auth_url, GITHUB_BRANCH], check=True, timeout=60)
        print(f"✅ 推送到 GitHub: {GITHUB_BRANCH} 分支")
        
        result = subprocess.run(['git', '-C', str(repo_local_path), 'tag', '-l', tag_name], 
                               capture_output=True, text=True)
        if tag_name in result.stdout:
            print(f"⚠️ Tag {tag_name} 已存在，删除后重新创建")
            subprocess.run(['git', '-C', str(repo_local_path), 'tag', '-d', tag_name], check=True)
            subprocess.run(['git', '-C', str(repo_local_path), 'push', auth_url, '--delete', tag_name], 
                          capture_output=True)
        
        subprocess.run(['git', '-C', str(repo_local_path), 'tag', tag_name, '-m', f'arXiv daily report {today}'], check=True)
        subprocess.run(['git', '-C', str(repo_local_path), 'push', auth_url, tag_name], check=True, timeout=30)
        print(f"🏷️ 创建并推送 Tag: {tag_name}")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Git 操作失败：{e}")
        return False
    except subprocess.TimeoutExpired as e:
        print(f"❌ Git 操作超时：{e}")
        return False
    except Exception as e:
        print(f"❌ GitHub 推送失败：{e}")
        return False


def main():
    """主函数"""
    output_dir = ARXIV_MONITOR_DIR
    json_path = output_dir / 'papers_history.json'
    
    today = datetime.now().strftime('%Y-%m-%d')
    report_path = output_dir / f'arxiv_daily_report_{today}.md'
    
    print(f"🔍 开始搜索 arXiv Robotics 论文...")
    
    # 从配置加载搜索查询
    SEARCH_QUERIES = CONFIG.get('search_queries', [])
    
    all_papers = []
    for query in SEARCH_QUERIES:
        print(f"  搜索：{query[:60]}...")
        papers = search_arxiv(query, max_results=50)
        filtered = filter_papers(papers, KEYWORDS)
        all_papers.extend(filtered)
        print(f"    找到 {len(filtered)} 篇相关论文")
    
    seen_ids = set()
    unique_papers = []
    today_dt = datetime.now()
    
    for p in all_papers:
        if p['arxiv_id'] in seen_ids:
            continue
        
        try:
            published_date = datetime.strptime(p['published'][:10], '%Y-%m-%d')
            days_diff = (today_dt - published_date).days
            if days_diff > MAX_DAYS_OLD:
                continue
        except:
            pass
        
        seen_ids.add(p['arxiv_id'])
        unique_papers.append(p)
    
    highlight_papers = [p for p in unique_papers if is_highlight_paper(p)]
    normal_papers = [p for p in unique_papers if not is_highlight_paper(p)]
    
    final_papers = highlight_papers.copy()
    
    if len(final_papers) >= MAX_PAPERS:
        final_papers = final_papers[:MAX_PAPERS]
    else:
        remaining_slots = MAX_PAPERS - len(final_papers)
        final_papers.extend(normal_papers[:remaining_slots])
    
    if len(final_papers) < MIN_PAPERS and len(normal_papers) > remaining_slots:
        additional_needed = MIN_PAPERS - len(final_papers)
        final_papers.extend(normal_papers[remaining_slots:remaining_slots + additional_needed])
    
    unique_papers = final_papers
    
    print(f"\n📊 去重 + 过滤后共 {len(unique_papers)} 篇论文（最近 {MAX_DAYS_OLD} 天，范围 {MIN_PAPERS}-{MAX_PAPERS} 篇）")
    print(f"   - Highlight: {len(highlight_papers)} 篇 | Poster: {len(unique_papers) - len(highlight_papers)} 篇")
    
    print(f"\n🔍 获取开源状态...")
    for i, paper in enumerate(unique_papers):
        print(f"  [{i+1}/{len(unique_papers)}] {paper['title'][:50]}...")
        paper['open_source'] = detect_open_source(paper)
    
    print(f"\n🌐 开始翻译摘要为中文（使用 DeepSeek）...")
    for i, paper in enumerate(unique_papers):
        print(f"  [{i+1}/{len(unique_papers)}] 翻译：{paper['title'][:50]}...")
        chinese_summary = translate_to_chinese(paper['summary'])
        paper['chinese_summary'] = chinese_summary
    
    print(f"\n📥 开始下载高亮论文 PDF...")
    downloaded_pdfs = []
    for i, paper in enumerate(unique_papers):
        if is_highlight_paper(paper):
            print(f"  [{i+1}/{len(unique_papers)}] 高亮论文：{paper['title'][:50]}...")
            pdf_path = download_pdf(paper)
            if pdf_path:
                downloaded_pdfs.append(pdf_path)
                paper['pdf_path'] = pdf_path
        else:
            print(f"  [{i+1}/{len(unique_papers)}] 跳过（非高亮）：{paper['title'][:50]}...")
    
    print(f"\n💾 共下载 {len(downloaded_pdfs)} 篇高亮论文 PDF")
    if downloaded_pdfs:
        print(f"📂 PDF 存储目录：{PDF_STORAGE_DIR}")
    
    new_count = save_results(unique_papers, json_path)
    print(f"\n💾 保存成功！新增 {new_count} 篇，历史共 {len(unique_papers)} 篇")
    
    generate_markdown_report(unique_papers, report_path, SEARCH_QUERIES)
    print(f"📄 报告已生成：{report_path}")
    
    print(f"\n🔑 本次搜索关键词:")
    for i, kw in enumerate(SEARCH_QUERIES, 1):
        print(f"  {i}. {kw}")
    
    print(f"\n🚀 开始推送到 GitHub...")
    github_success = push_to_github(report_path, len(unique_papers))
    if github_success:
        print(f"✅ GitHub 推送成功！")
    else:
        print(f"❌ GitHub 推送失败，请检查配置和网络")
    
    return unique_papers

if __name__ == '__main__':
    main()
