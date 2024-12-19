from browser import launch_browser, close_browser
from login import perform_login
from config import WEBSITE_URL

def main():
    driver = None
    try:
        driver = launch_browser()
        perform_login(driver, WEBSITE_URL)
    except Exception as e:
        print(f"Login failed: {e}")
    finally:
        if driver:
            close_browser(driver)
        print("Browser closed.")

if __name__ == "__main__":
    main()
