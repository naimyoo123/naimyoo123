# utils/locators.py
from selenium.webdriver.common.by import By

# Locators for login process
ACCEPT_BUTTON_ID = "cookie_consent_accept_all_button"
LOGIN_NAVIGATE_BUTTON_ID = "newrelic-login-navigate"
USERNAME_FIELD = (By.ID, "username")
PASSWORD_FIELD = (By.ID, "password")  # This is correct based on the HTML
LOGIN_SUBMIT_ID = "newrelic-login-submit"
CHAT_BUTTON_ARIA_LABEL = "Tchat"