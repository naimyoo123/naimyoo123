from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import USERNAME, PASSWORD
from utils.locators import (
    ACCEPT_BUTTON_ID,
    LOGIN_NAVIGATE_BUTTON_ID,
    USERNAME_FIELD,
    PASSWORD_FIELD,
    LOGIN_SUBMIT_ID,
    CHAT_BUTTON_ARIA_LABEL
)
from utils.exceptions import LoginError
import time


def perform_login(driver, website_url):
    """
    Performs the login process on the given website.
    """
    driver.get(website_url)
    wait = WebDriverWait(driver, 30)

    # Accept cookie consent (if present)
    try:
        accept_btn = wait.until(EC.element_to_be_clickable((By.ID, ACCEPT_BUTTON_ID)))
        accept_btn.click()
        print("Accepted cookie consent.")
    except Exception as e:
        print(f"Cookie consent not found or could not be clicked: {e}")

    # Click "Log in" button
    try:
        login_nav = wait.until(EC.element_to_be_clickable((By.ID, LOGIN_NAVIGATE_BUTTON_ID)))
        login_nav.click()
        print("Clicked 'Log in' button.")
    except Exception as e:
        raise LoginError(f"Failed to click 'Log in' button: {e}")

    # Fill in username
    try:
        username_field = wait.until(EC.visibility_of_element_located(USERNAME_FIELD))
        username_field.click()
        username_field.send_keys(USERNAME)
        print("Username entered.")
    except Exception as e:
        raise LoginError(f"Failed to enter username: {e}")

    # Fill in password
    try:
        password_field = wait.until(EC.element_to_be_clickable(PASSWORD_FIELD))
        print(f"Password field found: {password_field}")

        # Scroll into view to ensure visibility
        driver.execute_script("arguments[0].scrollIntoView();", password_field)

        # Add a small delay
        time.sleep(0.5)

        # Attempt to interact with the field
        password_field.clear()
        password_field.send_keys(PASSWORD)
        print("Entered password using send_keys.")

        # Fallback: Use JavaScript if direct interaction fails
        if not password_field.get_attribute('value'):
            driver.execute_script(f"arguments[0].value = '{PASSWORD}';", password_field)
            print("Entered password using JavaScript.")
    except Exception as e:
        raise LoginError(f"Failed to enter password: {e}")

    # Submit login form
    try:
        login_submit = wait.until(EC.element_to_be_clickable((By.ID, LOGIN_SUBMIT_ID)))
        login_submit.click()
        print("Submitted login form.")
    except Exception as e:
        raise LoginError(f"Failed to submit login form: {e}")

    # Verify login success
    try:
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, f"//button[@aria-label='{CHAT_BUTTON_ARIA_LABEL}']"))
        )
        print("Login successful.")
    except Exception as e:
        raise LoginError(f"Login may have failed. Expected element not found: {e}")
