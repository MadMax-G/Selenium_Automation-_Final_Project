import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

def choose_prod(prod_name):
    product_list = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_label a")
    for item in product_list:
        if item.text == prod_name:
            item.click()
            break

driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "#login-button").click()
choose_prod("Sauce Labs Bike Light")
driver.find_element(By.CSS_SELECTOR, "#add-to-cart").click()
driver.find_element(By.CSS_SELECTOR, "#back-to-products").click()
choose_prod("Sauce Labs Fleece Jacket")
driver.find_element(By.CSS_SELECTOR, "#add-to-cart").click()
driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container a").click()
driver.find_element(By.CSS_SELECTOR, "#checkout").click()
driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("max")
driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("mxd")
driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("49316")
driver.find_element(By.CSS_SELECTOR, "#continue").click()
driver.find_element(By.CSS_SELECTOR, "#finish").click()
print(driver.find_element(By.CSS_SELECTOR, ".complete-header").text)


input("wwe")