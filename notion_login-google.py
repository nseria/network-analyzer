import asyncio
import sys

from playwright.async_api import Playwright, async_playwright


async def run(playwright: Playwright) -> None:
    browser = await playwright.firefox.launch(headless=False)
    context = await browser.new_context()
    page = await browser.new_page()

    # ---------------------
    sys.stdout = open('login-google.txt', 'w')

    page.on("request", lambda request: print(">>", request.method, request.url))
    # page.on("request", lambda request: print(">>", request.headers_array(), request.method, request.url))

    page.on("response", lambda response: print("<<", response.status, response.url))
    #page.on("response", lambda response: print("<<", response.headers_array(), response.status, response.url))
    
    await page.goto("https://www.notion.so/ko-kr")
    await page.get_by_role("navigation", name="Primary Navigation").get_by_role("link", name="로그인").click()
    async with page.expect_popup() as page1_info:
        await page.get_by_role("button", name="Continue with Google").click()
    page1 = await page1_info.value
    await page1.get_by_role("textbox", name="Email or phone").fill("lemisily@gmail.com")
    await page1.get_by_role("button", name="Next").click()
    await page1.get_by_role("textbox", name="Enter your password").click()
    await page1.get_by_role("textbox", name="Enter your password").fill("***")
    await page1.get_by_role("button", name="Next").click()
    await page1.close()
    await page.goto("https://www.notion.so/oauth2callback?state=eyJjYWxsYmFja1R5cGUiOiJwb3B1cCIsImVuY3J5cHRlZFRva2VuIjoidjAyOmxvZ2luX3dpdGhfZ29vZ2xlOlI4TkM1QlZoMUlIa19RUWZmdVpsQVMyd20xRGtNd2puN21aeUJEM0pYUEVfVHFRU1ZFRDZndTBRZkdDeG1taTBqZlpaZFVGM3I0Mnp3VkVQYWdRdzMzd0JmNFVZUzlJMHZNcVVid0RhUHRxdHZKNnVrcUZIR04zSkhLS1hTNGVQMnJDQyJ9&code=4%2F0AbUR2VMeP5kUYmI-GQ9RwD4cQ4YZyHDMFDpo0PVCqggVsGDoQzri4HYRpmf2bN6kSA8b3A&scope=email+profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+openid&authuser=0&prompt=none")
    await page.goto("https://www.notion.so/")
    await page.goto("https://www.notion.so/hwseclab/OS-Study-b0758a292e8341e8815e5c1c3af6c772?pvs=3&qid=")
    await page.goto("https://www.notion.so/hwseclab/OS-Study-b0758a292e8341e8815e5c1c3af6c772")

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())