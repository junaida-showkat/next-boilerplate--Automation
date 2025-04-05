import pytest
import time
from pages.register_page import RegisterPage

@pytest.mark.order(1)
def test_register_and_logout(driver):
    reg_page = RegisterPage(driver)

    reg_page.open_register_page()
    time.sleep(2)

    name = "TestUser"
    email = "QA1@yopmail.com"
    password = "ValidPass123"

    reg_page.register_user(name, email, password)
    print("Registration form submitted")

    time.sleep(3)

    if reg_page.is_user_logged_in():
        print("Registration successful. User is logged in.")
        reg_page.logout()
        print("Logout successful.")
    else:
        print("Registration failed.")
        assert False
