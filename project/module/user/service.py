from .schema import UserUpdate
from .exception import NotFoundError
from .repository import UserRepo


class UserService:
    def __init__(self, repo: UserRepo):
        self.repo = repo

    def get_users(self):
        return self.repo.get_users()

    def find_user(self, user_id: int):
        user = self.repo.find_user(user_id)
        if user:
            return user
        raise NotFoundError(f"User with id: {user_id} not found")

    def update_user(self, user_id: int, user_payload: UserUpdate):
        self.find_user(user_id)
        self.repo.update_user(user_id, user_payload)

    def remove_user(self, user_id: int):
        self.find_user(user_id)
        self.repo.remove_user(user_id)
