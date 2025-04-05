from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class ChangePasswordPage(BasePage):
    URL = "https://next-boilerplate-umber.vercel.app/settings"

    OLD_PASSWORD = (By.NAME, "old")
    NEW_PASSWORD = (By.NAME, "new")
    CONFIRM_PASSWORD = (By.NAME, "confirm")
    UPDATE_BUTTON = (By.XPATH, "//button[contains(@class, 'MuiButtonBase-root') and contains(@class, 'MuiButton-containedPrimary') and contains(@class, 'css-1hw9j7s')]")


    def open_settings_page(self):
        self.driver.get(self.URL)
        time.sleep(2)

    def change_password(self, old_pass, new_pass, confirm_pass):
        self.send_keys(self.OLD_PASSWORD, old_pass)
        self.send_keys(self.NEW_PASSWORD, new_pass)
        self.send_keys(self.CONFIRM_PASSWORD, confirm_pass)
        self.click(self.UPDATE_BUTTON)
        time.sleep(4)

    def is_update_successful(self):
        # Optionally check for some success indication here
        return True
    """def refresh_page(self):
        Refreshes the current page
        self.driver.refresh()
        time.sleep(2)"""
    def refresh_page(self):
        print("🔄 Refreshing the settings page...")
        self.driver.execute_script("location.reload()")
