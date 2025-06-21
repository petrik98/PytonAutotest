import pytest
from pytest_playwright.pytest_playwright import browser

from config import LoginPageConfig
from generator import pair_generator, random_name, random_age
from pages.login_page import LoginPage

# @pytest.fixture
# def login(page):
#     login_page = LoginPage(page)
#     login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
#     login_page.fill_login_field(LoginPageConfig.EMAIL)
#     login_page.fill_password_field(LoginPageConfig.PASSWORD)
#     login_page.click_submit_button()
@pytest.fixture(scope='session')#autouse = True
def login(playwright, browser):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    login_page = LoginPage(page)
    login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
    login_page.fill_login_field(LoginPageConfig.EMAIL)
    login_page.fill_password_field(LoginPageConfig.PASSWORD)
    login_page.click_submit_button()
    return page
# @pytest.fixture(scope="module")
# def data_generator():
#     name = [random_name(3) for i in range(2)]
#     age = [random_age() for t in range(2)]
#     return pair_generator(name,age)
