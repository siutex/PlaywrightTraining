import pytest


@pytest.fixture(scope="function")
def set_up(browser):
    # Assess - Given
    # browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # # Open new page
    page = context.new_page()
    page.goto("https://siutex.pythonanywhere.com/")
    page.set_default_timeout(3000)

    yield page
    page.close()
