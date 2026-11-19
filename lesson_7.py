import requests

def validate_user_api():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url, timeout=10)
    assert response.status_code == 200, "Ожидался 200"
    response_json = response.json()

    assert response_json["id"] == 1, "Id неверный"
    assert response_json["username"] == "Bret", "Некорректное имя"
    assert "email" in response_json
    return True

print(validate_user_api())

def novalidate_user_api():
    url = "https://jsonplaceholder.typicode.com/users/99999"
    response = requests.get(url, timeout=10)
    assert response.status_code == 404, "Ожидался 404"
    return True

print(novalidate_user_api())