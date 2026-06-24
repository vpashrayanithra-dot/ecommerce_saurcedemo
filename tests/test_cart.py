from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_navigate_to_cart(driver):
    driver.get("https://www.saucedemo.com/")

    # 1. Login and navigate
    LoginPage(driver).login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()

    # 2. Assert navigation
    assert "cart" in driver.current_url