# test_search.py
import time
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("test_setUp")
class TestSearch:
    
    def test_hp(self):
        ele = self.driver.find_element(By.NAME, "search")
        ele.send_keys("Hp")
        self.driver.find_element(By.CLASS_NAME, "btn-default").click()
        time.sleep(2)
        assert "HP" in self.driver.find_element(By.CSS_SELECTOR, ".caption h4 a").text

def test_Honda(test_setUp):
    driver = test_setUp
    ele = driver.find_element(By.XPATH, "//input[@name='search']")
    ele.send_keys("Honda")
    btn = driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']")
    btn.click()
    time.sleep(3)
    txt = driver.find_element(By.XPATH, "//*[@id='content']/p[2]").text
    assert "There is no product that matches the search criteria." in txt

def test_Empty(test_setUp):
    driver = test_setUp
    ele = driver.find_element(By.XPATH, "//input[@name='search']")
    ele.send_keys("")
    btn = driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']")
    btn.click()
    time.sleep(3)
    txt = driver.find_element(By.XPATH, "//*[@id='content']/p[2]").text
    assert "There is no product that matches the search criteria." in txt
