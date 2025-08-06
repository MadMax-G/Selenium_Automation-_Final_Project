import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://prd.canvusapps.com/signup")

driver.find_element(By.CSS_SELECTOR, "#user_name").send_keys("123")
driver.find_element(By.CSS_SELECTOR, "#user_email").send_keys("maxmadorski@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#user_password").send_keys("123")
driver.find_element(By.CSS_SELECTOR, "#user_password_confirmation").send_keys("456")
driver.find_element(By.CSS_SELECTOR, "#company_name").send_keys("!!!")

driver.find_element(By.CSS_SELECTOR, ".submit.btn.btn-primary").click()

err_msg = driver.find_element(By.CSS_SELECTOR, ".alert.alert-error.alert-block.error").text
print(err_msg)

driver.find_element(By.CSS_SELECTOR, ".span6.text-right a").click()

driver.find_element(By.CSS_SELECTOR, ".form-vertical.well p a").click()

driver.find_element(By.CSS_SELECTOR, "#email").send_keys("maxmadorski@gmail.com")

driver.find_element(By.CSS_SELECTOR, ".actions [name='commit']").click()
input("wwe")