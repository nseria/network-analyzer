import asyncio
import sys

from playwright.async_api import Playwright, async_playwright


async def run(playwright: Playwright) -> None:
    browser = await playwright.firefox.launch(headless=False)
    context = await browser.new_context()
    page = await browser.new_page()

    # ---------------------
    sys.stdout = open('./txt_storage/using-ai.txt', 'w')
    
    await page.goto("https://www.notion.so/")
    await page.get_by_role("navigation", name="Primary Navigation").get_by_role("link", name="Log in").click()
    await page.get_by_placeholder("Enter your email address...").click()
    await page.get_by_placeholder("Enter your email address...").fill("lemisily@korea.ac.kr")
    await page.get_by_placeholder("Enter your email address...").press("Enter")
    await page.get_by_placeholder("Enter your password...").click()
    await page.get_by_placeholder("Enter your password...").fill("***")
    await page.get_by_placeholder("Enter your password...").press("Enter")

    page.on("request", lambda request: print(">>", request.method, request.url))
    # page.on("request", lambda request: print(">>", request.headers_array(), request.method, request.url))

    page.on("response", lambda response: print("<<", response.status, response.url))
    #page.on("response", lambda response: print("<<", response.headers_array(), response.status, response.url))

    await page.get_by_text("Brainstorm ideas…").click()
    await page.get_by_placeholder("Ask AI to write anything…").fill("Brainstorm ideas on iot")
    await page.get_by_placeholder("Ask AI to write anything…").press("Enter")
    await page.get_by_placeholder("Tell AI what to do next…").click()
    await page.get_by_placeholder("Tell AI what to do next…").fill("Summarize list")
    await page.get_by_placeholder("Tell AI what to do next…").press("Enter")

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())