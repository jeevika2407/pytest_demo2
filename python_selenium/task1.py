import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
f=driver.find_element(By.ID,value="navbar-iframe")
driver.switch_to.frame(f)
time.sleep(3)
s=driver.find_element(By.XPATH,value="//div[@class='bQ1fYb ZObeYc']//table//tr/td/input")
s.click
s.send_keys("Hellooo")
time.sleep(5)
txt=driver.find_element(By.XPATH,"//*[@id='Blog1']/div[1]/div[1]/div[1]/text()[1]")
print(txt.text)