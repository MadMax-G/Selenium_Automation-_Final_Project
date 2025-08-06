import time
from os import wait3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.asos.com/")

driver.find_element(By.CSS_SELECTOR, "#chrome-search").send_keys("Adidas")
time.sleep(1)
item_list = driver.find_elements(By.CSS_SELECTOR, "#search-results li")
for item in item_list:
    if "Adidas Samba" in item.text:
        item.click()
        break

driver.find_element(By.CSS_SELECTOR, "#product-207192824").click()

dd = driver.find_element(By.CSS_SELECTOR, "#variantSelector")
dd = Select(dd)
dd.select_by_index(1)

driver.find_element(By.CSS_SELECTOR, ".jAEfQ.LLfrW.Tyz1C").click()


input("wwe")