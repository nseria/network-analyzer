from playwright.sync_api import Playwright, sync_playwright, Page, expect
import time
import sys

# You can use this code if you do not want to leave your id and passwrod inside the code.

# user_id = input("Enter your notion ID: ")
# user_password = input("Enter the password for login: ")

# Page.on method can be manually activated by uncommenting the code below depending on what you want to do.
# Initialize page.on request and response at the very beginning of the 'run' function is recommended.
# sys.stdout change the direction of the print function to the targe txt file in the txt_storage folder.

# Change the urls with your own. At the end of each work, go back to the home page.

def auto_login(page: Page):

    sys.stdout = open('./txt_storage/login-status.txt', 'w')

    # page.on("request", lambda request: print(">>", request.method, request.url))
    # page.on("response", lambda response: print("<<", response.status, response.url))

    page.goto("https://www.notion.so/nseria/Seria-4e57ff48336d4a08a8b10f40d647b8ed")
    time.sleep(5)

def using_ai(page: Page):

    sys.stdout = open('./txt_storage/using_ai.txt', 'w')

    # page.on("request", lambda request: print(">>", request.method, request.url))
    # page.on("response", lambda response: print("<<", response.status, response.url))

    # set page as an empty page.
    # do not click anything except generating the page so that "write with AI" button can be shown.
    page.goto("https://www.notion.so/nseria/Apple-co-936ec3dcda5147058837a696eb4c2dfd")
    page.get_by_role("button", name="Write “Apple co.” with AI…").click()
    page.get_by_placeholder("Ask AI to write anything…").press("Enter")
    time.sleep(20)

    page.goto("https://www.notion.so/nseria/Seria-4e57ff48336d4a08a8b10f40d647b8ed")

    time.sleep(3)

def export_pdf(page: Page):
    
    sys.stdout = open('./txt_storage/export_pdf.txt', 'w')
    
    # page.on("request", lambda request: print(">>", request.method, request.url))
    # page.on("response", lambda response: print("<<", response.status, response.url))
    
    # write something in this page.
    page.goto("https://www.notion.so/nseria/Apple-Inc-77949e288f734a12a43f8f91d4bb2f02")
    page.locator(".notion-topbar-more-button").click()
    page.locator(".notion-topbar-more-button").press("ArrowDown")
    page.locator(".notion-topbar-more-button").press("ArrowDown")
    page.locator(".notion-topbar-more-button").press("ArrowDown")
    page.locator(".notion-topbar-more-button").press("ArrowDown")
    page.locator(".notion-topbar-more-button").press("ArrowDown")
    page.locator(".notion-topbar-more-button").press("ArrowDown")
    page.locator(".notion-topbar-more-button").press("ArrowDown")
    page.locator(".notion-topbar-more-button").press("ArrowDown")
    page.locator(".notion-topbar-more-button").press("ArrowDown")
    page.locator(".notion-topbar-more-button").press("ArrowDown")
    page.locator(".notion-topbar-more-button").press("ArrowDown")
    page.locator(".notion-topbar-more-button").press("ArrowDown")
    page.locator(".notion-topbar-more-button").press("ArrowDown")
    page.locator(".notion-topbar-more-button").press("ArrowDown")
    page.locator(".notion-topbar-more-button").press("ArrowDown")
    page.locator(".notion-topbar-more-button").press("ArrowDown")
    page.locator(".notion-topbar-more-button").press("ArrowDown")
    page.locator(".notion-topbar-more-button").press("ArrowDown")
    page.locator(".notion-topbar-more-button").press("ArrowDown")
    page.locator(".notion-topbar-more-button").press("ArrowDown")
    page.locator(".notion-topbar-more-button").press("Enter")
    with page.expect_download() as download_info:
        page.get_by_role("button", name="Export").click()
    download = download_info.value

    file_name = download.suggested_filename
    
    download.save_as(f"./pdf_storage/{file_name}")
    time.sleep(20)

    page.goto("https://www.notion.so/nseria/Seria-4e57ff48336d4a08a8b10f40d647b8ed")

    time.sleep(3)

def download_pdf(page: Page):

    sys.stdout = open('./txt_storage/download_pdf.txt', 'w')

    # page.on("request", lambda request: print(">>", request.method, request.url))
    # page.on("response", lambda response: print("<<", response.status, response.url))

    # embed a file link in this page. click to trigger the action.
    page.goto("https://www.notion.so/nseria/Download-apple-report-f98d56dbe7f4479aa6e6b3ba5f68bc33")
    with page.expect_popup() as page1_info:
        page.get_by_role("button", name="e1796d8b-5155-4ffd-a087-9021a4971a0e_Apple_Inc..pdf 25.3KB").click()
    page1 = page1_info.value
    page1.close()
    
    time.sleep(3)

    page.goto("https://www.notion.so/nseria/Seria-4e57ff48336d4a08a8b10f40d647b8ed")

    time.sleep(3)

def upload_pdf(page: Page):

    sys.stdout = open('./txt_storage/upload_pdf.txt', 'w')

    # page.on("request", lambda request: print(">>", request.method, request.url))
    # page.on("response", lambda response: print("<<", response.status, response.url))

    # embed empty upload link in this page. click to trigger the action.
    page.goto("https://www.notion.so/nseria/Upload-apple-report-06b6d95d8e874641bbfc992cd02380ec")
    page.get_by_role("button", name="Upload or embed a file").click()
    page.get_by_role("button", name="Choose a file").click()
    page.locator("input[type=\"file\"]").set_input_files("./pdf_storage/55909764.pdf")
    time.sleep(15)

    page.goto("https://www.notion.so/nseria/Seria-4e57ff48336d4a08a8b10f40d647b8ed")

