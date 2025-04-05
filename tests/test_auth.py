"""from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage

def test_register_and_logout(driver):
    register_page = RegisterPage(driver)
    register_page.register_user("testuser", "testuser@yopmail.com", "password123")
    register_page.logout()

def test_login_and_logout(driver):
    login_page = LoginPage(driver)
    login_page.login_user("testuser@yopmail.com", "password123")
    login_page.logout()

def test_forgot_password(driver):
    forgot_password_page = ForgotPasswordPage(driver)
    forgot_password_page.reset_password("testuser@yopmail.com")
"""