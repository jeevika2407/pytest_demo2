import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
driver.implicitly_wait(10)

links = driver.find_elements(By.XPATH, "//div[@id='LinkList1']//a")
print(len(links))

for link in links:
    print(link.get_attribute("href"))

action = ActionChains(driver)
for link in links:
    action.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL)

action.perform()

time.sleep(3)
driver.quit()
