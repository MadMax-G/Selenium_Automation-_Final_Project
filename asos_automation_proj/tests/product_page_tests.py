import time
import allure
import pytest
from allure_commons.types import Severity
from asos_automation_proj.tests.base_test import BaseTest

@allure.epic("ProductPage")
@allure.severity(Severity.CRITICAL)
class TestProductPage(BaseTest):

    @allure.feature("Product Browsing")
    @allure.story("As a user, I want to view individual products from search results")
    @allure.title("Select a product from the search results")
    @allure.description("After searching for 'jeans', this test selects a product to view its details")
    def test_01_prod_page_01(self):
        self.product_page.select_prod()

    @allure.feature("Product Selection")
    @allure.story("As a user, I want to select a size before purchasing an item")
    @allure.title("Select size for a chosen product")
    @allure.description("This test selects a size for the previously selected jeans product")
    def test_01_prod_page_02(self):
        self.product_page.select_size()

    @allure.feature("Shopping Cart")
    @allure.story("As a user, I want to add selected products to my shopping bag")
    @allure.title("Add a product to the shopping bag")
    @allure.description("This test adds the selected jeans product with chosen size to the bag")
    def test_01_prod_page_03(self):
        self.product_page.add_to_basket()

    @allure.feature("Shopping Cart")
    @allure.story("As a user, I want to remove items from my shopping bag")
    @allure.title("Remove a product from the shopping bag")
    @allure.description("This test opens the shopping bag and removes the added item")
    def test_01_prod_page_04(self):
        self.product_page.remove_from_basket()

    @allure.feature("Shopping Cart")
    @allure.story("As a user, I want to modify the size of an item in the shopping bag")
    @allure.title("Change product size in the shopping bag")
    @allure.description("This test adds an item with size 'S', then changes it to size 'M' from the bag")
    @allure.severity(Severity.NORMAL)
    def test_01_prod_page_05(self):
        self.product_page.modify_item_size_in_basket()

    @allure.feature("Shopping Cart")
    @allure.story("As a user, I want to change the quantity of an item in the shopping bag")
    @allure.title("Change product quantity in the shopping bag")
    @allure.description("This test adds one pair of jeans to the bag, then updates the quantity to 3")
    @allure.severity(Severity.NORMAL)
    def test_01_prod_page_06(self):
        self.product_page.modify_item_qty_in_basket()

    @allure.feature("Shopping Cart")
    @allure.story("As a user, I want to move items from my bag to my saved items")
    @allure.title("Save item for later from shopping bag")
    @allure.description("This test adds a product to the bag, then moves it to 'Saved for later'")
    @allure.severity(Severity.NORMAL)
    def test_01_prod_page_07(self):
        self.product_page.save_item_for_later_from_bag()

    @allure.feature("Checkout")
    @allure.story("As a user, I want to proceed to checkout after adding items to the bag")
    @allure.title("Go to checkout after adding an item to the bag")
    @allure.description("This test adds an item to the bag and proceeds to the checkout screen")
    def test_01_prod_page_08(self):
        self.product_page.checkout()