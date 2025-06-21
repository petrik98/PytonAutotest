import allure
import pytest

from config import PetDetails
# from generator import random_invalid_age, random_name
from pages.edit_ped_page import ProfilePage

a=PetDetails.PET_NAME
b=''

class TestEditPet:
    @pytest.mark.parametrize("name,age", [('edc',"5"),('cwec','4')])
    # @pytest.mark.parametrize("age", [random_age() for _ in range(2)])
    def test_edit_pet(self, login, name, age):
        page = ProfilePage(login)
        with allure.step('Click the edit pet button'):
            page.click_edit_pet_button()
        with allure.step('Change pet name'):
            page.fill_name_field(name)
        with allure.step('Click the button to select the pet type'):
            page.click_pet_selection_button()
        with allure.step('change pet type'):
            page.click_choosing_a_pet_type()
        with allure.step('change in pet\'s age'):
            page.fill_entering_the_pets_age(age)
        with allure.step('Click on the button to select the pet\'s gender'):
            page.click_gender_selection_button()
        with allure.step('pet gender change'):
            page.click_choosing_your_pets_gender()
        with allure.step('Click on the save changes button'):
            page.click_save_button()
        with allure.step('Checking the transition to the save page'):
            page.check_registration_page()
        with allure.step('Click the button to go to the profile page'):
            page.click_profile_button()
        with allure.step('Checking the transition to the profile page'):
            page.check_profile_page()
        with allure.step('Checking the pet list for a changed name'):
            page.checking_edited_pet(name)

class TestEditPetNegative:
    def test_edit_pet_negative (self, login):
        page = ProfilePage(login)
        with allure.step('Click the edit pet button'):
            page.click_edit_pet_button()
        with allure.step('Change pet name'):
            page.fill_name_field(b)
        with allure.step('Click on the save changes button'):
            page.click_save_button()
        with allure.step('Check for error when name field is empty'):
            page.name_error_check()

    # @pytest.mark.parametrize("name","age", [([random_invalid_age() for _ in range(1)],[random_name(4) for _ in range(1)])])
    @pytest.mark.parametrize("name,age", [('edc',"585858585858585885"),('cwec','458584884848484848')])
    # @pytest.mark.parametrize("name, age", [next(iter(data_generator())) for _ in range(2)])
    def test_edit_pet_negative_age(self,login, age,name):
        page = ProfilePage(login)
        with allure.step('Click the edit pet button'):
            page.click_edit_pet_button()
        with allure.step(f'Fill in the name field{name}'):
            page.fill_name_field(name)
        with allure.step(f'Filling the age field with inappropriate data{age}'):
            page.fill_entering_the_pets_age(age)
        with allure.step('Click on the button to create a pet'):
            page.click_save_button()
        with allure.step('Error checking when entering incorrect age'):
            page.unsatisfactory_age_verification()