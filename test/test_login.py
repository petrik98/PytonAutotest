from config import LoginPageConfig
from pages.login_page import LoginPage


class TestLogin:
    def test_login(self, page):
        login_page = LoginPage(page)
        login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
        login_page.click_register_button()
        login_page.fill_login_field(LoginPageConfig.EMAIL_MAIN)
        login_page.fill_password_field(LoginPageConfig.PASSWORD_MAIN)
        login_page.fill_confirm_password(LoginPageConfig.PASSWORD_MAIN)
        login_page.click_submit_button()
        login_page.check_profile_page()
