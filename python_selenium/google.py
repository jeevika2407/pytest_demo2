import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(10)
searchBox=driver.find_element(By.XPATH, "//div/textarea")
print(searchBox.is_enabled())
searchBox.send_keys("Selenium")
time.sleep(10)
search_btn=driver.find_element(By.NAME,value="btnK")

time.sleep(10)
search_btn.click()
driver.quit()
