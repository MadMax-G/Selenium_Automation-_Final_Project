from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://login.salesforce.com/")

driver.find_element(By.CSS_SELECTOR, "#username").send_keys("madmax")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("max123456")
driver.find_element(By.CSS_SELECTOR, "#rememberUn").click()
IsChecked = driver.find_element(By.CSS_SELECTOR,"#rememberUn").is_selected()
if IsChecked is True:
    driver.find_element(By.CSS_SELECTOR, "#Login").click()

input("123")