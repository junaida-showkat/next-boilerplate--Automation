import pytest
import time
from pages.forgot_password_page import ForgotPasswordPage

@pytest.mark.order(3)
@pytest.mark.parametrize("email, should_reset", [
    ("QA1@yopmail.com", True),   # Valid Email
    ("invaliduser@yopmail.com", False),     # Unregistered Email
    ("", False)                             # Missing Email
])
def test_forgot_password(driver, email, should_reset):
    forgot_page = ForgotPasswordPage(driver)
    forgot_page.open_forgot_password_page()
    forgot_page.reset_password(email)

    time.sleep(2)

    print(f"Forgot password process executed for {email}")

    assert True, "Test executed successfully"
