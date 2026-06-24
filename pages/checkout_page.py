from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    POPUP_CLOSE_BTN = (By.ID, "close-popup-id")

    def fill_checkout_info(self, first, last, zip_code):
        self.dismiss_popup(self.POPUP_CLOSE_BTN)
        self.driver.find_element(*self.FIRST_NAME).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.ZIP_CODE).send_keys(zip_code)
        self.driver.find_element(*self.CONTINUE_BTN).click()