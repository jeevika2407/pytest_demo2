import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
driver.implicitly_wait(10)

links = driver.find_elements(By.XPATH, "//div[@id='LinkList1']//a")
print(f"Total links found: {len(links)}")

def verify_link(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        if response.status_code == 200:
            print(f"{url} - working Link ({response.status_code})")
        else:
            print(f"{url} - broken Link ({response.status_code})")
    except requests.RequestException as e:
        print(f"{url} - Error: {e}")

for link in links:
    href = link.get_attribute("href")
    print(href)
    if href:
        verify_link(href)

action = ActionChains(driver)
for link in links:
    action.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL)
action.perform()

time.sleep(3)
driver.quit()
