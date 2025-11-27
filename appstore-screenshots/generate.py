#!/usr/bin/env python3
"""
App Store 截图生成脚本
使用 Playwright 自动截图

安装依赖:
pip install playwright
playwright install chromium

使用方法:
python generate.py
"""

import asyncio
import os

async def generate_screenshots():
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("请先安装 playwright:")
        print("  pip install playwright")
        print("  playwright install chromium")
        return
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "output")
    os.makedirs(output_dir, exist_ok=True)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        # iOS 截图 (1242x2688)
        print("正在生成 iOS 截图...")
        ios_page = await browser.new_page(viewport={"width": 1400, "height": 2800})
        ios_html = os.path.join(script_dir, "ios-posters.html")
        await ios_page.goto(f"file://{ios_html}")
        await ios_page.wait_for_timeout(1000)
        
        for i in range(1, 7):
            poster = await ios_page.query_selector(f"#poster{i}")
            if poster:
                await poster.screenshot(path=os.path.join(output_dir, f"ios_{i}.png"))
                print(f"  已保存: ios_{i}.png")
        
        # Watch 截图 (422x514)
        print("正在生成 Watch 截图...")
        watch_page = await browser.new_page(viewport={"width": 600, "height": 700})
        watch_html = os.path.join(script_dir, "watch-posters.html")
        await watch_page.goto(f"file://{watch_html}")
        await watch_page.wait_for_timeout(1000)
        
        for i in range(1, 3):
            poster = await watch_page.query_selector(f"#watch{i}")
            if poster:
                await poster.screenshot(path=os.path.join(output_dir, f"watch_{i}.png"))
                print(f"  已保存: watch_{i}.png")
        
        await browser.close()
        
    print(f"\n截图已保存到: {output_dir}")
    print("完成!")

if __name__ == "__main__":
    asyncio.run(generate_screenshots())
