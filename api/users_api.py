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