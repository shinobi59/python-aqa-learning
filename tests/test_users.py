
def test_get_user(users_api):
    response = users_api.get_user(1)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1