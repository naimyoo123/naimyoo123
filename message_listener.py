# message_listener.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.locators import (
    USERNAME_IN_CONVERSATION,
    MESSAGE_ITEMS,
    USER_MESSAGES_TOOLTIP,
)
from utils.exceptions import ConversationError

def extract_username(driver):
    """
    Extract the username from the conversation header.
    """
    try:
        username_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(USERNAME_IN_CONVERSATION)
        )
        username = username_element.text.strip()
        return username
    except Exception as e:
        raise ConversationError(f"Failed to extract username: {e}")

def extract_new_messages(driver):
    """
    Extract messages sent by the user after your last response.

    Returns:
        List of new messages from the user.
    """
    try:
        messages = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(MESSAGE_ITEMS)
        )
        new_messages = []
        for message in messages:
            try:
                tooltip = message.get_attribute("data-tooltip")
                if tooltip == USER_MESSAGES_TOOLTIP:
                    # Extract the message text
                    message_text = message.find_element(By.CSS_SELECTOR, "div.message__text").text.strip()
                    new_messages.append(message_text)
            except Exception:
                continue  # Skip if any element is not found
        return new_messages
    except Exception as e:
        raise ConversationError(f"Failed to extract messages: {e}")
