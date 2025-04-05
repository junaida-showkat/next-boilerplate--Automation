from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    SIGNIN_BUTTON = (By.XPATH, "//button[contains(@class, 'MuiButton-outlinedPrimary')]")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'MuiButton-containedPrimary')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[@aria-label='Sign out']")

    def open_login_page(self):
        self.click(self.SIGNIN_BUTTON)

    def login_user(self, email, password):
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    def logout(self):
        if self.is_element_present(self.LOGOUT_BUTTON):
            self.click(self.LOGOUT_BUTTON)
            return True
        return False
