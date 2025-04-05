from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class ForgotPasswordPage(BasePage):
    SIGNIN_BUTTON = (By.XPATH, "//button[contains(@class, 'MuiButton-outlinedPrimary')]")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot password")
    EMAIL_INPUT = (By.NAME, "email")
    RESET_BUTTON = (By.XPATH, "//button[contains(@class, 'MuiButton-containedPrimary')]")

    def open_forgot_password_page(self):
        """Click Sign In and navigate to Forgot Password page."""
        self.click(self.SIGNIN_BUTTON)
        time.sleep(1)  # Small wait
        self.click(self.FORGOT_PASSWORD_LINK)
        time.sleep(2)  # Wait to load the Forgot Password page

    def reset_password(self, email):
        """Enter email and click Reset."""
        self.send_keys(self.EMAIL_INPUT, email)
        time.sleep(1)  # Small wait
        self.click(self.RESET_BUTTON)
        time.sleep(2)  # Wait for reset action to complete
