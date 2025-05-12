import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch browser and navigate to the URL
driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")

# Maximize the window (optional)
driver.maximize_window()

# Wait for the page to load
time.sleep(2)

# Click the "Try it" button to trigger an alert
# This button is under the "Alert Box" section
alert_button = driver.find_element(By.ID, "alert1")
alert_button.click()

# Wait for the alert to appear
time.sleep(1)

# Switch to the alert
alert = driver.switch_to.alert

# Print alert text
print("Alert says:", alert.text)

# Accept the alert (click OK)
alert.accept()

# Optional: Close the browser
time.sleep(1)
driver.quit()
