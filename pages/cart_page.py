from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class CartPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")
    POPUP_CLOSE_BTN = (By.ID, "close-popup-id")

    def proceed_to_checkout(self):
        self.dismiss_popup(self.POPUP_CLOSE_BTN)
        self.driver.find_element(*self.CHECKOUT_BTN).click()

    def is_cart_empty(self):
        return len(self.driver.find_elements(By.CLASS_NAME, "cart_item")) == 0