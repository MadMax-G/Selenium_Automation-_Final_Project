from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://galmatalon.github.io/tutorials/indexNoID.html")

driver.find_element(By.CSS_SELECTOR, "#firstname").send_keys("max")
driver.find_element(By.CSS_SELECTOR, "#lastname").send_keys("madorski")
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("max@gmail.com")
driver.find_element(By.CSS_SELECTOR, ".btn.btn-next.btn-fill.btn-warning.btn-wd.btn-sm").click()
driver.find_element(By.CSS_SELECTOR, ".fa.fa-star").click()
driver.find_element(By.CSS_SELECTOR, ".btn.btn-next.btn-fill.btn-warning.btn-wd.btn-sm").click()
driver.find_element(By.CSS_SELECTOR, "[name='streetname']").send_keys("brande")
driver.find_element(By.CSS_SELECTOR, "[name='streetnumber']").send_keys("21")
driver.find_element(By.CSS_SELECTOR, "[name='streetnumber']").send_keys("21")
driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys("petach tikva")
dd = Select(driver.find_element(By.CSS_SELECTOR, "#country"))
dd.select_by_value("Argentina")
driver.find_element(By.CSS_SELECTOR, "#finish").click()

input("www")