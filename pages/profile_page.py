from playwright.sync_api import expect

from config import PetDetails
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, page,timeout = 5000):
        super().__init__(page, timeout)
        self.page = page
        self.ADD_PET_BUTTON = self.page.locator ('//*[@id="app"]/main/div/div/div[1]/div/div[1]/button')
        self.NAME_FIELD = self.page.locator('//*[@id="name"]')
        self.PET_SELECTION_BUTTON = self.page.locator('//*[@id="typeSelector"]')
        self.CHOOSING_A_PET_TYPE = self.page.get_by_text(PetDetails.PET_VIEW)
        self.ENTERING_THE_PETS_AGE = self.page.locator('//*[@id="age"]/input')
        self.GENDER_SELECTION_BUTTON= self.page.locator('//*[@id="genderSelector"]')
        self.CHOOSING_YOUR_PETS_GENDER = self.page.get_by_text(PetDetails.PET_GENDER, exact=True)
        self.SUBMIT_BUTTON = self.page.get_by_text('Submit')
        self.ADD_PHOTO_BUTTON = self.page.locator('//*[@id="app"]/main/div/div/div[2]/div[2]/div/span')
        self.PROFILE_BUTTON = self.page.locator('//*[@id="app"]/header/div/ul/li[1]/a')
        # self.SECTION_WITH_PETS = self.page.locator('//*[@id="app"]/main/div/div/div[2]/div/div/div/div[1]/div[1]')
    def click_add_pet_button (self):
        self.ADD_PET_BUTTON.click(timeout=self.timeout)
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
    def click_submit_button(self):
        self.SUBMIT_BUTTON.click()
    def check_registration_page(self):
        expect(self.ADD_PHOTO_BUTTON).to_have_text('Choose')
    def click_profile_button(self):
        self.PROFILE_BUTTON.click()
    def check_profile_page(self):
        expect(self.page).to_have_url('http://34.141.58.52:8080/#/profile')
    def checking_the_created_pet(self,name):
        # expect(self.SECTION_WITH_PETS).to_have_text(name)
        expect(self.page.get_by_text(name)).to_be_visible()





