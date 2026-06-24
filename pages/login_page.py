from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.basepage import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD)).send_keys(username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()