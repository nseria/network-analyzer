import sys
import time

from playwright.sync_api import Playwright, sync_playwright, expect


# you should manually enter the 6-digit code from your iphone.
# Ready for verification number in setting -> password & security -> security -> two-factor authentication -> get verification code

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    sys.stdout = open('./txt_storage/login-apple.txt', 'w')

    page.on("request", lambda request: print(">>", request.method, request.url))
    # page.on("request", lambda request: print(">>", request.headers_array(), request.method, request.url))

    page.on("response", lambda response: print("<<", response.status, response.url))
    #page.on("response", lambda response: print("<<", response.headers_array(), response.status, response.url))
    

    page.goto("https://www.notion.so/ko-kr")
    page.goto("https://www.notion.so/")
    page.get_by_role("navigation", name="Primary Navigation").get_by_role("link", name="Log in").click()
    page.get_by_role("button", name="Apple로 계속하기").click()
    time.sleep(3)
    page.get_by_label("Apple ID로 로그인").fill("*****")
    page.get_by_label("Apple ID로 로그인").press("Enter")
    time.sleep(3)
    page.get_by_label("암호").fill("*****")
    page.get_by_label("암호").press("Enter")
    time.sleep(15)
    
    page.get_by_role("button", name="나중에").click()
    page.get_by_role("button", name="계속").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

