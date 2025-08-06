import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/")

#link_list = driver.find_elements(By.CSS_SELECTOR, ".td-home a")
#for link in link_list:
#    print(link.text)

link_list = driver.find_elements(By.CSS_SELECTOR, ".td-home a")
for link in link_list:
    if "Selenium" in link.text:
        print(link.text)

input("wwe")