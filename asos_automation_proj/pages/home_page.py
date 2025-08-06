import time
import allure
from selenium.webdriver.common.by import By
from asos_automation_proj.pages.base_page import BasePage

class HomepageWizard(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    __SEARCH_BAR = (By.CSS_SELECTOR,"#chrome-search")
    __WOMEN_BTN = (By.CSS_SELECTOR, "#women-floor")
    __ACCOUNT_DROPDOWN = (By.CSS_SELECTOR, "#myAccountDropdown")
    __MY_ACCOUNT = (By.CSS_SELECTOR,".pggyrBd.FfmKyt0.ZqXYTuz")
    __MY_ORDERS = (By.CSS_SELECTOR, ".cWzaeb1.FfmKyt0.ZqXYTuz")
    __RETURNS_INFO = (By.CSS_SELECTOR, ".UFGk9wq.FfmKyt0.ZqXYTuz")
    __CONTACT_PREF = (By.CSS_SELECTOR, ".LjZGpn8.FfmKyt0.ZqXYTuz")
    __SAVED_ITEMS_BTN = (By.CSS_SELECTOR, ".vQeUV7s.c_IO2I_.AYL96eR.JpgornA.isI7xiu")
    __SHOPPING_BAG_BTN = (By.CSS_SELECTOR, ".LpoEdV8.c_IO2I_.AYL96eR.JpgornA.isI7xiu")
    __SHOES_BTN = (By.CSS_SELECTOR, ".87a52035-f6fa-401f-bd58-0d259e403cbb")
    __SIGN_IN = (By.CSS_SELECTOR, ".U32RJ0i.TYb4J9A.EVhxZk8.leavesden2")
    __CHOSEN_ITEM = (By.CSS_SELECTOR, ".GSho_2H.Dgji62M #search-result-0")

    def search(self,  text):
        with allure.step("Click on the search bar"):
            self.click(self.__SEARCH_BAR)
        with allure.step("Type in the search bar: {text}"):
            self.fill_text(self.__SEARCH_BAR, text)
            time.sleep(2)

    def women_category(self):
        with allure.step("Click on women's category"):
            self.click(self.__WOMEN_BTN)
            time.sleep(2)

    def my_account(self):
        with allure.step("Click on the person (account) dropdown"):
            self.click(self.__ACCOUNT_DROPDOWN)
            time.sleep(1)
        with allure.step("Click on 'my account'"):
            self.click(self.__MY_ACCOUNT)
            time.sleep(2)

    def my_orders(self):
        with allure.step("Click on the person (account) dropdown"):
            self.click(self.__ACCOUNT_DROPDOWN)
            time.sleep(1)
        with allure.step("Click on 'my orders'"):
            self.click(self.__MY_ORDERS)
            time.sleep(2)

    def returns_info(self):
        with allure.step("Click on the person (account) dropdown"):
            self.click(self.__ACCOUNT_DROPDOWN)
            time.sleep(1)
        with allure.step("Click on 'returns info'"):
            self.click(self.__RETURNS_INFO)
            time.sleep(2)

    def contact_preferences(self):
        with allure.step("Click on the person (account) dropdown"):
            self.click(self.__ACCOUNT_DROPDOWN)
            time.sleep(1)
        with allure.step("Click on 'contact preferences'"):
            self.click(self.__CONTACT_PREF)
            time.sleep(2)

    def saved_items(self):
        with allure.step("Click on 'saved items'"):
            self.click(self.__SAVED_ITEMS_BTN)
            time.sleep(2)

    def shopping_bag(self):
        with allure.step("Click on 'shopping bag'"):
            self.click(self.__SHOPPING_BAG_BTN)
            time.sleep(2)

    def sign_in(self):
        with allure.step("Click on the person (account) dropdown"):
            self.click(self.__ACCOUNT_DROPDOWN)
            time.sleep(1)
        with allure.step("Click on 'sign in'"):
            self.click(self.__SIGN_IN)
            time.sleep(2)

    def search_and_choose(self, text):
        with allure.step("Click on the search bar"):
            self.click(self.__SEARCH_BAR)
        with allure.step("Type in the search bar: {text}"):
            self.fill_text(self.__SEARCH_BAR, text)
            time.sleep(1)
        with allure.step("Click on: {text}"):
            self.click(self.__CHOSEN_ITEM)
            time.sleep(2)



