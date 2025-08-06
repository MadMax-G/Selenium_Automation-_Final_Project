import time
import allure
import pytest
from allure_commons.types import Severity

from HW.tests.base_test import BaseTest

@pytest.mark.usefixtures("setup")
class TestWizardAll(BaseTest):

    @allure.severity(Severity.CRITICAL)
    @allure.title("Login")
    @allure.description("logging in to the website")
    def test_01_page_01(self):
        with allure.step("Login page steps"):
            self.wizard1_page.fill_info("standard_user", "secret_sauce")
        time.sleep(0.5)

    @allure.severity(Severity.NORMAL)
    @allure.title("Add to cart")
    @allure.description("Clicking on add to cart of chosen item")
    def test_02_page_02(self):
        with allure.step("Choosing first item"):
            self.wizard2_page.choose_item("#item_4_title_link")
        time.sleep(0.5)

    def test_03_page_03(self):
        self.wizard3_page.add_to_cart()
        self.wizard3_page.back()
        time.sleep(0.5)

    def test_04_page_02(self):
        self.wizard2_page.choose_item("#item_0_title_link")
        time.sleep(0.5)

    def test_05_page_03(self):
        self.wizard3_page.add_to_cart()
        time.sleep(0.5)
        self.wizard3_page.back()
        time.sleep(0.5)

    def test_06_page_02(self):
        self.wizard2_page.to_cart()
        time.sleep(0.5)

    def test_07_page_04(self):
        self.wizard4_page.checkout()
        time.sleep(0.5)

    def test_08_page_05(self):
        self.wizard5_page.fill_info("max", "madorski", "490")
        time.sleep(0.5)
        self.wizard5_page.continue_btn()
        time.sleep(0.5)

    def test_09_page_06(self):
        self.wizard6_page.finish_btn()
