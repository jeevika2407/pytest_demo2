import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
driver.implicitly_wait(10)
actions = webdriver.ActionChains(driver)
driver.find_element(By.ID, value = "input-email").send_keys("Helo@gmail.com")
driver.find_element(By.ID, value = "input-password").send_keys("Helo123")
actions.send_keys(Keys.ENTER).perform()
time.sleep(3)
driver.quit()