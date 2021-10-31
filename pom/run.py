from playwright.sync_api import Playwright, sync_playwright
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()
    #page.set_default_timeout(200)
    # Go to https://siutex.pythonanywhere.com/
    page.goto("https://siutex.pythonanywhere.com/")
    page.wait_for_load_state()
    time.sleep(1)
    # Click span
    page.click("span")
    # assert page.url == "https://siutex.pythonanywhere.com/accounts/login/"
    login_issue = True
    while login_issue:
        if not page.is_visible("input[name=\"username\"]"):
            page.click("span")
        else:
            login_issue = False
    # Click input[name="username"]
    page.click("input[name=\"username\"]")

    # Fill input[name="username"]
    page.fill("input[name=\"username\"]", "siutex")

    # Click input[name="password"]
    page.click("input[name=\"password\"]")

    # Fill input[name="password"]
    page.fill("input[name=\"password\"]", "Dupa1987")

    # Click text=login
    page.click("text=login")
    # assert page.url == "https://siutex.pythonanywhere.com/"

    # Click :nth-match(span, 2)
    page.click(":nth-match(span, 2)")
    # assert page.url == "https://siutex.pythonanywhere.com/drafts/"

    # Click text=siutex's blog
    page.click("text=siutex's blog")
    # assert page.url == "https://siutex.pythonanywhere.com/"

    # Go to https://siutex.pythonanywhere.com/admin/
    page.goto("https://siutex.pythonanywhere.com/admin/")

    # Click :nth-match(:text("Change"), 3)
    page.wait_for_selector(':nth-match(:text("Change"), 3)')
    page.click(":nth-match(:text(\"Change\"), 3)")
    assert page.url == "https://siutex.pythonanywhere.com/admin/auth/user/"

    # Click text=Home
    page.click("text=Home")
    # assert page.url == "https://siutex.pythonanywhere.com/admin/"

    # Click text=Log out
    page.click("text=Log out")
    # assert page.url == "https://siutex.pythonanywhere.com/admin/logout/"

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
