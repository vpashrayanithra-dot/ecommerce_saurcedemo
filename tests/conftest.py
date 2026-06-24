import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    options = Options()

    # These settings block the password manager security check
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--incognito")

    # Initialize the driver
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver  # This provides the driver to your test

    driver.quit()  # This closes the browser after the test