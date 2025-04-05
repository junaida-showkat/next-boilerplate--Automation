import pytest
import time
from pages.login_page import LoginPage
from pages.change_password_page import ChangePasswordPage

@pytest.mark.order(4)
def test_change_password_flow(driver):
    login_page = LoginPage(driver)
    change_page = ChangePasswordPage(driver)

    email = "QA1@yopmail.com"
    current_password = "ValidPass123"
    temp_password = "TempPass1"
    new_password = "NewPass1234"

    #Step 1: Logging in with current password
    login_page.open_login_page()
    login_page.login_user(email, current_password)
    time.sleep(3)


    #Step 2: Navigating to settings page
    change_page.open_settings_page()
    time.sleep(2)

    #Negative Test: Wrong old password"
    change_page.change_password("WrongOldPass", temp_password, temp_password)
    change_page.refresh_page()
    time.sleep(2)
    

    #Negative Test: Mismatched new and confirm password
    #change_page.change_password(current_password, "Mismatch1", "Mismatch2")
    #time.sleep(2)
    #change_page.refresh_page()
    #time.sleep(4) 

    #Positive Test: Changing password successfully
    change_page.change_password(current_password, new_password, new_password)
    time.sleep(3)
    login_page.logout()

    #Step 3: Logging in with new password
    login_page.open_login_page()
    login_page.login_user(email, new_password)
    time.sleep(3)
    print("Test Pass for forgot password")
    assert login_page.logout()

    #Step 4: Reverting back to original password
    login_page.open_login_page()
    login_page.login_user(email, new_password)
    time.sleep(3)
    change_page.open_settings_page()
    time.sleep(3)
    change_page.change_password(new_password, current_password, current_password)
    time.sleep(3)
    login_page.logout()

    
