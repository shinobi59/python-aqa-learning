
payload = {
    "id": "2",
    "name": "Maks",
    "username": "shinobimxx",
    "email": "shinobimxx@mail.ru",
}

def test_create_user(users_api):

    user = users_api.create_user(payload)
    assert user.status_code == 201
    assert "id" in user.json()

def test_update_user(users_api):
    updated_user = users_api.update_user(payload)
    assert updated_user.status_code == 200
    assert updated_user.json["id"] == 1