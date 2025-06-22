import allure
import pytest

from config import LoginPageConfig
from generator import random_email, random_password, random_invalid_email
from pages.login_page import LoginPage


class TestLogin:
    @pytest.mark.parametrize("email", [random_email() for _ in range(3)])
    # @pytest.mark.parametrize("password", [random_password() for _ in range(3)])
    # @pytest.mark.parametrize("email,password",[([random_email()],[random_password()])], Inderct= True)
    def test_login(self, page,email):
        login_page = LoginPage(page)
        with allure.step('Open login page'):
            login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
        with allure.step('Click on the "registration" button to go to the registration page'):
            login_page.click_register_button()
        with allure.step(f'Enter a random email{email} in the login line'):
            login_page.fill_login_field(email)
        with allure.step(f'Enter a random password {LoginPageConfig.PASSWORD} in the password line'):
            login_page.fill_password_field(LoginPageConfig.PASSWORD)
        with allure.step('Repeat password'):
            login_page.fill_confirm_password(LoginPageConfig.PASSWORD)
        with allure.step('click the "Submit" button'):
            login_page.click_submit_button()
        with allure.step('We check the transition to the created profile page'):
            login_page.check_profile_page()

@pytest.mark.negative
class TestLoginNegative:

    @pytest.mark.dependency(name = 'test_login_invalid_email')
    @pytest.mark.parametrize("email",[random_invalid_email() for _ in range(3)])
    def test_login_invalid_email(self, page, email):
        login_page = LoginPage(page)
        with allure.step('Open login page'):
            login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
        with allure.step(f'Fill to email{email}'):
            login_page.fill_login_field(email)
        with allure.step(f'Fill to password{LoginPageConfig.PASSWORD_MAIN}'):
            login_page.fill_password_field(LoginPageConfig.PASSWORD_MAIN)
        with allure.step('click submit button'):
            login_page.click_submit_button()
        with allure.step('chek invalid email'):
            login_page.chek_invalid_email()

    @pytest.mark.dependency(dependenc=['test_login_invalid_email'])
    @pytest.mark.parametrize("email, password",[('fg',""),('876',"kjj"),("","")])
    # @pytest.mark.parametrize("password", ['','lkj','94'])
    def test_login_invalid_data(self, page, email, password):
        login_page = LoginPage(page)
        with allure.step('Open login page'):
            login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
        with allure.step(f'Fill to email{email}'):
            login_page.fill_login_field(email)
        with allure.step(f'Fill to password{password}'):
            login_page.fill_password_field(password)
        with allure.step('click submit button'):
            login_page.click_submit_button()
        with allure.step('chek invalid email'):
            login_page.chek_invalid_email()
        with allure.step('Checking the password line filling'):
            if len(password) == 0:
                login_page.chek_empty_password()

    @pytest.mark.parametrize("password",[random_password() for _ in range(3)])
    def test_login_invalid_password(self, page, password):
        login_page = LoginPage(page)
        with allure.step('Open login page'):
            login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
        with allure.step(f'Fill to email{LoginPageConfig.EMAIL}'):
            login_page.fill_login_field(LoginPageConfig.EMAIL)
        with allure.step(f'Fill to password{password}'):
            login_page.fill_password_field(password)
        with allure.step('click submit button'):
            login_page.click_submit_button()
        with allure.step('chek invalid password'):
            login_page.chek_empty_password_()