import pytest
import time
from pages.register_page import RegisterPage

#valid user , email and password
@pytest.mark.order(5)
def test_positive_registration(driver):
    reg_page = RegisterPage(driver)

    reg_page.open_register_page()
    time.sleep(2)

    name = "ValidUser"
    email = "QA2@yopmail.com"
    password = "ValidPass123"

    reg_page.register_user(name, email, password)
    print("Registration form submitted for positive test")

    time.sleep(3)

    if reg_page.is_user_logged_in():
        print("Positive Test Passed: Registration successful and user is logged in")
        reg_page.logout()
        print("Logout successful")
    else:
        print("Positive Test Failed: Registration failed")
        assert False

#Missing user and valid email and password
@pytest.mark.order(6)
def test_registration_missing_username(driver):
    reg_page = RegisterPage(driver)

    reg_page.open_register_page()
    time.sleep(2)

    reg_page.register_user("", "missingnameuser@yopmail.com", "ValidPass123")
    print("Submitted form with missing username")

    time.sleep(3)

    if not reg_page.is_user_logged_in():
        print("Negative Test Passed: Registration failed as expected (missing username)")
    else:
        reg_page.logout()
        print("Negative Test Failed: User registered with missing username")
        assert False

#invalid email format
@pytest.mark.order(7)
def test_registration_invalid_email(driver):
    reg_page = RegisterPage(driver)

    reg_page.open_register_page()
    time.sleep(2)

    reg_page.register_user("InvalidEmailUser", "invalid-email", "ValidPass123")
    print("Submitted form with invalid email")

    time.sleep(3)

    if not reg_page.is_user_logged_in():
        print("Negative Test Passed: Registration failed as expected (invalid email)")
    else:
        reg_page.logout()
        print("Negative Test Failed: User registered with invalid email")
        assert False

#Invalid email & password
@pytest.mark.order(8)
def test_registration_invalid_email_and_password(driver):
    reg_page = RegisterPage(driver)

    reg_page.open_register_page()
    time.sleep(2)

    reg_page.register_user("InvalidComboUser", "invalid-email", "")
    print("Submitted form with invalid email and empty password")

    time.sleep(3)

    if not reg_page.is_user_logged_in():
        print("Negative Test Passed: Registration failed as expected (invalid email and empty password)")
    else:
        reg_page.logout()
        print("Negative Test Failed: User registered with invalid email and empty password")
        assert False
