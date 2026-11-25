import pytest

@pytest.mark.parametrize(
    "user_id, expected_status",
    [
        (1, 200),
        (2, 200),
        (3, 200),
        (4, 200),
        (5, 200),
        (6, 200),
        (7, 200),
        (8, 200),
        (9, 200),
        (10, 200),
    ],
)
def test_valid_users(users_api, user_id, expected_status):
    response = users_api.get_user(user_id)
    assert response.status_code == expected_status
    data = response.json()
    assert data["id"] == user_id

@pytest.mark.parametrize(
    "user_id, expected_status",
    [
        (999, 404),
        (9999, 404),
        (99999, 404),
        (100000, 404),
    ],
)
def test_invalid_users(users_api, user_id, expected_status):
    response = users_api.get_user(user_id)
    assert response.status_code == expected_status

@pytest.mark.parametrize(
    "user_id, expected_status",
    [
        (1,200),
        (5, 200),
        (10, 200),
        (999, 404),
        (99999, 404),
    ],
    ids=["valid_1", "valid_5", "valid_10", "invalid_999", "invalid_99999"],
)
def test_user_status(users_api, user_id, expected_status):
    response = users_api.get_user(user_id)
    assert response.status_code == expected_status