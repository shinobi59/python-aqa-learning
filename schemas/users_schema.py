user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "username": {"type": "string"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "phone": {"type": "string"},
        "website": {"type": "string"},
        "address": {"type": "object",
            "properties": {
            "street": {"type": "string"},
            "city": {"type": "string"},
            "zipcode": {"type": "string"},
        },
        "required": ["street", "city", "zipcode"]
        },
        "company": {"type": "object",
            "properties": {
                "name": {"type": "string"},
                "catchPhrase": {"type": "string"},
                "bs": {"type": "string"},
            },
            "required": ["name", "catchPhrase", "bs"]},
    },
    "required": ["id", "username", "name", "email", "phone", "website", "address", "company"]
}

users_schema = {
    "type": "array",
    "items": user_schema
}

created_user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"},
    },
    "required": ["id", "name", "username", "email"]
}