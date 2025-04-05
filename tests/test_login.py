import pytest
from pages.login_page import LoginPage
@pytest.mark.order(2)
@pytest.mark.parametrize("email, password, should_login", [
    ("QA1@yopmail.com", "ValidPass123", True),   # Valid Login
    ("invaliduser@yopmail.com", "ValidPass123", False), # Invalid Email
    ("test@yopmail.com", "WrongPass", False),     # Wrong Password
    ("", "ValidPass123", False),                        # Missing Email
    ("test@yopmail.com", "", False)              # Missing Password
])
def test_login_user(driver, email, password, should_login):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login_user(email, password)

    if should_login:
        assert login_page.logout(), "Login successful but logout failed!"
    else:
        assert not login_page.logout(), "User should not be logged in but logout button is visible!"
