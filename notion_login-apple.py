import asyncio
import sys

from playwright.async_api import Playwright, async_playwright
# you should manually enter the 6-digit code from your iphone.
# Ready for verification number in setting -> password & security -> security -> two-factor authentication -> get verification code
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")
num4 = input("Enter the fourth number: ")
num5 = input("Enter the fifth number: ")
num6 = input("Enter the sixth number: ")

async def run(playwright: Playwright) -> None:
    browser = await playwright.firefox.launch(headless=False)
    context = await browser.new_context()
    page = await browser.new_page()

    # ---------------------
    sys.stdout = open('login-apple.txt', 'w')

    page.on("request", lambda request: print(">>", request.method, request.url))
    # page.on("request", lambda request: print(">>", request.headers_array(), request.method, request.url))

    page.on("response", lambda response: print("<<", response.status, response.url))
    #page.on("response", lambda response: print("<<", response.headers_array(), response.status, response.url))
    
    await page.goto("https://www.notion.so/")
    await page.get_by_role("navigation", name="Primary Navigation").get_by_role("link", name="Log in").click()
    await page.get_by_role("button", name="Continue with Apple").click()
    await page.get_by_label("Sign In with your Apple ID").click()
    await page.get_by_label("Sign In with your Apple ID").fill("lemisily@gmail.com")
    await page.get_by_label("Sign In with your Apple ID").press("Enter")
    await page.get_by_label("Password").fill("***")
    await page.get_by_label("Password").press("Enter")
    
    await page.get_by_role("textbox", name="Enter verification code. On entering code in the input fields, the focus will automatically move on to the next input fields. After entering the verification code, the page gets updated automatically. Digit 1").fill(num1)
    await page.get_by_role("textbox", name="Digit 2").fill(num2)
    await page.get_by_role("textbox", name="Digit 3").fill(num3)
    await page.get_by_role("textbox", name="Digit 4").fill(num4)
    await page.get_by_role("textbox", name="Digit 5").fill(num5)
    await page.get_by_role("textbox", name="Digit 6").fill(num6)
    await page.get_by_role("button", name="Not Now").click()
    await page.get_by_role("button", name="Continue").click()

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())