import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

def click_element(driver, by, value, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
        driver.execute_script("arguments[0].click();", element)
    except Exception as e:
        print(f"Click failed: {e}")

click_element(driver, By.XPATH,"//input[@id='alert1']")
alert = driver.switch_to.alert

print("Alert says:", alert.text)


alert.accept()
driver.quit()
