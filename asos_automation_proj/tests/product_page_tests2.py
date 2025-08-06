import allure
import pytest
from allure_commons.types import Severity
from asos_automation_proj.tests.base_test import BaseTest

@allure.epic("ProductPage")
@allure.severity(Severity.NORMAL)
class TestProductPage2(BaseTest):

    @allure.feature("Sorting")
    @allure.story("As a user, I want to sort items by gender")
    @allure.title("Sort jeans products by gender")
    @allure.description("This test selects 'jeans' and applies the gender filter")
    def test_02_prod_page_01(self):
        self.product_page.sort_by_gender()

    @allure.feature("Sorting")
    @allure.story("As a user, I want to sort items by product type")
    @allure.title("Sort jeans products by product type")
    @allure.description("This test selects 'jeans' and filters them by specific product types")
    def test_02_prod_page_02(self):
        self.product_page.sort_by_product_type()

    @allure.feature("Sorting")
    @allure.story("As a user, I want to sort items by discount")
    @allure.title("Sort jeans products by discount")
    @allure.description("This test selects 'jeans' and applies a discount sorting filter")
    def test_02_prod_page_03(self):
        self.product_page.sort_by_discount()

    @allure.feature("Sorting")
    @allure.story("As a user, I want to sort items by price range")
    @allure.title("Sort jeans products by price range")
    @allure.description("This test selects 'jeans' and applies a price range filter")
    def test_02_prod_page_04(self):
        self.product_page.sort_by_price_range()

    @allure.feature("Localization")
    @allure.story("As a user, I want to change my country preference")
    @allure.title("Change country setting")
    @allure.description("This test clicks the country icon and selects a different country")
    @allure.severity(Severity.CRITICAL)
    def test_02_prod_page_05(self):
        self.product_page.change_country()

    @allure.feature("Localization")
    @allure.story("As a user, I want to change my preferred currency")
    @allure.title("Change currency setting")
    @allure.description("This test clicks the country icon and selects a different currency")
    @allure.severity(Severity.CRITICAL)
    def test_02_prod_page_06(self):
        self.product_page.change_currency()

    @allure.feature("External Links")
    @allure.story("As a user, I want to open the brand's Facebook page")
    @allure.title("Click on Facebook link in the footer")
    @allure.description("This test clicks the Facebook icon and verifies that the Facebook page opens")
    def test_02_prod_page_07(self):
        self.product_page.facebook_link()

    @allure.feature("External Links")
    @allure.story("As a user, I want to open the brand's Instagram page")
    @allure.title("Click on Instagram link in the footer")
    @allure.description("This test clicks the Instagram icon and verifies that the Instagram page opens")
    def test_02_prod_page_08(self):
        self.product_page.instagram_link()

    @allure.feature("Product Browsing")
    @allure.story("As a user, I want to view all images of a product")
    @allure.title("Navigate through product images using next/previous buttons")
    @allure.description("This test opens a product detail page and clicks through its image gallery")
    def test_02_prod_page_09(self):
        self.product_page.prev_next_picture()


