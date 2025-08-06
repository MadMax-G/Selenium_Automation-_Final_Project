from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://galmatalon.github.io/tutorials/indexNoID.html")

driver.find_element(By.ID, "firstname").send_keys("Max")
driver.find_element(By.ID, "lastname").send_keys("Madorski")
driver.find_element(By.ID, "email").send_keys("max@gmail.com")
driver.find_element(By.CSS_SELECTOR, ".btn.btn-next.btn-fill.btn-warning.btn-wd.btn-sm").click()
driver.find_element(By.CSS_SELECTOR,".icon").click()
driver.find_element(By.CSS_SELECTOR, "[name='next']").click()
driver.find_element(By.CSS_SELECTOR, "[name='streetname']").send_keys("Brande zeev")
driver.find_element(By.CSS_SELECTOR, "[name='streetnumber']").send_keys("21")
driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys("Petach Tikva")
driver.find_element(By.CSS_SELECTOR, "#finish").click()

temp_txt = driver.find_element(By.CSS_SELECTOR,".cta-title").text
if temp_txt == "Congratulations!":
    print("lets fucking gooooooooo!")
input(123)