import asyncio
import sys

from playwright.async_api import Playwright, async_playwright


async def run(playwright: Playwright) -> None:
    browser = await playwright.firefox.launch(headless=False)
    context = await browser.new_context()
    page = await browser.new_page()

    # ---------------------
    sys.stdout = open('./txt_storage/login-email.txt', 'w')

    page.on("request", lambda request: print(">>", request.method, request.url))
    # page.on("request", lambda request: print(">>", request.headers_array(), request.method, request.url))

    page.on("response", lambda response: print("<<", response.status, response.url))
    #page.on("response", lambda response: print("<<", response.headers_array(), response.status, response.url))
    
    await page.goto("https://www.notion.so/")
    await page.get_by_role("navigation", name="Primary Navigation").get_by_role("link", name="Log in").click()
    await page.get_by_placeholder("Enter your email address...").click()
    await page.get_by_placeholder("Enter your email address...").fill("lemisily@gmail.com")
    await page.get_by_placeholder("Enter your email address...").press("Enter")
    await page.get_by_placeholder("Enter your password...").click()
    await page.get_by_placeholder("Enter your password...").fill("***")
    await page.get_by_placeholder("Enter your password...").press("Enter")

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())