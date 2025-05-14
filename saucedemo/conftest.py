# import pytest
# from selenium import webdriver
# import read_config

# @pytest.fixture()
# def setup_and_teardown():
#     browser = read_config.get_config('browser', 'b')
#     url = read_config.get_config('url', 'u')

#     if browser == "chrome":
#         driver = webdriver.Chrome()
#     elif browser == "firefox":
#         driver = webdriver.Firefox()
#     elif browser == "edge":
#         driver = webdriver.Edge()

#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get(url)

#     yield driver 
#     driver.quit()

import pytest
from selenium import webdriver
from util.excelReader import get_data
from read_config import get_config
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup_and_teardown():
    browser = get_config('browser', 'b')
    url = get_config('url', 'u')

    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_options)

    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser in config.ini")

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)

    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login_data():
    file = "D:\\sc_python_selenium\\saucedemo\\ExcelFile\\logindata.xlsx"
    sheet = "Sheet1"
    return get_data(file, sheet)
