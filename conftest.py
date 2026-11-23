import pytest
import requests
from api.users_api import UsersAPI


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

@pytest.fixture
def users_api(base_url, api_session):
    return UsersAPI(base_url, api_session)