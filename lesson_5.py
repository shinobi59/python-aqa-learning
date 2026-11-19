users = [
    {"id": 1, "name": "Alex", "is_active": True},
    {"id": 2, "name": "Max", "is_active": False},
    {"id": 3, "name": "John", "is_active": True},
    {"id": 4, "name": "Kate", "is_active": False},
    {"id": 5, "name": "Anna", "is_active": True}
]


def get_active_users(users):
    active_users = []
    for user in users:
        if user["is_active"] is True:
            active_users.append(user["name"])
    return active_users

print(get_active_users(users))