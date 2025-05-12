import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

def flash_element(element):
    for i in range(1, 30):
        driver.execute_script("arguments[0].style.background='red'", element)
        time.sleep(0.2)
        default_color = element.value_of_css_property('background-color')
        driver.execute_script(f"arguments[0].style.background='{default_color}'", element)

element = driver.find_element(By.ID, "alert1")
flash_element(element)
time.sleep(2)
driver.quit()
