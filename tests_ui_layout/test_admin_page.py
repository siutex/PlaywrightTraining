import os

import pytest

from pom.admin_page_elements import *

TESTUSER = os.environ['TESTUSER']
PASSWORD = os.environ['PASSWORD']


@pytest.mark.smoke
def test_admin_page_login(set_up):
    # Open new page
    page = set_up

    # Go to https://siutex.pythonanywhere.com/admin/login/?next=/admin/
    page.goto("https://siutex.pythonanywhere.com/admin/login/?next=/admin/")

    # Click input[name="username"]
    page.click(AdminPage.username_input)

    # Fill input[name="username"]
    page.fill(AdminPage.username_input, TESTUSER)

    # Click input[name="password"]
    page.click(AdminPage.password_input)

    # Fill input[name="password"]
    page.fill(AdminPage.password_input, PASSWORD)

    # Click text=Log in
    page.click(AdminPage.login_button)
    # assert page.url == "https://siutex.pythonanywhere.com/admin/"

    # Click text=Groups
    page.click(AdminPage.groups_button)
    # assert page.url == "https://siutex.pythonanywhere.com/admin/auth/group/"

    # Click text=Add group
    page.click(AdminPage.add_group_button)
    # assert page.url == "https://siutex.pythonanywhere.com/admin/auth/group/add/"

    # Click text=Log out
    page.click(AdminPage.log_out_button)
    assert page.url == "https://siutex.pythonanywhere.com/admin/logout/"
