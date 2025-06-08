from config import PetDetails
from pages.profile_page import ProfilePage
a=PetDetails.PET_NAME

class TestAddPet:
    def test_add_pet(self, page, login):
        page = ProfilePage(page)
        page.click_add_pet_button()
        page.fill_name_field(a)
        page.click_pet_selection_button()
        page.click_choosing_a_pet_type()
        page.fill_entering_the_pets_age(PetDetails.PET_AGE)
        page.click_gender_selection_button()
        page.click_choosing_your_pets_gender()
        page.click_submit_button()
        page.check_registration_page()
        page.click_profile_button()
        page.check_profile_page()
        page.checking_the_created_pet(a)