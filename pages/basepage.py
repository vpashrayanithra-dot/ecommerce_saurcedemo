from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def dismiss_popup(self, locator):
        try:
            short_wait = WebDriverWait(self.driver, 3)
            popup_close_button = short_wait.until(EC.element_to_be_clickable(locator))
            popup_close_button.click()
            print("Pop-up dismissed successfully.")
        except:
            print("No pop-up found, continuing...")