import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# The 'indirect=True' should only be used for the 'browser' fixture
@pytest.mark.parametrize("browser,url", [
    ("chrome", "https://www.flipkart.com/"),
    ("chrome", "https://www.amazon.in/"),
    ("firefox", "https://www.flipkart.com/"),
    ("firefox", "https://www.amazon.in/")
], indirect=["browser"])
def test_browser(browser, url):
    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    
    driver.maximize_window()
    driver.get(url)
    print(driver.title)
    time.sleep(2)
    driver.quit()
