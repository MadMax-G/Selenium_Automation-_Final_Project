import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.ebay.com/")

driver.find_element(By.CSS_SELECTOR, "#gh-ac").send_keys("tent")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#gh-search-btn").click()

def print_items():
    items_list = driver.find_elements(By.CSS_SELECTOR, ".s-item__title")
    for item in items_list:
        print(item.text)

print_items()
for i in range(9):
    driver.find_element(By.CSS_SELECTOR, ".pagination__next.icon-link").click()
    time.sleep(1)
    print_items()


input("wwe")