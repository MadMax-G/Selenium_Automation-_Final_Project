from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class Wizard4:

    def __init__(self,driver):
        self.driver:webdriver = driver

    def checkout(self):
        self.driver.find_element(By.CSS_SELECTOR,".btn.btn_action.btn_medium.checkout_button").click()

