import requests


def test_get_user():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "Bret"
    assert "email" in data

def test_user_not_found():
    url = "https://jsonplaceholder.typicode.com/users/99999"
    response = requests.get(url)

    assert response.status_code == 404

def test_get_users_list():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert data[0]["id"] == 1
    assert len(data) == 10