def integration_onedrive(page: Page):

    sys.stdout = open('./txt_storage/integration_onedrive.txt', 'w')

    # page.on("request", lambda request: print(">>", request.method, request.url))
    # page.on("response", lambda response: print("<<", response.status, response.url))

    # embed a file link in this page. click to trigger the action.
    page.goto("https://www.notion.so/nseria/Onedrive-test-4bfa9b29e34b419bb7b99919519520d6")
    time.sleep(5)
    with page.expect_popup() as page2_info:
        page.get_by_role("link", name="20230508_zkp-seminar.pdf 794.54 KB").click()
    page2 = page2_info.value
    time.sleep(15)
    page2.close()
    
    time.sleep(5)

    page.goto("https://www.notion.so/nseria/Seria-4e57ff48336d4a08a8b10f40d647b8ed")

    time.sleep(3)

def integration_googledrive(page: Page):

    sys.stdout = open('./txt_storage/integration_googledrive.txt', 'w')

    # page.on("request", lambda request: print(">>", request.method, request.url))
    # page.on("response", lambda response: print("<<", response.status, response.url))

    # embed a file link in this page. click to trigger the action.
    page.goto("https://www.notion.so/nseria/Googledrive-test-b03888e31e9d4d0ca28fef51608caeea")
    time.sleep(5)
    with page.expect_popup() as page3_info:
        page.get_by_role("link", name="Blockchain_Mechanics_of_Bitcoin.pdf 2.38 MB • pdf • https://drive.google.com").click()
    page3 = page3_info.value
    time.sleep(15)
    page3.close()
    
    time.sleep(5)

    page.goto("https://www.notion.so/nseria/Seria-4e57ff48336d4a08a8b10f40d647b8ed")

    time.sleep(3)

def integration_zoom(page: Page):

    sys.stdout = open('./txt_storage/integration_zoom.txt', 'w')

    # page.on("request", lambda request: print(">>", request.method, request.url))
    # page.on("response", lambda response: print("<<", response.status, response.url))

    # embed a zoom link in this page. click to trigger the action.
    page.goto("https://www.notion.so/nseria/Zoom-test-c3863d8c073748bc9d8ea86ab6b9cf1a")
    time.sleep(5)
    with page.expect_popup() as page4_info:
        page.get_by_role("link", name="Join Zoom meeting981-4422-7751").click()
    page4 = page4_info.value
    time.sleep(15)
    page4.close()
    
    time.sleep(5)

    page.goto("https://www.notion.so/nseria/Seria-4e57ff48336d4a08a8b10f40d647b8ed")

    time.sleep(3)

def integration_googlemap(page: Page):

    sys.stdout = open('./txt_storage/integration_googlemap.txt', 'w')

    # page.on("request", lambda request: print(">>", request.method, request.url))
    # page.on("response", lambda response: print("<<", response.status, response.url))

    # embed a google map link in this page. click to trigger the action.
    page.goto("https://www.notion.so/nseria/Googlemap-test-de0f6adffb124e1dae5984ceb59c055c")
    time.sleep(5)
    with page.expect_popup() as page5_info:
        page.frame_locator("#notion-app iframe").get_by_role("link", name="큰 지도 보기").click()
    page5 = page5_info.value
    time.sleep(15)
    page5.close()
    time.sleep(3)
    page.get_by_role("button", name="Embed a Google Map").click()
    page.get_by_placeholder("https://www.google.com/maps…").click()
    page.get_by_placeholder("https://www.google.com/maps…").fill("https://goo.gl/maps/mNEASkstfbgtTKqp8")
    page.get_by_placeholder("https://www.google.com/maps…").press("Enter")
    time.sleep(5)

    page.goto("https://www.notion.so/nseria/Seria-4e57ff48336d4a08a8b10f40d647b8ed")

    time.sleep(3)

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    sys.stdout = open('./txt_storage/login-email.txt', 'w')

    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    
    # you should change the email and password of your own account
    # check for the language of the page
    page.goto("https://www.notion.so/ko-kr")
    page.get_by_role("navigation", name="Primary Navigation").get_by_role("link", name="Log in").click()
    page.get_by_placeholder("이메일 주소를 입력하세요.").click()
    page.get_by_placeholder("이메일 주소를 입력하세요.").fill("*****")
    page.get_by_placeholder("이메일 주소를 입력하세요.").press("Tab")
    page.get_by_role("button", name="이메일로 계속하기").click()
    page.get_by_placeholder("비밀번호를 입력하세요.").fill("******")
    page.get_by_placeholder("비밀번호를 입력하세요.").press("Enter")

    time.sleep(8)

    auto_login(page) # check whether the login status is valid or not, and go to the default page
    using_ai(page) # use Notion AI to write simple essay
    export_pdf(page) # export notion page to make pdf file
    download_pdf(page) # download pdf file from AWS notion cloud storage
    upload_pdf(page) # upload pdf file to AWS notion cloud storage
    integration_onedrive(page) # check network when user click onedrive link
    integration_googledrive(page) # check network when user click googledrive link
    integration_zoom(page) # check network when user click zoom link
    integration_googlemap(page) # check network when user click googlemap link and embed googlemap url

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
