import time
import allure
from selenium.webdriver.common.by import By
from asos_automation_proj.pages.base_page import BasePage
from asos_automation_proj.pages.home_page import HomepageWizard



class LoginWizard(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    __EMAIL = (By.CSS_SELECTOR, "#email")
    __PASSWORD = (By.CSS_SELECTOR, "#password")
    __NEXT_BTN = (By.CSS_SELECTOR, ".button-module_button__17Mvp.button-module_primary__kFgMN")
    __SIGN_IN_BTN = (By.CSS_SELECTOR, ".button-module_content__35zEt")

    def fill_email(self,  email):
        with allure.step("Click on 'sign in' button"):
            hw = HomepageWizard(self.driver)
            hw.sign_in()
        with allure.step("login with email: {email}"):
            self.fill_text(self.__EMAIL, email)
            time.sleep(1)
        with allure.step("Click on 'continue' button"):
            self.click(self.__NEXT_BTN)
            time.sleep(3)

    @allure.step("login with invalid email: {email}")
    def fill_invalid_email(self, email):
        self.fill_email(email)
        with allure.step("Check if an appropriate error message is displayed"):
            alert = self.driver.find_element(By.CSS_SELECTOR, ".hgdilB1r9wGHTwyS5Aow")
            assert "Oops! Please type in your correct email address" in alert.text
            time.sleep(3)


    def fill_password(self, password):
        with allure.step("Enter password: {password}"):
            self.fill_text(self.__PASSWORD, password)
            time.sleep(1)
        with allure.step("Click on 'sign in' button"):
            self.click(self.__SIGN_IN_BTN)
            time.sleep(3)
