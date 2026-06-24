import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage


def add_to_cart_by_name(driver, product_name):
    # Wait up to 10 seconds for the button to be clickable
    wait = WebDriverWait(driver, 10)

    # This XPATH looks for the button that is a sibling of the product name
    xpath = f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"

    button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    button.click()


@pytest.mark.parametrize("product_name", [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)",
])
def test_add_to_cart_ddt(driver, product_name):
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    add_to_cart_by_name(driver, product_name)

    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"