import pytest
from pom.home_page_elements import HomePage


# @pytest.mark.xfail(reason='url not ready')
# @pytest.mark.skip
@pytest.mark.parametrize("username", ["siutex",
                                      pytest.param("test", marks=pytest.mark.xfail),
                                      pytest.param("zonk", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("password", ["Dupa1987",
                                      pytest.param("test", marks=pytest.mark.xfail),
                                      pytest.param("test", marks=pytest.mark.xfail)])
def test_home_page(set_up, username, password) -> None:
    page = set_up

    page.click(HomePage.blog_layout)

    page.click(HomePage.main_page)
    assert page.url == HomePage.home_url

    page.click(HomePage.login_page)
    assert page.url == HomePage.home_url + "accounts/login/"

    # Click input[name="username"]
    page.click(HomePage.username_input)

    # Fill input[name="username"]
    page.fill(HomePage.username_input, username)

    # Click input[name="password"]
    page.click(HomePage.password_input)

    # Fill input[name="password"]
    page.fill(HomePage.password_input, password)

    # Click text=login
    page.click(HomePage.login_button)
    assert page.url == HomePage.home_url

    # Click text=Log out
    page.click("text=Log out")
    assert page.url == HomePage.home_url
