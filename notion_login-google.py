from playwright.sync_api import Playwright, sync_playwright, expect

import sys
import time

# you should turn off two factor authentication setting in Google

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    sys.stdout = open('./txt_storage/login-google.txt', 'w')

    page.on("request", lambda request: print(">>", request.method, request.url))
    # page.on("request", lambda request: print(">>", request.headers_array(), request.method, request.url))

    page.on("response", lambda response: print("<<", response.status, response.url))
    #page.on("response", lambda response: print("<<", response.headers_array(), response.status, response.url))

    page.goto("https://www.notion.so/ko-kr")
    page.goto("https://www.notion.so/")
    page.get_by_role("navigation", name="Primary Navigation").get_by_role("link", name="Log in").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("button", name="Google로 계속하기").click()
    page1 = page1_info.value

    time.sleep(3)
    page1.get_by_role("textbox", name="이메일 또는 휴대전화").click()
    page1.get_by_role("textbox", name="이메일 또는 휴대전화").fill("*****")
    page1.get_by_role("textbox", name="이메일 또는 휴대전화").press("Enter")
    time.sleep(3)
    page1.get_by_role("textbox", name="비밀번호 입력").fill("*****")
    page1.get_by_role("textbox", name="비밀번호 입력").press("Enter")
    page1.close()
    page.goto("https://www.notion.so/")
    page.goto("https://www.notion.so/nseria/Seria-4e57ff48336d4a08a8b10f40d647b8ed?pvs=3&qid=")
    page.goto("https://www.notion.so/nseria/Seria-4e57ff48336d4a08a8b10f40d647b8ed")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
