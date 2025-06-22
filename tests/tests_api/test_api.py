import pytest

from api import PetsApi
from config import LoginPageConfig


class TestApi:
    def test_login(self):
        res = PetsApi().login(LoginPageConfig.EMAIL,LoginPageConfig.PASSWORD)
        status_code = res[1]
        assert status_code == 200

    @pytest.mark.parametrize("name,pet_type,age,gender", [('Ya', 'donkey', 12, 'male')])
    def test_post_pet(self,name: str, pet_type: str, age: int, gender: str):
        res = PetsApi().post_pet(name,pet_type,age,gender)
        status_code = res[1]
        assert status_code == 200
        assert type(res[0]['id']) is int

    @pytest.mark.parametrize("pet_id", [35682])
    def test_get_pet(self, pet_id: int):
        res = PetsApi().get_pet(pet_id)
        status_code = res[1]
        assert status_code == 200

    @pytest.mark.parametrize("pet_id", [3568])
    def test_deleted_pet(self,pet_id):
        res =PetsApi().delite_pet(pet_id)
        status_code = res[1]
        assert status_code == 200

    @pytest.mark.parametrize("name,pet_type,age,gender,pet_id", [('Ya', 'donkey', 12, 'male',35683)])
    def test_patch_pet(self,name: str, pet_type: str, age: int, gender: str, pet_id: int):
        res = PetsApi().patch_pet(name,pet_type,age,gender,pet_id)
        status_code = res[1]
        assert status_code == 200
        assert type(res[0]['id']) is int

    @pytest.mark.parametrize("pet_id", [35685])
    def test_put_like_pet(self, pet_id):
        res = PetsApi().put_like_pet(pet_id)
        status_code = res[1]
        assert status_code == 200

class TestApiNegative:
    @pytest.mark.parametrize("password", ['','123','qwer'])
    def test_login_incorrect_password(self, password):
        res = PetsApi().login(LoginPageConfig.EMAIL, password)
        status_code = res[1]
        assert status_code == 400
        assert res[0]['detail'] == 'Username is taken or pass issue'

    @pytest.mark.parametrize("email", ['123', 'qwer'])
    def test_login_incorrect_email(self, email: str):
        res = PetsApi().login(email, LoginPageConfig.PASSWORD)
        status_code = res[1]
        assert status_code == 400
        assert res[0]['detail'] == 'Username is taken or pass issue'

    @pytest.mark.parametrize("pet_id", [35683])
    def test_put_like_pet_negative(self, pet_id):
        res = PetsApi().put_like_pet(pet_id)
        status_code = res[1]
        assert status_code == 403
        assert res[0]['detail'] == 'You already liked it'

    @pytest.mark.parametrize("name,pet_type,age,gender,invalid_pet_id", [('Ya', 'donkey', 12, 'male', 5)])
    def test_patch_pet_invalid_id(self, name: str, pet_type: str, age: int, gender: str, invalid_pet_id: int):
        res = PetsApi().patch_pet(name, pet_type, age, gender, invalid_pet_id)
        status_code = res[1]
        assert status_code == 403
        assert res[0]['detail'] == 'You are not allowed to change this pet'

    @pytest.mark.parametrize("invalid_pet_id", [-1,0])
    def test_get_pet_invalid_id (self, invalid_pet_id: int):
        res = PetsApi().get_pet(invalid_pet_id)
        status_code = res[1]
        assert status_code == 404
        assert res[0]['detail'] == 'Pet not found'
