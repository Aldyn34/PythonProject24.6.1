from api.petstore_api import PetStoreAPI

def main():
    api = PetStoreAPI()

    # 1. Добавление нового питомца (POST)
    new_pet = {
        "id": 12345,
        "category": {"id": 1, "name": "Dogs"},
        "name": "Buddy",
        "photoUrls": ["https://example.com/photo.jpg"],
        "tags": [{"id": 1, "name": "friendly"}],
        "status": "available"
    }
    print("Adding new pet:")
    api.add_pet(new_pet)

    # 2. Получение информации о питомце (GET)
    print("\nGetting pet by ID:")
    api.get_pet_by_id(12345)

    # 3. Обновление информации о питомце (PUT)
    updated_pet = {
        "id": 12345,
        "category": {"id": 1, "name": "Dogs"},
        "name": "Buddy Updated",
        "photoUrls": ["https://example.com/photo.jpg"],
        "tags": [{"id": 1, "name": "friendly"}],
        "status": "sold"
    }
    print("\nUpdating pet:")
    api.update_pet(updated_pet)

    # 4. Удаление питомца (DELETE)
    print("\nDeleting pet:")
    api.delete_pet(12345)

if __name__ == "__main__":
    main()