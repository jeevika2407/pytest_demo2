import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.parametrize("search_term", ["Selenium WebDriver", "PyTest Tutorial", "Python programming"])
def test_google_search(set_up_and_tear_down, search_term):
    driver = set_up_and_tear_down  # Use the driver from the fixture

    # Wait for the search box to be visible before interacting with it
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//textarea[@class='gLFyf']"))
    )

    search_box.send_keys(search_term)
    search_box.submit()  # Submit the search
    time.sleep(2)  # Wait for search results to load (you can also use WebDriverWait here)