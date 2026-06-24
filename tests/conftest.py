import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    options = Options()

    # Existing security settings
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--incognito")

    # --- Added for GitHub Actions (Headless Compatibility) ---
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # --------------------------------------------------------

    # Initialize the driver
    driver = webdriver.Chrome(options=options)

    # Note: maximize_window() can sometimes fail in headless mode;
    # it is often better to set a window size explicitly:
    driver.set_window_size(1920, 1080)

    yield driver  # This provides the driver to your test

    driver.quit()  # This closes the browser after the test
