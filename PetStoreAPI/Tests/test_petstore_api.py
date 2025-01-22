import pytest
from api.petstore_api import PetStoreAPI

@pytest.fixture
def api():

    return PetStoreAPI()

def test_add_pet(api):

    new_pet = {
        "id": 12345,
        "category": {"id": 1, "name": "Dogs"},
        "name": "Buddy",
        "photoUrls": ["https://example.com/photo.jpg"],
        "tags": [{"id": 1, "name": "friendly"}],
        "status": "available"
    }
    response = api.add_pet(new_pet)
    assert response.status_code == 200
    assert response.json()["name"] == "Buddy"

def test_get_pet_by_id(api):

    response = api.get_pet_by_id(12345)
    assert response.status_code == 200
    assert response.json()["id"] == 12345

def test_update_pet(api):

    updated_pet = {
        "id": 12345,
        "category": {"id": 1, "name": "Dogs"},
        "name": "Buddy Updated",
        "photoUrls": ["https://example.com/photo.jpg"],
        "tags": [{"id": 1, "name": "friendly"}],
        "status": "sold"
    }
    response = api.update_pet(updated_pet)
    assert response.status_code == 200
    assert response.json()["name"] == "Buddy Updated"

def test_delete_pet(api):

    response = api.delete_pet(12345)
    assert response.status_code == 200