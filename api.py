# api.py

class PetFriends:
    def test__init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self, email, password):

        headers = {
            'email': email,
            'password': password
        }
        response = requests.post(f"{self.base_url}api/key", headers=headers)
        return response.json()

import requests
BASE_URL = "https://petfriends.skillfactory.ru/"


EMAIL = "dezenmaa@yandex.ru"
PASSWORD = "Zamira1906"


def get_api_key(email, password):
    headers = {
        'email': email,
        'password': password
    }
    response = requests.post(f"{BASE_URL}api/key", headers=headers)
    print("POST /api/key:")
    print("Status code:", response.status_code)
    print("Response:", response.json())
    return response.json().get('key')

def get_list_of_pets(auth_key, filter = ""):
    headers = {'auth_key': auth_key}
    params = {'filter': filter}
    response = requests.get(f"{BASE_URL}api/pets", headers=headers, params=params)
    print("\nGET /api/pets:")
    print("Status code:", response.status_code)
    print("Response:", response.json())
    return response.json()

def add_new_pet(auth_key, name, animal_type, age):
    headers = {'auth_key': auth_key}
    data = {
        'name': name,
        'animal_type': animal_type,
        'age': age
    }
    response = requests.post(f"{BASE_URL}api/create_pet_simple", headers=headers, data=data)
    print("\nPOST /api/create_pet_simple:")
    print("Status code:", response.status_code)
    print("Response:", response.json())
    return response.json()

def update_pet_info(auth_key, pet_id, name, animal_type, age):
    headers = {'auth_key': auth_key}
    data = {
        'name': name,
        'animal_type': animal_type,
        'age': age
    }
    response = requests.put(f"{BASE_URL}api/pets/{pet_id}", headers=headers, data=data)
    print("\nPUT /api/pets/{pet_id}:")
    print("Status code:", response.status_code)
    print("Response:", response.json())
    return response.json()

def delete_pet(auth_key, pet_id):
    headers = {'auth_key': auth_key}
    response = requests.delete(f"{BASE_URL}api/pets/{pet_id}", headers=headers)
    print("\nDELETE /api/pets/{pet_id}:")
    print("Status code:", response.status_code)
    print("Response:", response.text)
    return response.status_code
