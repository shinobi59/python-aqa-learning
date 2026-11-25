users_schema = {
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
        "company": {"type": "string"},
    }
}