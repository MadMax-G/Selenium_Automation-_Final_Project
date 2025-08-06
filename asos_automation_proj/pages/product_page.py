import time
import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from asos_automation_proj.pages.base_page import BasePage
from asos_automation_proj.pages.home_page import HomepageWizard

class ProductPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    __PROD_ID = (By.CSS_SELECTOR, "#product-207633546")
    __SELECT_SIZE = (By.CSS_SELECTOR, ".C09ug #variantSelector")
    __ADD_TO_BAG = (By.CSS_SELECTOR, ".jAEfQ.LLfrW.Tyz1C")
    __ITEM_REMOVE = (By.CSS_SELECTOR, ".bag-item-remove")
    __BAG_BUTTON = (By.CSS_SELECTOR, "#miniBagDropdown")
    __VIEW_BAG = (By.CSS_SELECTOR, ".qQoHatg.sY3mB1c.london3-button.hgH_Y9G")
    __CHECKOUT = (By.CSS_SELECTOR, ".qQoHatg.sY3mB1c.london3-button.mZPCs_0")
    __SIZE_BTN_MYBAG = (By.CSS_SELECTOR, ".bag-item-size-holder.bag-item-select2-holder")
    __SIZE_QTY_MYBAG = (By.CSS_SELECTOR, ".bag-item-quantity-holder.bag-item-select2-holder")
    __UPDATE = (By.CSS_SELECTOR, ".bag-item-edit-update")
    __SAVE_FOR_LATER = (By.CSS_SELECTOR, ".bag-item-save")
    __CHANGE_COUNTRY_BTN = (By.CSS_SELECTOR, ".breiRmE.TYb4J9A")
    __CHOOSE_COUNTRY = (By.CSS_SELECTOR, "#country")
    __UPDATE_PREFERENCES_BTN = (By.CSS_SELECTOR, ".AlRI892.nEgs3gH.london2-button")
    __CHOOSE_CURRENCY = (By.CSS_SELECTOR, "#currency")
    __FACEBOOK_LINK = (By.CSS_SELECTOR, '[data-testid="social-link"]')
    __RIGHT_PICTURE = (By.CSS_SELECTOR, ".arrow-button.arrow-button-right")
    __LEFT_PICTURE = (By.CSS_SELECTOR, ".arrow-button.arrow-button-left")

    def sort_func_prod_page(self, sort_type, select):
        sort_list = self.driver.find_elements(By.CSS_SELECTOR, ".button_eZ0Gy")
        for sort in sort_list:
            if sort_type in sort.text:
                sort.click()
                category_list = self.driver.find_elements(By.CSS_SELECTOR, ".value_hLBn8")
                for category in category_list:
                    if select in category.text:
                        category.click()

    def select_prod(self):
        with allure.step("Search and choose a product"):
            hw = HomepageWizard(self.driver)
            hw.search_and_choose("jeans")
        with allure.step("Click on the product"):
            self.click(self.__PROD_ID)
            time.sleep(2)

    def select_size(self):
        with allure.step("Select a product"):
            self.select_prod()
        with allure.step("Select the size"):
            self.click(self.__SELECT_SIZE)
            element = self.driver.find_element(By.CSS_SELECTOR, "#variantSelector")
            dropdown = Select(element)
            dropdown.select_by_visible_text("EU 40")
            time.sleep(2)

    def add_to_basket(self):
        with allure.step("Select the product and the size"):
            self.select_size()
        with allure.step("Add the product to the bag"):
            self.click(self.__ADD_TO_BAG)
            time.sleep(2)

    def remove_from_basket(self):
        with allure.step("Add product to the bag"):
            self.add_to_basket()
            time.sleep(1)
        with allure.step("Click on the person (account) dropdown and click 'view bag'"):
            self.click(self.__VIEW_BAG)
            time.sleep(2)
        with allure.step("Remove product from the bag"):
            self.click(self.__ITEM_REMOVE)
            time.sleep(2)

    def modify_item_size_in_basket(self):
        with allure.step("Add product to the bag"):
            self.add_to_basket()
            time.sleep(1)
        with allure.step("Click on the person (account) dropdown and click 'view bag'"):
            self.click(self.__VIEW_BAG)
            time.sleep(2)
        with allure.step("Modify the size of the product"):
            self.click(self.__SIZE_BTN_MYBAG)
            time.sleep(2)
            element = self.driver.find_element(By.CSS_SELECTOR, ".bag-item-size.bag-item-selector.select2-hidden-accessible")
            dropdown = Select(element)
            dropdown.select_by_visible_text("EU 34")
            time.sleep(2)
        with allure.step("Click on 'Update' button"):
            self.click(self.__UPDATE)
            time.sleep(2)

    def modify_item_qty_in_basket(self):
        with allure.step("Add product to the bag"):
            self.add_to_basket()
            time.sleep(1)
        with allure.step("Click on the person (account) dropdown and click 'view bag'"):
            self.click(self.__VIEW_BAG)
            time.sleep(2)
        with allure.step("Modify the quantity of the product"):
            self.click(self.__SIZE_QTY_MYBAG)
            time.sleep(2)
            element = self.driver.find_element(By.CSS_SELECTOR, ".bag-item-quantity.bag-item-selector.select2-hidden-accessible")
            dropdown = Select(element)
            dropdown.select_by_visible_text("3")
            time.sleep(2)
        with allure.step("Click on 'Update' button"):
            self.click(self.__UPDATE)
            time.sleep(2)

    def save_item_for_later_from_bag(self):
        with allure.step("Add product to the bag"):
            self.add_to_basket()
            time.sleep(1)
        with allure.step("Click on the person (account) dropdown and click 'view bag'"):
            self.click(self.__VIEW_BAG)
            time.sleep(2)
        with allure.step("Click on 'save for later' button"):
            self.click(self.__SAVE_FOR_LATER)
            time.sleep(2)

    def checkout(self):
        with allure.step("Add product to the bag and select the size"):
            self.select_size()
            self.click(self.__ADD_TO_BAG)
            time.sleep(3)
        with allure.step("Click on 'Checkout' button on the bag pop up"):
            self.click(self.__CHECKOUT)
            time.sleep(2)

    def sort_by_gender(self):
        with allure.step("Search and choose a product"):
            hw = HomepageWizard(self.driver)
            hw.search_and_choose("jeans")
        with allure.step("Sort by Gender, Men"):
            self.sort_func_prod_page("Gender", "Men")
            time.sleep(2)

    def sort_by_product_type(self):
        with allure.step("Search and choose a product"):
            hw = HomepageWizard(self.driver)
            hw.search_and_choose("jeans")
        with allure.step("Sort by Product Type, Jackets"):
            self.sort_func_prod_page("Product Type", "Jackets")
            time.sleep(2)

    def sort_by_discount(self):
        with allure.step("Search and choose a product"):
            hw = HomepageWizard(self.driver)
            hw.search_and_choose("jeans")
        with allure.step("Sort by Discount, 40% - 50%"):
            self.sort_func_prod_page("Discount %", "40% - 50%")
            time.sleep(2)

    def sort_by_price_range(self):
        with allure.step("Search and choose a product"):
            hw = HomepageWizard(self.driver)
            hw.search_and_choose("jeans")
        with allure.step("Sort by Price Range"):
            sort_list = self.driver.find_elements(By.CSS_SELECTOR, ".button_eZ0Gy")
            for sort in sort_list:
                if "Price Range" in sort.text:
                    sort.click()
                    min_slider = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="minIndicator"]')
                    max_slider = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="maxIndicator"]')
                    actions = ActionChains(self.driver)
                    actions.click_and_hold(min_slider).move_by_offset(50, 0).release().perform()
                    time.sleep(1)
                    actions.click_and_hold(max_slider).move_by_offset(-80, 0).release().perform()
                    time.sleep(1)
            time.sleep(2)

    def change_country(self):
        with allure.step("Click on Country button"):
            self.click(self.__CHANGE_COUNTRY_BTN)
            time.sleep(1)
        with allure.step("Choose a country: "):
            self.click(self.__CHOOSE_COUNTRY)
            time.sleep(1)
            element = self.driver.find_element(By.CSS_SELECTOR,"#country")
            dropdown = Select(element)
            dropdown.select_by_visible_text("Argentina")
            time.sleep(1)
        with allure.step("Click on 'Update Preferences' button"):
            self.click(self.__UPDATE_PREFERENCES_BTN)
            time.sleep(2)

    def change_currency(self):
        with allure.step("Click on Country button"):
            self.click(self.__CHANGE_COUNTRY_BTN)
            time.sleep(1)
        with allure.step("Choose a currency: "):
            self.click(self.__CHOOSE_CURRENCY)
            time.sleep(1)
            element = self.driver.find_element(By.CSS_SELECTOR, "#currency")
            dropdown = Select(element)
            dropdown.select_by_visible_text("$ USD")
            time.sleep(2)
        with allure.step("Click on 'Update Preferences' button"):
            self.click(self.__UPDATE_PREFERENCES_BTN)
            time.sleep(2)

    def facebook_link(self):
        with allure.step("Click on facebook link"):
            element = self.driver.find_element(By.CSS_SELECTOR, ".st34raq.J8Sftp9")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(1)
            element.click()
            time.sleep(2)

    def instagram_link(self):
        with allure.step("Click on instagram link"):
            element = self.driver.find_element(By.CSS_SELECTOR, ".st34raq.mbXMayF")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(1)
            element.click()
            time.sleep(2)

    def prev_next_picture(self):
        with allure.step("Search and choose a product"):
            hw = HomepageWizard(self.driver)
            hw.search_and_choose("jeans")
        with allure.step("Click on the product"):
            self.click(self.__PROD_ID)
        with allure.step("Click on the left arrow 3 times to view the product images"):
            for i in range(3):
                self.click(self.__LEFT_PICTURE)
                time.sleep(0.5)
        with allure.step("Click on the right arrow 3 times to view the product images"):
            for i in range(3):
                self.click(self.__RIGHT_PICTURE)
                time.sleep(0.5)
            time.sleep(2)
