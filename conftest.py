# conftest.py
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager

# @pytest.fixture(scope="function")
# def browser(request):
#     # Get the browser parameter from the test
#     browser = request.param
#     if browser == "chrome":
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     elif browser == "firefox":
#         driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#     else:
#         raise ValueError(f"Browser {browser} is not supported!")

#     yield driver  # Provide the driver to the test function

#     # Teardown after test
#     driver.quit()


# import pytest
# from selenium import webdriver

# @pytest.fixture()
# def set_up_and_tear_down():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get("https://www.google.com")  # Go to Google home page
#     yield driver  # Yielding driver so it can be used in the test
#     driver.quit()

# import pytest
# from selenium import webdriver

# @pytest.fixture(params=["https://www.google.com"])
# def set_up_and_tear_down(request):
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get(request.param)  # Open the URL passed by param
#     yield driver
#     driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["chrome", "firefox"])
def set_up_and_tear_down(request):
    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.demoblaze.com/index.html")
    request.cls.driver = driver
    yield
    driver.quit()
