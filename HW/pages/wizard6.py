import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class Wizard6:

    def __init__(self,driver):
        self.driver:webdriver = driver

    def finish_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, "#finish").click()