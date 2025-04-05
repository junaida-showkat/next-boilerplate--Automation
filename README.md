
# **Selenium Automation Framework with Pytest**

This project demonstrates an automation testing framework using **Python**, **Selenium**, and **Pytest**, following the **Page Object Model (POM)** design pattern. It includes structured test cases for real-world scenarios such as login, registration, and change password.

---

## **Features**
- Page Object Model (POM) structure for clean and maintainable code.
- Real-world scenarios: Register, Login, Logout, Forgot Password, and Change Password.
- Test case management using **Pytest**.
- Setup for **Selenium** with support for **Chrome** and **pytest fixtures**.

---

## **Requirements**

- **Python**: 3.10 or higher  
  [Download Python](https://www.python.org/downloads/)
  
- **VS Code**:  
  [Download VS Code](https://code.visualstudio.com/download)  
  **Extension**: Python (`ms-python.python`)

---

## **Install Dependencies**

1. **Install Python dependencies**:

   ```bash
   pip install python
   pip install selenium
   pip install pytest
   pip install pytest-order
   ```

2. **Optional** (For Selenium Wire support):

   ```bash
   pip install selenium-wire
   ```

3. **Verify installations**:

   ```bash
   python --version
   python -m pytest --version
   ```

---

## **Folder Structure**

```plaintext
project/
│
├── tests/                              # Test cases directory
│   ├── test_register_logout.py         # Register + Logout (Positive Case)
│   ├── test_register_positive_negative.py  # Positive & Negative Registration
│   ├── test_login.py                   # Login with valid/invalid data
│   ├── test_change_password.py         # Change password (positive/negative)
│   └── test_forgot_password.py         # Forgot password valid/invalid data
│
├── pages/                              # Page Object Model (POM) files
│   ├── base_page.py                    # Common methods: click, wait, send_keys
│   ├── register_page.py                # Locators & actions for Register
│   ├── login_page.py                   # Locators & actions for Login
│   ├── change_password_page.py         # Actions for Change Password
│   └── forgot_password_page.py         # Actions for Forgot Password
│
├── conftest.py                         # Browser setup/teardown fixture
├── requirements.txt                    # Project dependencies
```

---

## **How to Run Tests**

- **Run All Tests**:

   ```bash
   python -m pytest -v tests/
   ```

   Or

   ```bash
   pytest tests/
   ```

- **Run a Specific Test File**:

   ```bash
   python -m pytest -v tests/test_login.py
   ```

---

## **What Each File Does**

### **conftest.py**
- Sets up and tears down the browser using **Pytest** fixtures.

### **base_page.py**
- Contains common reusable methods for all pages:
  - `click(locator)`
  - `send_keys(locator, text)`
  - `is_element_present(locator)`
  - Automatically refreshes if elements are not loaded.

### **register_page.py**
- Functions for registration actions:
  - `open_register_page()`
  - `register_user(name, email, password)`
  - `is_user_logged_in()`
  - `logout()`

### **login_page.py**
- Functions for login actions:
  - `open_login_page()`
  - `login_user(email, password)`
  - `get_error_messages()`
  - `logout()`

### **change_password_page.py**
- Directly accesses the settings page and provides functions to change password:
  - `change_password(old, new, confirm)`
  - `refresh_page()`
  - `get_success_or_error_message()`

### **test_register_valid_invalid.py**
- Covers scenarios like:
  1. Valid registration
  2. Missing name
  3. Invalid email
  4. Invalid email + empty password

### **test_register_logout.py**
- Registers a user and logs out to confirm a successful login session.

### **test_login.py**
- Tests login with:
  1. Valid email/password
  2. Invalid email
  3. Wrong password
  4. Missing fields

### **test_change_password.py**
- Covers:
  1. Valid password change
  2. Mismatched new and confirm passwords
  3. Incorrect old password

---
## **Author**
Created by: Junaida Showkat 

Contact : junaidahShowkat@gmail.com

---
## **Contributing**
Feel free to fork the repository, create issues, and submit pull requests. Contributions are welcome!
