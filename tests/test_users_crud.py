
payload = {
    "name": "Maks",
    "username": "shinobimxx",
    "email": "shinobimxx@mail.ru",
}

def test_create_user(users_api):

    user = users_api.create_user(payload)
    assert user.status_code == 201
    data = user.json()
    assert "id" in data
    assert data["name"] == payload["name"]
    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]

def test_update_user(users_api):
    updated_user = users_api.update_user(1, payload)
    assert updated_user.status_code == 200
    assert updated_user.json()["id"] == 1
    assert updated_user.json()["name"] == payload["name"]
    assert updated_user.json()["username"] == payload["username"]
    assert updated_user.json()["email"] == payload["email"]

def test_patch_user(users_api):
    updated_user = users_api.patch_user(2, payload={"name": "Max"})
    assert updated_user.status_code == 200
    assert updated_user.json()["name"] == "Max"
    assert updated_user.json()["id"] == 2

def test_delete_user(users_api):
    deleted_user = users_api.delete_user(3)
    assert deleted_user.status_code == 200
    assert deleted_user.json() == {}