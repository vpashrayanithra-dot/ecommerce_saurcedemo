import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


def fill_checkout_form(driver, first, last, zip_code):
    driver.find_element(By.ID, "first-name").send_keys(first)
    driver.find_element(By.ID, "last-name").send_keys(last)
    driver.find_element(By.ID, "postal-code").send_keys(zip_code)
    driver.find_element(By.ID, "continue").click()


@pytest.mark.parametrize("first, last, zip_code", [
    ("John", "Doe", "12345"),
    ("Jane", "Smith", "54321"),
    ("Alice", "Brown", "90210"),
    ("Bob", "White", "10001"),
    ("Charlie", "Green", "60606"),
    ("David", "Black", "33101"),
    ("", "MissingName", "00000"),  # Negative case: empty first name
    ("Invalid", "User", ""),  # Negative case: empty zip code
])
def test_checkout_form_ddt(driver, first, last, zip_code):
    # Setup
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    # Go to Cart and start Checkout
    driver.get("https://www.saucedemo.com/cart.html")
    driver.find_element(By.ID, "checkout").click()

    # Action: Fill form
    fill_checkout_form(driver, first, last, zip_code)

    # Validation
    if first == "" or zip_code == "":
        # Should stay on the same page due to error
        assert "checkout-step-one" in driver.current_url
    else:
        # Should proceed to step two
        assert "checkout-step-two" in driver.current_url