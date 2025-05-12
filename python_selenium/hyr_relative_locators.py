import time
from selenium import webdriver
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.hyrtutorials.com/p/css-selectors-practice.html")

firstname = driver.find_element(By.XPATH, "//input[@id='firstName']")
firstname.send_keys("jeevika")
lastname = driver.find_element(locate_with(By.TAG_NAME, "input").below(firstname))
lastname.send_keys("balaj")
city=driver.find_element(By.XPATH,"//input[@class='city']")
city.send_keys("salem")
country=driver.find_element(locate_with(By.TAG_NAME,"input").below(city))
country.send_keys("india")
gender=driver.find_element(locate_with(By.TAG_NAME,"input").above(city))
gender.send_keys("female")
sec=driver.find_element(By.XPATH,"//input[@placeholder='Enter your security question']")
sec.send_keys("hello")
sec2=driver.find_element(locate_with(By.XPATH,"//input[@placeholder='Enter your security answer']").below(sec))
sec2.send_keys("world")
sec3=driver.find_element(locate_with(By.XPATH,"//input[@placeholder='Verify your personal details']").below(sec))
sec3.send_keys("world")

button1=driver.find_element(By.XPATH,"//input[@value='Buttton1']")
button1.click()
time.sleep(5)

button2=driver.find_element(locate_with(By.XPATH,"//input[@value='Buttton2']").to_left_of(button1))
button2.click()
time.sleep(3)

button3=driver.find_element(locate_with(By.XPATH,"//button[@id='button3']").to_right_of(button2))
button3.click()
time.sleep(5)

# time.sleep(3)

driver.quit()


