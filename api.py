import requests
import json
from config import LoginPageConfig


class PetsApi:
    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def login (self, email, password):
        data = {'email':email,'password':password}
        res = requests.post(self.base_url+'login', data=json.dumps(data))
        # token = res.json()['token']
        # id = res.json()['id']
        # status_code = res.status_code
        return res.json(), res.status_code
        # return token, id, status_code

    def post_pet (self,name: str, pet_type: str, age: int, gender: str) -> json:
        login_data = PetsApi().login(LoginPageConfig.EMAIL,LoginPageConfig.PASSWORD)
        # print(login_data[0]["token"])
        headers = {'Authorization':f'Bearer {login_data[0]["token"]}'}
        # headers = {'Authorization': f'Bearer{login_data[0]}'}
        data = {
            "id": 0,
            "name": name,
            "type": pet_type,
            "age": age,
            "gender": gender,
            "owner_id": login_data[0]['id']
        }
        res = requests.post(self.base_url+'pet', data = json.dumps(data), headers=headers)
        # print(res.json())
        return res.json(), res.status_code

    def get_pet(self, id: int) ->json:
        login_data = PetsApi().login(LoginPageConfig.EMAIL,LoginPageConfig.PASSWORD)
        # print(login_data[0]["token"])
        headers = {'Authorization': f'Bearer {login_data[0]["token"]}'}
        res = requests.get(self.base_url+f'pet/{id}', headers=headers)
        return res.json(), res.status_code

    def post_pet_image(self, pet_id: int) ->json:
        login_data = PetsApi().login(LoginPageConfig.EMAIL, LoginPageConfig.PASSWORD)
        headers = {'Authorization': f'Bearer {login_data[0]["token"]}'}
        files = {
            'pic':open('/Users/kseniasemenak/Desktop/PytonAutotest/tests/tests_api/pic.png','rb')
        }
        res = requests.post(self.base_url+f'pet/{pet_id}/image', headers=headers, files=files)
        return res.json(), res.status_code
    def delite_pet (self, pet_id: int) ->json:
        login_data = PetsApi().login(LoginPageConfig.EMAIL, LoginPageConfig.PASSWORD)
        headers = {'Authorization': f'Bearer {login_data[0]["token"]}'}
        res = requests.delete(self.base_url+f'pet/{pet_id}', headers=headers)
        return res.json(), res.status_code
    def patch_pet(self, name: str, pet_type: str, age: int, gender: str, pet_id: int) -> json:
        login_data = PetsApi().login(LoginPageConfig.EMAIL, LoginPageConfig.PASSWORD)
        headers = {'Authorization': f'Bearer {login_data[0]["token"]}'}
        data = {
            "id": pet_id,
            "name": name,
            "type": pet_type,
            "age": age,
            "gender": gender,
            "owner_id": login_data[0]['id']
        }
        res = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        return res.json(), res.status_code
    def put_like_pet(self, pet_id: int) -> json:
        login_data = PetsApi().login(LoginPageConfig.EMAIL, LoginPageConfig.PASSWORD)
        headers = {'Authorization': f'Bearer {login_data[0]["token"]}'}
        res = requests.put(self.base_url+f'pet/{pet_id}/like', headers=headers)
        return res.json(), res.status_code

# print(PetsApi().login(LoginPageConfig.EMAIL,''))
# print(PetsApi().post_pet('wewq','donkey',13,'your'))
# print(PetsApi().get_pet(35682))
# print(PetsApi().post_pet_image(35682))
# print(PetsApi().delite_pet(35681))
print(PetsApi().patch_pet('Dima','donkey',105,'non',35684))
# print(PetsApi().put_like_pet(35684))