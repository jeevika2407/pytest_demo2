import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# Open Google
driver.get("https://www.google.com/")
time.sleep(2)

# Navigate to Flipkart (corrected URL)
driver.get("https://www.flipkart.com/")
time.sleep(2)

# Go back to Google
driver.back()
time.sleep(2)

# Go forward to Flipkart again
driver.forward()
time.sleep(2)

# Refresh the page
driver.refresh()
time.sleep(2)

# Close the browser
driver.quit()
