# optional, can be used for user-related repository functions in the module


from sqlalchemy import select
from sqlalchemy.orm import Session

from .model import UserModel


class UserRepo:
    def __init__(self, db: Session):
        self.db = db

    def get_users(self):
        stmt = select(UserModel)
        return self.db.scalars(stmt).all()

    def find_user(self):
        pass

    def update_user(self):
        pass

    def remove_user(self):
        pass
