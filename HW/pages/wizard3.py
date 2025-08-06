from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class Wizard3:

    def __init__(self,driver):
        self.driver:webdriver = driver

    def add_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR,".btn.btn_primary.btn_small.btn_inventory").click()

    def back(self):
        self.driver.find_element(By.CSS_SELECTOR, "#back-to-products").click()