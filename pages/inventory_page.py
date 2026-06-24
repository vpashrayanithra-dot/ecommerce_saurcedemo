from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class InventoryPage(BasePage):
    # Locators for the inventory items
    BACKPACK_ADD_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self):
        """Adds the backpack to the cart."""
        self.driver.find_element(*self.BACKPACK_ADD_BTN).click()

    def go_to_cart(self):
        """Navigates to the cart page."""
        self.driver.find_element(*self.CART_ICON).click()