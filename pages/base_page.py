"""from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        self.wait.until(EC.presence_of_element_located(locator)).send_keys(text)

    def is_element_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, ElementNotInteractableException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except (TimeoutException, ElementClickInterceptedException, ElementNotInteractableException) as e:
            print(f"Failed to click element {locator}: {e}")
            raise

    def send_keys(self, locator, text):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except TimeoutException as e:
            print(f"Failed to send keys to element {locator}: {e}")
            raise

    def is_element_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            print(f"Element not present: {locator}")
            return False

    def wait_for_element(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            print(f"Element not found within {timeout} seconds: {locator}")
            return False
    def safe_click(self, locator, retry=True):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except TimeoutException:
            if retry:
                print("Register button not found, refreshing the page...")
                self.driver.refresh()
                self.wait.until(EC.element_to_be_clickable(locator)).click()
            else:
                raise
    def get_element_text(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element.text
        except:
            return ""
