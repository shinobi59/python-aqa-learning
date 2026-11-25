from jsonschema import validate
from schemas.users_schema import users_schema

def test_get_user_schema(users_api):
    response = users_api.get_users()
    assert response.status_code == 200
    validate(instance=response, schema=users_schema)