from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/")

title = driver.find_element(By.CSS_SELECTOR, ".d-1.fw-bold").text
if title == "selenium web site" or "Selenium" in title:
    print("Yes!")
else:
    print("No!")

driver.get("https://www.google.com")
title = driver.find_element(By.CSS_SELECTOR, ".lnXdpd").text
if title == "Google" or "google" in title:
    print("Yes!")
else:
    print("No!")

driver.back()

title = driver.find_element(By.CSS_SELECTOR, ".d-1.fw-bold").text
if title == "selenium web site" or "Selenium" in title:
    print("Yes!")
else:
    print("No!")

input("123")