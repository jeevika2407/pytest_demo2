import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium import webdriver
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.zoho.com/signup.html")
email=driver.find_element(By.XPATH,value="//input[@id='email']")
email.send_keys("2k21cse055@kiot.ac.in")

pwd=driver.find_element(By.XPATH,"//input[@id='password']")
pwd.send_keys("Jeevika%1234")

phone=driver.find_element(By.XPATH,"//input[@class='dialphone']")
phone.send_keys("9999900000")

checkbox=driver.find_element(By.XPATH,"//span[@id='signup-termservice']")
checkbox.click()
time.sleep(3)
signup=driver.find_element(By.XPATH,"(//input[@class='signupbtn'])[1]")
signup.click()
time.sleep(5)
captcha=driver.find_element(By.XPATH,"//input[@class='zs-txtfldnew zs-txtfldwidth']")
# captcha.send_keys("123")

# img=driver.find_element(By.XPATH,"//img[@class='za-captcha']")


# captcha_img = driver.find_element(By.CLASS_NAME, "za-captcha")
# location = captcha_img.location
# size = captcha_img.size
# driver.save_screenshot("full_page.png")

# # Crop only the CAPTCHA region
# left = location['x']
# top = location['y']
# right = left + size['width']
# bottom = top + size['height']

# image = Image.open("full_page.png")
# captcha_crop = image.crop((left, top, right, bottom))
# captcha_crop.save("captcha.png")

# # Read CAPTCHA text using pytesseract
# captcha_text = pytesseract.image_to_string(captcha_crop).strip()
# print("Extracted CAPTCHA Text:", captcha_text)

# # Enter the CAPTCHA

# driver.find_element(By.CLASS_NAME, "zs-txtfldnew").send_keys(captcha_text)
# time.sleep(10)

# # Wait for and click signup button again
# WebDriverWait(driver, 10).until(
#     expected_conditions.element_to_be_clickable((By.XPATH, "(//input[@class='signupbtn'])[1]"))
# ).click()


t=input("Please solve the CAPTCHA and press Enter to continue...")
cap=driver.find_element(By.XPATH,value="//input[@name='captcha']")
cap.send_keys(t)




