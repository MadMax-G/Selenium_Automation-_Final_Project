from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.udemy.com/")

print(driver.find_element(By.CSS_SELECTOR, ".ud-heading-serif-xxl").text)
print(driver.find_element(By.CSS_SELECTOR, ".ud-heading-serif-xxl").get_attribute("class"))
print(driver.find_element(By.CSS_SELECTOR, ".ud-heading-serif-xxl").tag_name)
print(driver.find_element(By.CSS_SELECTOR, ".ud-heading-serif-xxl").is_displayed())
print(driver.find_element(By.CSS_SELECTOR, ".ud-heading-serif-xxl").is_enabled())

input("123")