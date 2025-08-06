import allure
from allure_commons.types import Severity
from asos_automation_proj.tests.base_test import BaseTest

@allure.epic("Homepage")
@allure.feature("Navigation")
@allure.severity(Severity.CRITICAL)
class TestHomepage(BaseTest):

    @allure.story("As a user, I want to search for items using the search bar")
    @allure.title("Search for 'jeans' using the homepage search bar")
    @allure.description("This test inputs the text 'jeans' into the homepage search bar and verifies that relevant search results are shown.")
    def test_01_home_page_01(self):
        self.home_page.search("jeans")

    @allure.story("As a user, I want to browse women's products")
    @allure.title("Click on the 'Women' category from the homepage")
    @allure.description("This test clicks on the 'Women' category in the top navigation and verifies redirection to the women's section.")
    def test_01_home_page_02(self):
        self.home_page.women_category()

    @allure.story("As a user, I want to access my account details")
    @allure.title("Click on 'My Account' from the homepage")
    @allure.description("This test clicks on 'My Account' and verifies that the user is redirected to the account overview page.")
    def test_01_home_page_03(self):
        self.home_page.my_account()

    @allure.story("As a user, I want to view my past orders")
    @allure.title("Click on 'My Orders' from the account menu")
    @allure.description("This test clicks on 'My Orders' and verifies that the order history page is displayed.")
    def test_01_home_page_04(self):
        self.home_page.my_orders()

    @allure.story("As a user, I want to get information about returns")
    @allure.title("Click on 'Returns Info' from the help section")
    @allure.description("This test clicks on the 'Returns Info' link and verifies navigation to the returns information page.")
    def test_01_home_page_05(self):
        self.home_page.returns_info()

    @allure.story("As a user, I want to manage my contact preferences")
    @allure.title("Click on 'Contact Preferences' from the account settings")
    @allure.description("This test clicks on 'Contact Preferences' and verifies that the user can view or edit communication preferences.")
    def test_01_home_page_06(self):
        self.home_page.contact_preferences()

    @allure.story("As a user, I want to view my saved items")
    @allure.title("Click on 'Saved Items' from the top menu")
    @allure.description("This test clicks on 'Saved Items' and verifies that saved products are displayed.")
    def test_01_home_page_07(self):
        self.home_page.saved_items()

    @allure.story("As a user, I want to view items in my shopping bag")
    @allure.title("Click on 'Shopping Bag' icon")
    @allure.description("This test clicks on the shopping bag icon and verifies that the user is redirected to the cart page.")
    def test_01_home_page_08(self):
        self.home_page.shopping_bag()

    @allure.story("As a user, I want to sign into my account")
    @allure.title("Click on 'Sign In' from the homepage")
    @allure.description("This test clicks on the 'Sign In' button and verifies that the login page is displayed.")
    def test_01_home_page_09(self):
        self.home_page.sign_in()

    @allure.story("As a user, I want to search for items using the search bar")
    @allure.title("Click on search bar, type 'jeans', and click on the 'jeans' result")
    @allure.description("This test interacts with the search bar by typing 'jeans', then clicks on the suggested result, and verifies that relevant results are shown.")
    def test_01_home_page_10(self):
        self.home_page.search_and_choose("jeans")
