import requests

class PetStoreAPI:
    BASE_URL = "https://petstore.swagger.io/v2"

    def get_pet_by_id(self, pet_id):
        """GET запрос для получения информации о питомце по его ID"""
        url = f"{self.BASE_URL}/pet/{pet_id}"
        response = requests.get(url)
        print(f"GET {url} - Status Code: {response.status_code}")
        print("Response:", response.json())
        return response

    def add_pet(self, pet_data):
        """POST запрос для добавления нового питомца"""
        url = f"{self.BASE_URL}/pet"
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=pet_data, headers=headers)
        print(f"POST {url} - Status Code: {response.status_code}")
        print("Response:", response.json())
        return response

    def update_pet(self, pet_data):
        """PUT запрос для обновления информации о питомце"""
        url = f"{self.BASE_URL}/pet"
        headers = {"Content-Type": "application/json"}
        response = requests.put(url, json=pet_data, headers=headers)
        print(f"PUT {url} - Status Code: {response.status_code}")
        print("Response:", response.json())
        return response

    def delete_pet(self, pet_id):
        """DELETE запрос для удаления питомца по его ID"""
        url = f"{self.BASE_URL}/pet/{pet_id}"
        response = requests.delete(url)
        print(f"DELETE {url} - Status Code: {response.status_code}")
        print("Response:", response.json())
        return response