from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://prd.canvusapps.com/signup")

driver.find_element(By.CSS_SELECTOR, "#user_name").send_keys("max")
driver.find_element(By.CSS_SELECTOR, "#user_email").send_keys("max@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#user_password").send_keys("max123")
driver.find_element(By.CSS_SELECTOR, "#user_password_confirmation").send_keys("max123")
driver.find_element(By.CSS_SELECTOR, "#company_name").send_keys("AUTOMATION.COM")
driver.find_element(By.CSS_SELECTOR, "[name=commit]").click()
temp_txt = driver.find_element(By.CSS_SELECTOR, ".alert.alert-error.alert-block.error").text
print(temp_txt)

input("123")