import requests

class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self, email, password):
        headers = {'email': email, 'password': password}
        response = requests.post(f"{self.base_url}api/key", headers=headers)
        return response.json()
