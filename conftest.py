import pytest
import requests


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def api_session():
    session = requests.Session()
    yield session
    session.close()