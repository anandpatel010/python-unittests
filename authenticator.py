class Authenticator:
    def __init__(self):
        self.users = {}

    def register(self, username: str, password: str) -> bool:
        if username in self.users:
            return False
        if username and password:
            self.users[username] = password
            return True
        return False

    def login(self, username: str, password: str) -> bool:
        if username in self.users and self.users[username] == password:
            return True
        return False

    def change_password(self, username: str, old_password: str, new_password: str) -> bool:
        if self.login(username, old_password):
            self.users[username] = new_password
            return True
        return False

