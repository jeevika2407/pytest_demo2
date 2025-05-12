from selenium.webdriver.support.relative_locator import locate_with
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
sel=driver.find_element(By.ID,value="drop1")
select=Select(sel)
dropoptions=select.options
print(len(dropoptions))
for op in dropoptions:
    print(op.text)
# select.select_by_visible_text("doc 2")
# select.select_by_value("mno")
select.select_by_index(4)