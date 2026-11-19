import pytest
import requests


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="module")
def api_session():
    print("Создание сессии")
    session = requests.Session()

    yield session

    print("Закрытие сессии")
    session.close()