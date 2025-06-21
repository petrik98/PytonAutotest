from playwright.sync_api import expect

from config import PetDetails
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, page,timeout = 5000):
        super().__init__(page, timeout)
        self.page = page
        self.EDIT_PET_BUTTON = self.page.locator ('//*[@id="app"]/main/div/div/div[2]/div/div[1]/div/div[2]/button[1]')
        self.NAME_FIELD = self.page.locator('//*[@id="name"]')
        self.PET_SELECTION_BUTTON = self.page.locator('//*[@id="typeSelector"]')
        self.CHOOSING_A_PET_TYPE = self.page.get_by_text(PetDetails.PET_VIEW).first
        self.ENTERING_THE_PETS_AGE = self.page.locator('//*[@id="age"]/input')
        self.GENDER_SELECTION_BUTTON= self.page.locator('//*[@id="genderSelector"]')
        self.CHOOSING_YOUR_PETS_GENDER = self.page.get_by_text(PetDetails.PET_GENDER, exact=True).first
        self.SAVE_BUTTON = self.page.locator('//*[@id="app"]/main/div/form/div/div[2]/div[3]/button')
        # get_by_text('Save')
        self.PROFILE_BUTTON = self.page.locator('//*[@id="app"]/header/div/ul/li[1]/a')
        self.PET_NAME_FIELD = self.page.get_by_text('This field is email')
        self.SOMETHING_WENT_WRONG = self.page.get_by_text('Something went wrong').first
        # self.SECTION_WITH_PETS = self.page.locator('//*[@id="app"]/main/div/div/div[2]/div/div/div/div[1]/div[1]')
    def click_edit_pet_button (self):
        self.EDIT_PET_BUTTON.click(timeout=self.timeout)
    def fill_name_field(self, name):
        self.NAME_FIELD.fill(name,timeout=self.timeout)
    def click_pet_selection_button(self):
        self.PET_SELECTION_BUTTON.click()
    def click_choosing_a_pet_type(self):
        self.CHOOSING_A_PET_TYPE.click()
    def fill_entering_the_pets_age(self,age):
        self.ENTERING_THE_PETS_AGE.fill(age)
    def click_gender_selection_button(self):
        self.GENDER_SELECTION_BUTTON.click()
    def click_choosing_your_pets_gender (self):
        self.CHOOSING_YOUR_PETS_GENDER.click()
    def click_save_button(self):
        self.SAVE_BUTTON.click()
    def check_registration_page(self):
        expect(self.page).to_have_url('http://34.141.58.52:8080/#/profile?message=Your+pet+has+been+successfully+saved')
    def click_profile_button(self):
        self.PROFILE_BUTTON.click()
    def check_profile_page(self):
        expect(self.page).to_have_url('http://34.141.58.52:8080/#/profile')
    def checking_edited_pet(self,name):
        expect(self.page.get_by_text(name)).to_be_visible()
    def name_error_check(self):
        expect(self.PET_NAME_FIELD).to_be_visible()
    def unsatisfactory_age_verification(self):
        expect(self.SOMETHING_WENT_WRONG).to_be_visible()
        self.PROFILE_BUTTON.click()