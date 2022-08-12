class User:
    users = []
    n_active = 0

    def __init__(self, active, username):
        self.active = active
        self.user_name = username
