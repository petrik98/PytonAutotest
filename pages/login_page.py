from playwright.sync_api import expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page,timeout = 5000):
        super().__init__(page, timeout)
        self.page = page
        # self.REGISTER_BUTTON = self.page.locator('//*[@id="app"]/header/div/ul/li[2]/a')
        self.REGISTER_BUTTON = self.page.get_by_text('Register')
        self.LOGIN_FIELD = self.page.locator('//*[@id="login"]')
        self.PASSWORD_FIELD = self.page.locator('//*[@id="password"]/input')
        self.CONFIRM_PASSWORD = self.page.locator('//*[@id="confirm_password"]/input')
        self.SUBMIT_BUTTON = self.page.get_by_text('Submit')
        self.FIELD_IS_EMAIL_MASSAGE = self.page.get_by_text('This field is email')
        self.FIELD_IS_REQUIRED_PASSWORD = self.page.get_by_text('This field is required')
        self.SOMETHING_WENT_WRONG = self.page.get_by_text('Something went wrong').first
        # self.SUBMIT_BUTTON = self.page.locator('//*[@id="pv_id_10_content"]/div/form/div[3]/button')
    def click_register_button (self):
        self.REGISTER_BUTTON.click(timeout=self.timeout)
    def fill_login_field(self,login):
        self.LOGIN_FIELD.fill(login, timeout=self.timeout)
    def fill_password_field(self,password):
        self.PASSWORD_FIELD.fill(password, timeout=self.timeout)
        self.LOGIN_FIELD.click(timeout=self.timeout)
    def fill_confirm_password (self,password):
        self.CONFIRM_PASSWORD.fill(password)
        self.LOGIN_FIELD.click(timeout=self.timeout)
    def click_submit_button(self):
        self.SUBMIT_BUTTON.click(timeout=self.timeout)
    def check_profile_page(self):
        expect(self.page).to_have_url('http://34.141.58.52:8080/#/profile',timeout=self.timeout)
    def chek_invalid_email(self):
        expect(self.FIELD_IS_EMAIL_MASSAGE).to_be_visible(timeout=self.timeout)
    def chek_empty_password(self):
        expect(self.FIELD_IS_REQUIRED_PASSWORD).to_be_visible(timeout=self.timeout)
    def chek_empty_password_(self):
        expect(self.SOMETHING_WENT_WRONG).to_be_visible()