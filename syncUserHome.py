from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

from playwright.async_api import Playwright, async_playwright

async def get_tiktok_cookie(account_file):
    async with async_playwright() as playwright:
        options = {
            'args': [
                '--lang en-GB',
            ],
            'headless': False,  # Set headless option here
        }
        # Make sure to run headed.
        browser = await playwright.chromium.launch(**options)
        # Setup context however you like.
        context = await browser.new_context()  # Pass any options
        context = await set_init_script(context)
        # Pause the page, and start recording manually.
        page = await context.new_page()
        await page.goto("https://www.tiktok.com/login?lang=en")
        await page.pause()
        # 点击调试器的继续，保存cookie
        await context.storage_state(path=account_file)

# 设置 WebDriver (这里使用 Chrome)
driver = webdriver.Chrome()

# 打开页面
url = 'https://www.xiaohongshu.com/user/profile/5b6568aa11be106304b4473f?xsec_token=&xsec_source=pc_note'  # 替换为你要爬取的 URL
driver.get(url)

# 等待页面加载
sleep(10)  # 可以增加等待时间，确保数据加载完成

# 获取页面源代码
page_source = driver.page_source

# 使用 BeautifulSoup 解析获取到的 HTML
from bs4 import BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# 提取你需要的内容
a_tags = soup.find_all('a', style="display:none;")
for a_tag in a_tags:
    print(a_tag.get('href'), a_tag.text.strip())

# 关闭浏览器
driver.quit()
