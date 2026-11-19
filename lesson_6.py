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

user = json.loads(response_json)

def validate_user_response(user):
    assert user["status"] == "success"
    assert user["code"] == 200
    assert user["data"]["user_id"] == 15
    assert user["data"]["is_active"] is True
    assert ["admin"] in response_json["data"]["roles"]
    return True

print(validate_user_response)