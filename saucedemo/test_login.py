# import pytest
# import time
# from selenium.webdriver.common.by import By
# from util import excelReader

# @pytest.mark.usefixtures("setup_and_teardown")
# class TestLogin:
#     @pytest.mark.parametrize("username,password,test", excelReader.get_data("ExcelFile/logindata.xlsx", "Sheet1"))
#     def test_valid_login(self, setup_and_teardown, username, password, test):
#         driver = setup_and_teardown

#         driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
#         driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
#         driver.find_element(By.XPATH, "//input[@id='login-button']").click()

#         time.sleep(3)

#         if test in ["test1", "test3", "test4", "test5", "test6"]:
#             exp = driver.find_element(By.XPATH, "//div[@class='app_logo']").text
#             act = "Swag Labs"
#             assert act == exp

#         elif test == "test2":
#             exp = driver.find_element(By.XPATH, "//h3").text
#             act = "Epic sadface: Sorry, this user has been locked out."
#             assert act == exp
#             print("Actual:", act)
#             print("Expected:", exp)


import pytest
import time
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_login_all(self, setup_and_teardown, login_data):
        driver = setup_and_teardown
        for index in range(len(login_data)):
        # for username, password, test in login_data:
            driver.get("https://www.saucedemo.com/")
            username, password, test=login_data[index]

        # for username, password, test in login_data:
            # driver.find_element(By.XPATH, "//input[@id='user-name']").clear()
            # driver.find_element(By.XPATH, "//input[@id='password']").clear()

            driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
            driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
            driver.find_element(By.XPATH, "//input[@id='login-button']").click()
           

            time.sleep(2)

        if test in ["test1", "test3", "test4", "test5", "test6"]:
            exp = driver.find_element(By.XPATH, "//div[@class='app_logo']").text
            act = "Swag Labs"
            assert act == exp

        elif test == "test2":
            exp = driver.find_element(By.XPATH, "//h3").text
            act = "Epic sadface: Sorry, this user has been locked out."
            assert act == exp
            print("Actual:", act)
            print("Expected:", exp)


        