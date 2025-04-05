import pytest
import time
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://next-boilerplate-umber.vercel.app/")
    driver.maximize_window()
    yield driver  # Run the test
    time.sleep(2)
    print(" Waiting for 2 seconds before closing the browser...")   
    driver.quit()
