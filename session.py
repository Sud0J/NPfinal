class SessionManager:
    def __init__(self):
        self.username = None
        self.token = None

    def login(self, username, token):
        self.username = username
        self.token = token

    def logout(self):
        self.username = None
        self.token = None

    def is_authenticated(self):
        return self.username is not None and self.token is not None
