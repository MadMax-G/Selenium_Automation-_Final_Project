import time
import allure
import pytest
from allure_commons.types import Severity
from asos_automation_proj.tests.base_test import BaseTest

@allure.epic("Security")
@allure.feature("login")
class TestLogin(BaseTest):

    @allure.title("login via email")
    @allure.description("providing valid email, and clicking continue at the login page")
    @allure.severity(Severity.CRITICAL)
    @allure.story("As a user I want to login after entering a valid credentials")
    def test_01_login_page(self):
        self.login_page.fill_email("madorskimaxim@gmail.com")
        time.sleep(1)

    @allure.title("login via email and password")
    @allure.description("login via valid email, and valid password")
    @allure.severity(Severity.CRITICAL)
    @allure.story("As a user I want to login after entering a valid credentials")
    def test_02_login_page(self):
        self.login_page.fill_email("madorskimaxim@gmail.com")
        time.sleep(20)
        self.login_page.fill_password("Maxmark2001!")
        time.sleep(1)

    @allure.title("login via invalid email")
    @allure.description("providing invalid email, and clicking continue at the login page")
    @allure.severity(Severity.NORMAL)
    @allure.story("As a user I want to get error messages after entering invalid credentials")
    def test_03_login_page(self):
        self.login_page.fill_invalid_email("er5gwgwrevw4@rtgt")
        time.sleep(1)

