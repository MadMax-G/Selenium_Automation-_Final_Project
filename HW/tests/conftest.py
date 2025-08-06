import pytest
from selenium import webdriver

from HW.pages.wizard1 import Wizard1
from HW.pages.wizard2 import Wizard2
from HW.pages.wizard3 import Wizard3
from HW.pages.wizard4 import Wizard4
from HW.pages.wizard5 import Wizard5
from HW.pages.wizard6 import Wizard6


@pytest.fixture(scope="class")
def setup(request):
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.maximize_window()
    request.cls.driver.get("https://www.saucedemo.com/")
    request.cls.wizard1_page = Wizard1(request.cls.driver)
    request.cls.wizard2_page = Wizard2(request.cls.driver)
    request.cls.wizard3_page = Wizard3(request.cls.driver)
    request.cls.wizard4_page = Wizard4(request.cls.driver)
    request.cls.wizard5_page = Wizard5(request.cls.driver)
    request.cls.wizard6_page = Wizard6(request.cls.driver)
    yield
    request.cls.driver.quit()


@pytest.fixture(scope="function")
def setup_2(request):
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.maximize_window()
    request.cls.driver.get("https://www.saucedemo.com/")
    request.cls.wizard1_page = Wizard1(request.cls.driver)
    request.cls.wizard2_page = Wizard2(request.cls.driver)
    request.cls.wizard3_page = Wizard3(request.cls.driver)
    request.cls.wizard4_page = Wizard4(request.cls.driver)
    request.cls.wizard5_page = Wizard5(request.cls.driver)
    request.cls.wizard6_page = Wizard6(request.cls.driver)
    yield
    request.cls.driver.quit()