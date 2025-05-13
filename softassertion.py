import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions 


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://parabank.parasoft.com/parabank/index.htm")
register=driver.find_element(By.XPATH,"(//div[@id='loginPanel']/descendant::p)[4]//a")
register.click()
fname=driver.find_element(By.XPATH,"//input[@id='customer.firstName']")
fname.send_keys("jeev")
lname=driver.find_element(locate_with(By.XPATH,"(//form[@id='customerForm']/descendant::input)[2]").below(fname))
lname.send_keys("balaj")
address=driver.find_element(locate_with(By.XPATH,"(//form[@id='customerForm']/descendant::input)[3]").below(lname))
address.send_keys("123 street")
city=driver.find_element(locate_with(By.XPATH,"(//form[@id='customerForm']/descendant::input)[4]").below(lname))
city.send_keys("slm")
state=driver.find_element(locate_with(By.XPATH,"(//form[@id='customerForm']//child::input)[5]").below(lname))
state.send_keys("TN")
zip=driver.find_element(locate_with(By.XPATH,"(//form[@id='customerForm']//child::input)[6]").below(state))
zip.send_keys("123456")
ssn=driver.find_element(locate_with(By.XPATH,"(//form[@id='customerForm']//child::input)[8]").below(state))
ssn.send_keys("123")
phone=driver.find_element(locate_with(By.XPATH,"(//form[@id='customerForm']/descendant::input)[7]").above(ssn))
phone.send_keys("9876543210")

username=driver.find_element(locate_with(By.XPATH,"(//form[@id='customerForm']/descendant::input)[9]").below(ssn))
username.send_keys("jeevikaaaa010")
pwd=driver.find_element(locate_with(By.XPATH,"(//form[@id='customerForm']/descendant::input)[10]").below(username))
pwd.send_keys("jeevika123")
confirm=driver.find_element(locate_with(By.XPATH,"(//form[@id='customerForm']/descendant::input)[11]").below(pwd))
confirm.send_keys("jeevika123")
register=driver.find_element(locate_with(By.XPATH,"(//form[@id='customerForm']/descendant::input)[12]").below(confirm))
register.click()

regText=driver.find_element(By.XPATH,"//*[@id='rightPanel']/h1").text
# print("register verification: ",regText.text)
assert "jeevikaaaa010" in regText

# lusername=driver.find_element(By.XPATH,"//input[@name='username']")
# lusername.send_keys("jeevika")
# lpassword=driver.find_element(locate_with(By.XPATH,"//input[@name='password']").below(lusername))
# lpassword.send_keys("jeevika123")
# login=driver.find_element(locate_with(By.XPATH,"//input[@type='submit']").below(lpassword))
# login.click()
# loginText=driver.find_element(By.XPATH,"//div[@id='showOverview']/h1")
# txt=loginText.text
# print("login verification: ",txt)
