users = [
    {"id": 1, "name": "Alex", "is_active": True},
    {"id": 2, "name": "Max", "is_active": False},
    {"id": 3, "name": "John", "is_active": True},
    {"id": 4, "name": "Kate", "is_active": False},
    {"id": 5, "name": "Anna", "is_active": True}
]

def get_active_users(users):
    for user in users:
        user.append({"id": user["id"], "name": user["name"], "is_active": user["is_active"]})
        if user["is_active": True]:
            return user["name"]
