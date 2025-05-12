import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://selenium08.blogspot.com/2019/07/check-box-and-radio-buttons.html")

red = driver.find_element(By.XPATH, "//div/input[@value='red']")
time.sleep(10)
print(red.is_enabled())
time.sleep(10)
print(red.is_selected())
time.sleep(10)
opera = driver.find_element(By.XPATH, "//*[@id='post-body-7702345506409447484']/div/div/input[3]")
time.sleep(10)
print(opera.is_enabled())
