# wx2md - 微信文章转 Markdown 工具

## 快速开始

### 1. 安装依赖（首次使用）

```bash
cd wx2md

# 安装 Python 依赖
pip install -r requirements.txt

# 安装 Playwright 浏览器（只需一次）
playwright install chromium
```

### 2. 粘贴文章链接

打开 `links.txt`，把微信文章链接贴进去，**每行一个**：

```
https://mp.weixin.qq.com/s/xxxxxxxxx
https://mp.weixin.qq.com/s/yyyyyyyyy
```

> 获取链接方式：PC 微信打开文章 → 右上角菜单 → 复制链接地址

### 3. 运行脚本

```bash
python wx2md.py
```

### 4. 查看结果

生成的 Markdown 文件保存在 `output/` 目录下：

```
output/
├── 2026-06-14-文章标题A/
│   ├── article.md      ← 正文（Markdown 格式）
│   └── images/         ← 文章中的图片
│       ├── img_001.png
│       └── img_002.jpg
├── 2026-06-14-文章标题B/
│   ├── article.md
│   └── images/
```

每篇文章一个独立文件夹，图片本地化保存，Markdown 中用相对路径引用。

---

## 文章元数据

每个 `article.md` 顶部包含 YAML frontmatter，方便后续检索：

```yaml
---
title: 文章标题
author: 公众号名称
date: 2026-06-14
url: https://mp.weixin.qq.com/s/xxxxx
captured_at: 2026-06-14 00:35:00
---
```

---

## 注意事项

- 仅支持 `mp.weixin.qq.com` 域名的文章链接
- 脚本使用无头浏览器（headless），不会弹出窗口
- 如果抓取失败，可能是微信临时风控，稍后重试即可
- `links.txt` 中的链接处理完后不会自动清空，方便你核对
