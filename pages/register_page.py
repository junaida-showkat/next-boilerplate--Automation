from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class RegisterPage(BasePage):
    REGISTER_BUTTON = (By.XPATH, "//button[contains(@class, 'MuiButton-outlinedSecondary')]")
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'MuiButton-containedPrimary')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[@aria-label='Sign out']")

    def open_register_page(self):
        self.click(self.REGISTER_BUTTON)
        time.sleep(2)

    def register_user(self, name, email, password):
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)
        time.sleep(3)

    def logout(self):
        if self.is_element_present(self.LOGOUT_BUTTON):
            self.click(self.LOGOUT_BUTTON)
            time.sleep(2)
            return True
        return False

    def is_user_logged_in(self):
        return self.is_element_present(self.LOGOUT_BUTTON)

    def open_register_page(self):
        self.safe_click(self.REGISTER_BUTTON)