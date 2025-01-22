import sys
sys.path.append("../")  # Добавляем путь к корневой директории проекта
from petfriends_api import PetFriends

def test_get_all_pets_with_valid_key():
    petfriends = PetFriends()
    result = petfriends.get_api_key(email="Dezenmaa@yandex.ru", password="Zamira1906")
    assert 'key' in result