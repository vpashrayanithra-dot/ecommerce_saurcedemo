import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage


@pytest.mark.parametrize("product_name", [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)",
])
def test_inventory_item_visibility(driver, product_name):
    # 1. Navigate and Login
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    # 2. Wait until the inventory page is definitely loaded
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("inventory.html"))

    # 3. Locate the item by searching for the text in the page
    # This XPATH is absolute and highly reliable for this specific site
    xpath = f"//div[contains(text(), '{product_name}')]"

    try:
        element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        assert element.is_displayed(), f"{product_name} is hidden"
    except Exception as e:
        pytest.fail(f"Could not find {product_name}: {str(e)}")