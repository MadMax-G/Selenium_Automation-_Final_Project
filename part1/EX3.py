from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.ebay.com/sch/ebayadvsearch")

driver.find_element(By.CSS_SELECTOR, "#_nkw").send_keys("tent")
driver.find_element(By.CSS_SELECTOR, "#_ex_kw").send_keys("gun","sword")
driver.find_element(By.CSS_SELECTOR, ".field__label--end").click()
driver.find_element(By.CSS_SELECTOR, ".adv-form__actions .btn.btn--primary").click()
driver.back()

input("123")