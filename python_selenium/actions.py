import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
actions =ActionChains(driver)
blogs = driver.find_element(By.XPATH, "//a//span[@id='blogsmenu']")
# blogs.click()
actions.move_to_element(blogs).perform()
option2 = driver.find_element(By.XPATH, "(//a//span)[4]")
actions.click(option2).perform()
time.sleep(5)
driver.quit()


