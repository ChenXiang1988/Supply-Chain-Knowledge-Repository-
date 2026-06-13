"""
wx2md.py - 微信文章批量转 Markdown
用法: python wx2md.py
依赖: pip install -r requirements.txt && playwright install chromium
"""

import asyncio
import base64
import os
import re
from datetime import datetime
from urllib.parse import unquote, urlparse

from bs4 import BeautifulSoup
from markdownify import markdownify as md
from playwright.async_api import async_playwright

# ========== 配置 ==========
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LINKS_FILE = os.path.join(BASE_DIR, "links.txt")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)


def sanitize_filename(name: str) -> str:
    """清理文件名中的非法字符，限制长度"""
    name = re.sub(r'[\\/*?:"<>|]', "_", name)
    name = name.strip().strip(".")
    return name[:100]


def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)


async def download_image(page, img_url: str, img_dir: str, img_name: str) -> str | None:
    """通过 Playwright 在浏览器上下文中下载图片，绕过微信防盗链"""
    try:
        js_code = f"""
        async () => {{
            const resp = await fetch("{img_url}", {{
                headers: {{ "Referer": "https://mp.weixin.qq.com/" }}
            }});
            const blob = await resp.blob();
            return new Promise((resolve) => {{
                const reader = new FileReader();
                reader.onloadend = () => resolve(reader.result);
                reader.readAsDataURL(blob);
            }});
        }}
        """
        data_url = await page.evaluate(js_code)
        if data_url and data_url.startswith("data:image"):
            header, b64 = data_url.split(",", 1)
            ext = "png"
            if "jpeg" in header or "jpg" in header:
                ext = "jpg"
            elif "gif" in header:
                ext = "gif"
            elif "webp" in header:
                ext = "webp"

            img_path = os.path.join(img_dir, f"{img_name}.{ext}")
            with open(img_path, "wb") as f:
                f.write(base64.b64decode(b64))
            return f"{img_name}.{ext}"
    except Exception as e:
        print(f"  [图片下载失败] {img_url}: {e}")
    return None


async def process_article(context, url: str):
    """处理单篇微信文章"""
    print(f"\n正在处理: {url}")
    page = await context.new_page()
    try:
        await page.goto(url, wait_until="networkidle", timeout=30000)
        await page.wait_for_selector("#js_content", timeout=15000)

        # 提取标题
        title_el = await page.query_selector("#activity_name, .rich_media_title")
        title = await title_el.inner_text() if title_el else "未命名"
        title = title.strip()

        # 提取公众号名称
        author_el = await page.query_selector("#js_name, .profile_nickname")
        author = await author_el.inner_text() if author_el else "未知公众号"
        author = author.strip()

        # 提取发布时间
        date_el = await page.query_selector("#publish_time, .rich_media_meta_text")
        pub_date = await date_el.inner_text() if date_el else ""
        pub_date = pub_date.strip()

        print(f"  标题: {title}")
        print(f"  作者: {author}")
        print(f"  日期: {pub_date}")

        # 提取正文 HTML
        content_html = await page.evaluate(
            "() => { const node = document.getElementById('js_content'); return node ? node.innerHTML : ''; }"
        )
        if not content_html:
            print("  [警告] 未提取到正文内容")
            return

        # 创建文章输出目录
        date_prefix = datetime.now().strftime("%Y-%m-%d")
        safe_title = sanitize_filename(title)
        article_dir_name = f"{date_prefix}-{safe_title}"
        article_dir = os.path.join(OUTPUT_DIR, article_dir_name)
        img_dir = os.path.join(article_dir, "images")
        ensure_dir(img_dir)

        # 解析并下载图片
        soup = BeautifulSoup(content_html, "html.parser")
        imgs = soup.find_all("img")
        img_map: dict[str, str] = {}

        for idx, img in enumerate(imgs, 1):
            src = img.get("data-src") or img.get("src")
            if not src:
                continue

            local_name = f"img_{idx:03d}"
            local_file = await download_image(page, src, img_dir, local_name)
            if local_file:
                img_map[src] = f"images/{local_file}"
                img["src"] = f"images/{local_file}"
                if "data-src" in img.attrs:
                    del img.attrs["data-src"]

        # 清理无关属性，减少 Markdown 噪音
        for tag in soup.find_all(True):
            for attr in ["class", "id", "style", "data-tools"]:
                if attr in tag.attrs:
                    del tag.attrs[attr]

        # HTML 转 Markdown
        clean_html = str(soup)
        markdown = md(clean_html, heading_style="ATX", strip=["script", "style"])

        # 构造 frontmatter
        frontmatter = f"""---
title: {title}
author: {author}
date: {pub_date}
url: {url}
captured_at: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
---

"""

        md_path = os.path.join(article_dir, "article.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(frontmatter + markdown)

        print(f"  已保存: {md_path}")

    except Exception as e:
        print(f"  [错误] 处理失败: {e}")
    finally:
        await page.close()


async def main():
    ensure_dir(OUTPUT_DIR)

    if not os.path.exists(LINKS_FILE):
        print(f"未找到链接文件: {LINKS_FILE}")
        print("请在 links.txt 中粘贴微信文章链接，每行一个")
        return

    with open(LINKS_FILE, "r", encoding="utf-8") as f:
        links = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    if not links:
        print("links.txt 中没有找到有效链接")
        return

    print(f"共发现 {len(links)} 篇文章待处理")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent=USER_AGENT,
            viewport={"width": 1280, "height": 800},
        )

        for url in links:
            if "mp.weixin.qq.com" not in url:
                print(f"\n[跳过] 非微信文章链接: {url}")
                continue
            await process_article(context, url)

        await browser.close()

    print("\n全部处理完成！")


if __name__ == "__main__":
    asyncio.run(main())
