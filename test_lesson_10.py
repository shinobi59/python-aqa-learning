
def test_get_user(base_url, api_session):
    url = f"{base_url}/users/1"
    response = api_session.get(url)

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1

def test_get_posts(base_url, api_session):
    url = f"{base_url}/posts"
    response = api_session.get(url)
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 100

def test_user_not_found(base_url, api_session):
    url = f"{base_url}/users/99999"
    response = api_session.get(url)
    assert response.status_code == 404