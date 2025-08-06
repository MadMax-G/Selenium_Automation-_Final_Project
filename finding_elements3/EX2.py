import time
from os import wait3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

def choose_prod(prod_name):
    product_list = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_description")
    for item in product_list:
        if prod_name in item.text:
            item.find_element(By.CSS_SELECTOR, ".btn.btn_primary.btn_small.btn_inventory").click()
            break

driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "#login-button").click()

choose_prod("Sauce Labs Bike Light")
time.sleep(1)
choose_prod("Sauce Labs Fleece Jacket")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container a").click()
driver.find_element(By.CSS_SELECTOR, "#checkout").click()
driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("max")
driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("mxd")
driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("49316")
driver.find_element(By.CSS_SELECTOR, "#continue").click()
driver.find_element(By.CSS_SELECTOR, "#finish").click()
print(driver.find_element(By.CSS_SELECTOR, ".complete-header").text)

input("wwe")