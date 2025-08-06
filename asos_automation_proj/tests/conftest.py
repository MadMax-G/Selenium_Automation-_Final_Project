import os
import pytest
import undetected_chromedriver as uc
from asos_automation_proj.pages.login_page import LoginWizard
from asos_automation_proj.pages.home_page import HomepageWizard
from asos_automation_proj.pages.product_page import ProductPage

browser_name = None
browser_version = None

@pytest.fixture(scope="function", autouse=True)
def setup(request):
    global browser_name, browser_version
    request.cls.driver = uc.Chrome()
    request.cls.driver.maximize_window()
    request.cls.driver.get("https://www.asos.com/men/")
    request.cls.login_page = LoginWizard(request.cls.driver)
    request.cls.home_page = HomepageWizard(request.cls.driver)
    request.cls.product_page = ProductPage(request.cls.driver)
    browser_name = request.cls.driver.name
    browser_version = request.cls.driver.capabilities['browserVersion']
    yield
    request.cls.driver.quit()

def pytest_sessionfinish():
    global browser_name, browser_version
    if browser_name and browser_version:
        environment_properties = {
            'browser': browser_name,
            'driver_version': browser_version
        }
        allure_env_path = os.path.join("allure-results", 'environment.properties')
        os.makedirs("allure-results", exist_ok=True)
        with open(allure_env_path, 'w') as f:
            for key, value in environment_properties.items():
                f.write(f"{key}={value}\n")
