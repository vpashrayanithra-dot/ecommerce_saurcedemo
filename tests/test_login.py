from pages.login_page import LoginPage# Change your existing test code to look like this:
class TestLogin:
    def test_login_flow(self, driver):
        driver.get("https://www.saucedemo.com/")
        login_page = LoginPage(driver)

        # Use the actual method name from your class: login(username, password)
        login_page.login("standard_user", "secret_sauce")