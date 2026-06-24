from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By


def test_add_to_cart(driver):
    driver.get("https://www.saucedemo.com/")

    # 1. Login
    LoginPage(driver).login("standard_user", "secret_sauce")

    # 2. Add to cart
    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()

    # 3. Assert
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.is_displayed()
    assert cart_badge.text == "1"