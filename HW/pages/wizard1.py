import allure
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

class Wizard1:

    def __init__(self,driver):
        self.driver:webdriver = driver

    @allure.step("Login with username: {username}, password: {password}")
    def fill_info(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR,"#login-button").click()
