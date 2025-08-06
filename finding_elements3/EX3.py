import time
from os import wait3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.mytinytodo.net/demo/#list/1")

def add_task(name):
    driver.find_element(By.CSS_SELECTOR, "#task").send_keys(name)
    driver.find_element(By.CSS_SELECTOR, "#newtask_submit").click()

add_task("task1")
time.sleep(1)
add_task("task2")
time.sleep(1)
print(driver.find_element(By.CSS_SELECTOR, "#total").text)

input("wwe")