import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "#login-button").click()

items_list = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
for item in items_list:
    print(item.text)

input("wwe")