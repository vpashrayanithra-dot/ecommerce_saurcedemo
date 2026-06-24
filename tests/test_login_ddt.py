import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize("user, password, expected_success", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
    ("problem_user", "secret_sauce", True),
    ("performance_glitch_user", "secret_sauce", True),
    ("error_user", "secret_sauce", True),
    ("visual_user", "secret_sauce", True),
])
def test_login_variations(driver, user, password, expected_success):
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)

    login.login(user, password)

    if expected_success:
        assert "inventory" in driver.current_url
    else:
        assert "inventory" not in driver.current_url