import json

response_json = """
{
    "status": "success",
    "code": 200,
    "data": {
        "user_id": 15,
        "username": "shinobi",
        "email": "shinobi@example.com",
        "is_active": true,
        "roles": ["user", "admin"]
    }
}
"""

def validate_user_response(response_json):
    user = json.loads(response_json)
    assert user["status"] == "success", "Ожидался success"
    assert user["code"] == 200, "Ожидался HTTP-код 200"
    assert user["data"]["user_id"] == 15, "Ожидался id 15"
    assert user["data"]["is_active"] is True, "Ожидалось True"
    assert "admin" in user["data"]["roles"]
    return True

print(validate_user_response(response_json))