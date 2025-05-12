# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By 
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
# parent=driver.current_window_handle

# driver.find_element(By.XPATH,"//a[@id='selenium143']").click()
# time.sleep(3)
# windowid=driver.window_handles

# for w in windowid:
#     if w != parent:
#         driver.switch_to.window(w)
#         windowtext = driver.find_element(By.XPATH, "//a[@href='http://selenium-by-arun.blogspot.com/2012/11/what-is-selenium.html']").text
#         print("current url:", driver.current_url)
#         print(windowtext)
#         if driver.title.__eq__("Selenium143 "):
#             driver.close()
#         break
   
# driver.switch_to.window(parent)
# time.sleep(3)




import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
pw=driver.current_window_handle
# ele=driver.find_element(By.XPATH,value="//a[@id='selenium143']")
ele=driver.find_element(By.XPATH,value="//*[@id='HTML37']/div[1]/p/a")
ele.click()
time.sleep(3)
cw=driver.window_handles
for c in cw:
    if c!=pw:
        driver.switch_to.window(c)
        if driver.title == "New Window":
            ele=driver.find_element(By.XPATH,value="//div[@class='example']/h3")
            # print(driver.current_url)
            print(ele.text)
            driver.close()
            break