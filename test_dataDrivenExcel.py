import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities import excelLogic 

@pytest.mark.parametrize("username,password,status", excelLogic.get_data("ExcelFiles/loginData.xlsx", "Sheet1"))
class TestLogin:

    def test_valid_login(self,username, password,status):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.demoblaze.com/index.html")

        driver.find_element(By.ID, "login2").click()
        time.sleep(1)

        driver.find_element(By.ID, "loginusername").send_keys(username)
        driver.find_element(By.ID, "loginpassword").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Log in']").click()

        time.sleep(3)

        if status=="test1" or status=="test2":
            assert "Welcome" in driver.page_source
        else:
                alert = driver.switch_to.alert
                assert "Wrong password." in alert.text
                alert.accept()



