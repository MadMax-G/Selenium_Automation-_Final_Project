from asos_automation_proj.pages.login_page import LoginWizard
from asos_automation_proj.pages.home_page import HomepageWizard
from asos_automation_proj.pages.product_page import ProductPage


class BaseTest:

    login_page: LoginWizard
    home_page: HomepageWizard
    product_page: ProductPage

