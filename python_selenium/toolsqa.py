import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.toolsqa.com/selenium-training/")
time.sleep(3)

button = driver.find_element(By.XPATH, "//a[@class='btn btn-primary-shadow btn-block']")
button.click()
print(button.size)
print(button.location)
driver.save_screenshot("toolsqa.png")
time.sleep(5)

driver.forward()
time.sleep(2)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()
time.sleep(2)

driver.quit()
