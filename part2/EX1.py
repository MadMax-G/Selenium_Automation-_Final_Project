import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "#login-button").click()

product_list = driver.find_elements(By.CSS_SELECTOR, ".inventory_item")

for area in product_list:
    product = area.find_element(By.CSS_SELECTOR, ".inventory_item_name")
    if product.text == "Sauce Labs Bike Light":
        button = area.find_element(By.CSS_SELECTOR, ".btn.btn_primary.btn_small.btn_inventory")
        button.click()


input("wwe")