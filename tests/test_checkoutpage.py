from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout_process(driver):
    driver.get("https://www.saucedemo.com/")

    # 1. Setup
    LoginPage(driver).login("standard_user", "secret_sauce")
    InventoryPage(driver).go_to_cart()
    CartPage(driver).proceed_to_checkout()

    # 2. Checkout
    checkout = CheckoutPage(driver)
    checkout.fill_checkout_info("John", "Doe", "12345")

    # 3. Assert
    assert "checkout-step-two" in driver.current_url