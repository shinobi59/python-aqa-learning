class UsersAPI:
    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session

    def get_user(self, user_id):
        url = f"{self.base_url}/users/{user_id}"
        return self.session.get(url, timeout=10)

    def get_posts(self):
        url = f"{self.base_url}/posts"
        return self.session.get(url, timeout=10)

    def get_users(self):
        url = f"{self.base_url}/users"
        return self.session.get(url, timeout=10)

    def create_user(self, payload):
        url = f"{self.base_url}/users"
        return self.session.post(url, json=payload, timeout=10)

    def update_user(self, user_id, payload):
        url = f"{self.base_url}/users/{user_id}"
        return self.session.put(url, json=payload, timeout=10)

    def patch_user(self, user_id, payload):
        url = f"{self.base_url}/users/{user_id}"
        return self.session.patch(url, json=payload, timeout=10)

    def delete_user(self, user_id):
        url = f"{self.base_url}/users/{user_id}"
        return self.session.delete(url, timeout=10)
