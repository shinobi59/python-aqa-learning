
def test_get_user(users_api):
    response = users_api.get_user(1)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1

def test_get_users(users_api):
    response = users_api.get_users()
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 10

def test_get_posts(users_api):
    response = users_api.get_posts()
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 100

def test_user_not_found(users_api):
    response = users_api.get_user(99999)
    assert response.status_code == 404