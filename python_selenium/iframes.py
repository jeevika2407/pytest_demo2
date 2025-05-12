from selenium.webdriver.support.relative_locator import locate_with
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://letcode.in/frame")
time.sleep(3)
driver.switch_to.frame(1)
uname=driver.find_element(By.XPATH,value="//input[@name='fname']")
uname.send_keys("jee")
lname=driver.find_element(By.XPATH,value="//input[@name='lname']")
lname.send_keys("bala")
time.sleep(3)
cf=driver.find_element(By.XPATH,value="//div[@class='container has-text-centered mb-4 mt-6']/child::iframe")
driver.switch_to.frame(cf)
email=driver.find_element(By.XPATH,value="//input[@name='email']")
email.send_keys("jee@gmail.com")