from .repository import UserRepo


class UserService:
    def __init__(self, repo: UserRepo):
        self.repo = repo

    def get_users(self):
        return self.repo.get_users()

    def find_user(self):
        pass

    def update_user(self):
        pass

    def remove_user(self):
        pass
