import pytest
import requests


@pytest.mark.parametrize("user_id, expected_username", [
    (1, "Bret"),
    (2, "Antonette"),
    (3, "Samantha"),
    (4, "Karianne"),
    (5, "Kamren")
])
def test_existing_users(user_id, expected_username):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url, timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["username"] == expected_username


@pytest.mark.parametrize("user_id", [999, 1000, 99999])
def test_nonexistent_users(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url, timeout=10)
    assert response.status_code == 404