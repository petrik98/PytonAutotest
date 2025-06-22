import allure
import pytest

from config import PetDetails
from generator import random_invalid_age, random_name, random_age
from pages.profile_page import ProfilePage

a=PetDetails.PET_NAME

class TestAddPet:
    # def test_add_pet(self, page, login):
    #     page = ProfilePage(page)
    #     page.click_add_pet_button()
    #     page.fill_name_field(a)
    #     page.click_pet_selection_button()
    #     page.click_choosing_a_pet_type()
    #     page.fill_entering_the_pets_age(PetDetails.PET_AGE)
    #     page.click_gender_selection_button()
    #     page.click_choosing_your_pets_gender()
    #     page.click_submit_button()
    #     page.check_registration_page()
    #     page.click_profile_button()
    #     page.check_profile_page()
    #     page.checking_the_created_pet(a)
    @pytest.mark.parametrize("name", [random_name(5) for _ in range(2)])
    @pytest.mark.parametrize("age", [random_age() for _ in range(2)])
    def test_add_pet(self, login, name, age):
        page = ProfilePage(login)
        with allure.step('Click the add pet button'):
            page.click_add_pet_button()
        with allure.step(f'Fill in the name field{name}'):
            page.fill_name_field(name)
        with allure.step('Click the button to select the pet type'):
            page.click_pet_selection_button()
        # with allure.step(f'Choose a random pet{PetDetails.PET_VIEW}'):
        #     page.click_choosing_a_pet_type()
        # with allure.step(f'Enter the pet\'s age{PetDetails.PET_AGE}'):
        #     page.fill_entering_the_pets_age(PetDetails.PET_AGE)
        with allure.step(f'Choose a random pet{PetDetails.PET_VIEW}'):
            page.click_choosing_a_pet_type()
        with allure.step(f'Enter the pet\'s age{age}'):
            page.fill_entering_the_pets_age(age)
        with allure.step('Click on the button to select the pet\'s gender'):
            page.click_gender_selection_button()
        with allure.step(f'Choosing the gender of your pet{PetDetails.PET_GENDER}'):
            page.click_choosing_your_pets_gender()
        with allure.step('Click on the button to create a pet'):
            page.click_submit_button()
        with allure.step('Checking the transition to the photo adding page'):
            page.check_registration_page()
        with allure.step('Go to the profile page'):
            page.click_profile_button()
        with allure.step('Check location on profile page'):
            page.check_profile_page()
        with allure.step('Control pet creation via pop-up window'): #page.checking_the_created_pet(a)
            page.pet_creation_control()

class TestAddPetNegative:
    def test_add_pet_negative_name(self, login):
        page = ProfilePage(login)
        with allure.step('Click the add pet button'):
            page.click_add_pet_button()
        with allure.step('Click the button to select the pet type'):
            page.click_pet_selection_button()
        with allure.step(f'Choose a random pet{PetDetails.PET_VIEW}'):
            page.click_choosing_a_pet_type()
        with allure.step('Click on the button to create a pet'):
            page.click_submit_button()
        with allure.step('Check for error when name field is empty'):
            page.name_error_check()

    @pytest.mark.parametrize("name", [random_name(4) for _ in range(2)])
    def test_add_pet_negative_pet_type (self, login, name):
        page = ProfilePage(login)
        with allure.step('Click the add pet button'):
            page.click_add_pet_button()
        with allure.step(f'Fill in the name field{name}'):
            page.fill_name_field(name)
        with allure.step('Click on the button to create a pet'):
            page.click_submit_button()
        with allure.step ('Pet Type Empty Field Error Check'):
            page.pet_type_selection_error_check()

    @pytest.mark.parametrize("age", [random_invalid_age()for _ in range(2)])
    def test_add_pet_negative_age (self, login, age):
        page = ProfilePage(login)
        with allure.step('Click the add pet button'):
            page.click_add_pet_button()
        with allure.step(f'Fill in the name field{a}'):
            page.fill_name_field(a)
        with allure.step('Click the button to select the pet type'):
            page.click_pet_selection_button()
        with allure.step(f'Choose a random pet{PetDetails.PET_VIEW}'):
            page.click_choosing_a_pet_type()
        with allure.step(f'Filling the age field with inappropriate data{age}'):
            page.fill_entering_the_pets_age(age)
        with allure.step('Click on the button to create a pet'):
            page.click_submit_button()
        with allure.step ('Error checking when entering incorrect age'):
            page.unsatisfactory_age_verification()