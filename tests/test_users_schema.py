from jsonschema import validate
from schemas.users_schema import user_schema
from schemas.users_schema import users_schema
from schemas.users_schema import created_user_schema

payload = {
    "name": "Maks",
    "username": "test",
    "email": "test@mail.ru",
}

def test_get_user_schema(users_api):
    response = users_api.get_user(1)
    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    validate(instance=data, schema=user_schema)

def test_get_users_schema(users_api):
    response = users_api.get_users()
    assert response.status_code == 200

    data = response.json()

    assert len(data) == 10
    validate(instance=data, schema=users_schema)

def test_created_user_schema(users_api):
    response = users_api.create_user(payload)
    assert response.status_code == 201

    data = response.json()

    validate(instance=data, schema=created_user_schema)