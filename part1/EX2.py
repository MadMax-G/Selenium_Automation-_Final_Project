from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://login.salesforce.com/")

driver.find_element(By.CSS_SELECTOR, "#forgot_password_link").click()
temp_txt = driver.find_element(By.CSS_SELECTOR, "#header").text
print(temp_txt)
if "Forgot Your Password" in temp_txt:
    driver.find_element(By.CSS_SELECTOR, "#un").send_keys("madmax")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()
    temp_err = driver.find_element(By.CSS_SELECTOR, ".mb16.error").text
    print(temp_err)

input("123")