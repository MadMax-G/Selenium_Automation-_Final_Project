import allure
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class Wizard2:

    def __init__(self,driver):
        self.driver:webdriver = driver

    @allure.step("Choosing item: {item}")
    def choose_item(self,item):
        self.driver.find_element(By.CSS_SELECTOR, item).click()

    def to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR,"#shopping_cart_container").click()
