import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class Wizard5:

    def __init__(self,driver):
        self.driver:webdriver = driver

    def fill_info(self, first, last, zipcode):
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first)
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last)
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(zipcode)

    def continue_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()