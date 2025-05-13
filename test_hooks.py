import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Fixture to set up and tear down the browser
@pytest.fixture(params=["chrome", "firefox"], scope="module")  # Change to "module" if needed
def set_up_and_tear_down(request):
    browser = request.param
    print(f"\n[Fixture] Launching {browser} browser...")

    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError("Unsupported browser")

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.google.com")

    yield driver

    print(f"[Fixture] Quitting {browser} browser...")
    driver.quit()


# Hook to run before each test function
def pytest_runtest_setup(item):
    print(f"\n[Hook] Starting test: {item.name}")

# Hook to run after each test function
def pytest_runtest_teardown(item, nextitem):
    print(f"[Hook] Finished test: {item.name}")


# Test 1: Check page title
def test_google_title(set_up_and_tear_down):
    driver = set_up_and_tear_down
    assert "Google" in driver.title

# Test 2: Check URL
def test_google_url(set_up_and_tear_down):
    driver = set_up_and_tear_down
    assert driver.current_url == "https://www.google.com/"
