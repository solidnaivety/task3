import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture(scope="session")
def driver():
    # Setup Chrome WebDriver using webdriver-manager
    options = webdriver.ChromeOptions()
    # Run in headful mode
    # Remove headless option if previously set
    # options.add_argument("--headless")  # Ensure headful
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def navigate_menu(driver, menu_path):
    """
    Navigate through the menu based on the provided menu_path list.
    Example: ['Dev Challenge', 'About']
    """
    for item in menu_path:
        menu_item = driver.find_element(By.LINK_TEXT, item)
        menu_item.click()
        time.sleep(1)  # Wait for the menu to load

def test_contact_email_visible(driver):
    # Case #001 - Contact email is visible
    driver.get("https://www.devchallenge.it")
    navigate_menu(driver, ["Dev Challenge", "About"])
    # Scroll down to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for scrolling
    # Verify contact email is displayed
    try:
        contact_email = driver.find_element(By.XPATH, "//a[contains(@href, 'mailto:hello@devchallenge.it')]")
        assert contact_email.is_displayed(), "Contact email is not visible."
        assert contact_email.text == "hello@devchallenge.it", "Contact email text does not match."
    except Exception as e:
        pytest.fail(f"Test failed: {e}")

def test_count_judges(driver):
    # Case #002 - Count judges
    driver.get("https://www.devchallenge.it")
    navigate_menu(driver, ["Dev Challenge", "Judges"])
    time.sleep(2)  # Wait for page to load
    # Assuming judges are listed with a specific class or tag
    judges = driver.find_elements(By.CSS_SELECTOR, ".judge")  # Replace with actual selector
    assert len(judges) == 6, f"Expected 6 judges, but found {len(judges)}."

def test_no_mobile_partners():
    # Case #003 - No mobile partners
    options = webdriver.ChromeOptions()
    mobile_emulation = { "deviceMetrics": { "width": 360, "height": 800, "pixelRatio": 3.0 },
                        "userAgent": "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36" }
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.set_window_size(360, 800)
    driver.get("https://www.devchallenge.it")
    navigate_menu(driver, ["Dev Challenge", "Partners"])
    time.sleep(2)  # Wait for page to load
    # Verify 'Apple Inc' is not in the partners list
    partners = driver.find_elements(By.XPATH, "//*[contains(text(), 'Apple Inc')]")
    assert len(partners) == 0, "Apple Inc is present in the partners list."
    driver.quit()
