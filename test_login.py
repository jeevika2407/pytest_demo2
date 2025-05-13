import pytest
import time
from selenium.webdriver.common.by import By
import read_config

@pytest.mark.usefixtures("set_up_and_tear_down")
class TestLogin:
    def test_valid_login(self):
        self.driver.find_element(By.ID, "login2").click()
        time.sleep(1) 

        username = read_config.get_config("login credentials", "uname")
        password = read_config.get_config("login credentials", "pass")

        self.driver.find_element(By.ID, "loginusername").send_keys(username)
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        time.sleep(3)

        assert "Welcome" in self.driver.page_source

        self.driver.find_element(By.XPATH,"")
        
        
