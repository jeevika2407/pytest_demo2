import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
# driver.get("https://www.google.co.in")
url="https://www.flipkart.com/"
driver.get(url)
print("Title :",driver.title)
print("Length of the title:",len(driver.title))
print("Current URL : ",driver.current_url)
print("current url and driver url is same or not :",driver.current_url==("https://www.flipkart.com/"))
# print("Page source : ",driver.page_source)
print("Page source length  : ",len(driver.page_source))
time.sleep(5)
driver.close()

